from operator import and_
from sqlalchemy import delete, select, and_
from sqlalchemy.orm import Session

from core.models.db_base import engine
from core.models.db_working_view import WorkingView
from core.db_request.db_esh_event_sets import db_get_wv_section_details
from core.models.db_working_view_item import WorkingViewItem
from core.models.db_working_view_section import WorkingViewSection


def _load_working_view_bands():
    """
    Creating working views (bands)  
    """

    wv_band_data = [
        # Working View (Band) Display Name
        "Furry Friend Quick View",
        "Furry Friend Systems Assessment",
    ]

    # TODO: to remove, FOR TEST ONLY
    temp_updt_id = 5

    with Session(engine) as session:       

        for band_disp_name in wv_band_data:
            
            # Check if the band already exists? If not, create it
            kw = {
                'display_name': band_disp_name
            }
            # check if the band already exists in working_view table
            band_row = session.query(WorkingView).filter_by(**kw).one_or_none()
            if not band_row:
                band_row = WorkingView(**kw)
                band_row.updt_id = temp_updt_id,
                session.add(band_row)

        session.commit()


def _load_iview_sections_to_views():
    """
    Load iView sections indicated by (v1_event_set_code.event_set_name) to the view indicated by the working_view.display_name
    """

    wv_band_sections_data = [
        # Band Display Name             # Section Display                   # section_ES_name                   # Include_IND
        ("Furry Friend Quick View", (    
                                        ("Vital Signs",                     "Vital Signs",                      True),
                                        ("Measurements",                    "Measurements1",                    True),
                                    )),

        ("Furry Friend Systems Assessment", (
                                        ("Furry Friend Care/Monitoring",    "Furry Friend Care/Monitoring",     True),
                                        ("Furry Friend Training",           "Furry Friend Training",            True),
                                    )),

    ]

    # TODO: to remove, FOR TEST ONLY
    temp_updt_id = 5

    with Session(engine) as session:       

        for band_disp, sections in wv_band_sections_data:
            
            # (1) Check if the band name exisit in the working_view table
            kw = {
                'display_name': band_disp
            }
            # check if the band already exists in working_view table. If not, create it
            band_row = session.query(WorkingView).filter_by(**kw).one_or_none()
            if not band_row:
                band_row = WorkingView(**kw)
                band_row.updt_id = temp_updt_id,
                session.add(band_row)
                session.flush([band_row])

            # (2) Adding sections to the view
            for section in sections:

                section_disp = section[0]
                section_name = section[1]
                
                # (2a) check if the section event_set_name is in working_view_section table. 
                # If not, add the section to working_view_section table
                kw = {
                    'working_view_id'   : band_row.working_view_id,
                    'event_set_name'    : section_name,
                }
                sect_row = session.query(WorkingViewSection).filter_by(**kw).one_or_none()
                if sect_row is None:
                    sect_row = WorkingViewSection(**kw)
                    sect_row.display_name = section_disp
                    sect_row.updt_id = temp_updt_id
                    session.add(sect_row)
                    session.flush([sect_row])

                else:
                    if sect_row.display_name != section_disp:   # Update the display_name if needed.
                        sect_row.display_name = section_disp
                        sect_row.updt_id = temp_updt_id
                        sect_row.updt_cnt = sect_row.updt_cnt + 1 
                        session.add(sect_row)

                    # (2a1) Refesh the section by remove all the items, and then add them back.
                    kw = {
                        "working_view_section_id": sect_row.working_view_section_id
                    }
                    wv_item_rows = session.query(WorkingViewItem).filter_by(**kw).all()
                    for item in wv_item_rows:
                        session.delete(item)

                # (2b) Get all the items from the Working_view_sections, then add them to the table
                section_items = db_get_wv_section_details(section_name)
                for item in section_items:
                    kw = {
                        'working_view_section_id'       : sect_row.working_view_section_id,
                        'primitive_event_set_name'      : item[0],
                        'parent_event_set_name'         : item[1], 
                    }
                    item_row = session.query(WorkingViewItem).filter_by(**kw).one_or_none()
                    if not item_row:
                        item_row = WorkingViewItem(**kw)
                        item_row.updt_id = temp_updt_id,
                        session.add(item_row)

        session.commit()


# Testing stuff
if __name__ == "__main__":
    # _load_working_views()
    _load_iview_sections_to_views()
    pass