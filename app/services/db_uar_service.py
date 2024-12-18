from app.extensions import db, cache
from sqlalchemy import select
from app.models.code_value import CodeValue
from app.models.code_value_set import CodeSet

# Global dictionaries to hold code values
g_descriptor_cv = {}    # Descriptor includes display, displaykey, description
g_meaning_cv = {}
g_cv_display = {}       # Code value to display


@cache.cached(key_prefix="global_code_values")
def get_global_cv_dicts():
    """Load global dictionaries with code values from CodeValue table."""
    global g_descriptor_cv
    global g_meaning_cv
    global g_cv_display
    
    with db.session() as session:
        # Querying the CodeValue table with db.session.query()
        results = (
            db.session.query(
                CodeValue.display,
                CodeValue.display_key,
                CodeValue.description,
                CodeValue.meaning,
                CodeValue.code_set,
                CodeValue.code_value
            )
            .filter(CodeValue.active_ind == True)
            .order_by(CodeValue.display)
            .all()
        )

        for display, display_key, description, meaning, codeset, code_value in results:
            g_descriptor_cv[display, codeset] = code_value
            g_descriptor_cv[display_key, codeset] = code_value
            g_descriptor_cv[description, codeset] = code_value
            if meaning:
                g_meaning_cv[meaning, codeset] = code_value
            if code_value:
                g_cv_display[code_value] = display
    
        print("Just refreshed global codevalue dicts.")

    # Return something to store in the cache
    return "Cache populated with code values."


def uar_update_code_values():
    """Update the global uar code values"""
    cache.delete("global_code_values")
    get_global_cv_dicts()


def uar_get_code_by(type, codeset, vstr):
    """ Get the code value by the type ('DISPLAY', 'DISPLAYKEY', 'DESCRIPTION') """
    get_global_cv_dicts()
    try:
        if type in ('DISPLAY', 'DISPLAYKEY', 'DESCRIPTION'):
            return g_descriptor_cv[vstr, codeset]
        elif type == 'MEANING':
            return g_meaning_cv[vstr, codeset]  
        else:
            return None
    except KeyError:
        return None


def uar_get_code_display(code_value):
    """ Get the code value's display  """
    get_global_cv_dicts()
    try:
        return g_cv_display[code_value]
    except KeyError:
        return None
