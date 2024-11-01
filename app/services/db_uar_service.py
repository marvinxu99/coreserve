from sqlalchemy import select

from app.models.code_value import CodeValue
from app import db

g_display_codevalue = {}
g_displaykey_codevalue = {}
g_description_codevalue = {}
g_meaning_codevalue = {}
g_codevalue_display = {}

def create_global_cv_dicts():
    global g_display_codevalue
    global g_displaykey_codevalue
    global g_description_codevalue
    global g_meaning_codevalue
    global g_codevalue_display

    with db.session() as session:
        stmt = select(
            CodeValue.display, 
            CodeValue.display_key, 
            CodeValue.description, 
            CodeValue.meaning,
            CodeValue.code_set, 
            CodeValue.code_value
        ).where(
            CodeValue.active_ind==True
        ).order_by(CodeValue.display)
        
        results = session.execute(stmt).all()

        for display, display_key, description, meaning, codeset, code_value in results:
            g_display_codevalue[display, codeset] = code_value
            g_displaykey_codevalue[display_key, codeset] = code_value
            g_description_codevalue[description, codeset] = code_value

            if meaning:
                g_meaning_codevalue[meaning, codeset] = code_value

            g_codevalue_display[code_value] = display


def uar_update_code_values():
    """Update the global uar code values"""
    create_global_cv_dicts()     


def uar_get_code_by(type, codeset, vstr):
    """ Get the code value by the type ('DISPLAY', 'DISPLAYKEY', 'DESCRIPTION') """
    try:
        if type == 'DISPLAY':
            return(g_display_codevalue[vstr, codeset])
        elif type == 'DISPLAYKEY':
            return(g_displaykey_codevalue[vstr, codeset])    
        elif type == 'DESCRIPTION':
            return(g_description_codevalue[vstr, codeset])    
        elif type == 'MEANING':
            return(g_meaning_codevalue[vstr, codeset])    
        else:
            return None
    except:
        return None


def uar_get_code_display(code_value):
    """ Get the code value's display  """
    try:
        return(g_codevalue_display[code_value])    
    except:
        return None


#test
if __name__ == '__main__':
    print(uar_get_code_by('MEANING', 79, 'PENDING'))
    print(uar_get_code_by('MEANING', 79, 'OVERDUE'))