""" Database utility functions """

def db_get_or_create(session, model, **kwargs):
    """ Get the instance, or create it if it does not exist in database"""
    instance = session.query(model).filter_by(**kwargs).one_or_none()
    if instance:
        return instance
    else:
        instance = model(**kwargs)
        session.add(instance)
        session.commit()
        return instance

def db_get_or_add_instance(session, model, **kwargs):
    """ Get the row, add an instance it does not exist in database"""
    instance = session.query(model).filter_by(**kwargs).one_or_none()
    if instance:
        return instance
    else:
        instance = model(**kwargs)
        session.add(instance)
        return instance

def db_get_instance(session, model, **kwargs):
    """ Get the row, create it of not existed"""
    return session.query(model).filter_by(**kwargs).one_or_none()
