from app.extensions import db, cache
from sqlalchemy import select
from app.models.code_value import CodeValue
from app.models.code_value_set import CodeSet

# Global dictionaries to hold code values
g_display_codevalue = {}
g_displaykey_codevalue = {}
g_description_codevalue = {}
g_meaning_codevalue = {}
g_codevalue_display = {}


@cache.cached(key_prefix="global_code_values")
def get_global_cv_dicts():
    """Load global dictionaries with code values from CodeValue table."""
    global g_display_codevalue
    global g_displaykey_codevalue
    global g_description_codevalue
    global g_meaning_codevalue
    global g_codevalue_display

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
            g_display_codevalue[display, codeset] = code_value
            g_displaykey_codevalue[display_key, codeset] = code_value
            g_description_codevalue[description, codeset] = code_value

            if meaning:
                g_meaning_codevalue[meaning, codeset] = code_value

            g_codevalue_display[code_value] = display
    
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
        if type == 'DISPLAY':
            return g_display_codevalue[vstr, codeset]
        elif type == 'DISPLAYKEY':
            return g_displaykey_codevalue[vstr, codeset] 
        elif type == 'DESCRIPTION':
            return g_description_codevalue[vstr, codeset]
        elif type == 'MEANING':
            return g_meaning_codevalue[vstr, codeset]  
        else:
            return None
    except KeyError:
        return None


def uar_get_code_display(code_value):
    """ Get the code value's display  """
    get_global_cv_dicts()
    try:
        return g_codevalue_display[code_value]
    except KeyError:
        return None
