# app/services/code_value_service.py
from app.extensions import db, cache
from app.models.code_value import CodeValue

@cache.memoize()
def get_code_values():
    """Fetches all CodeValue records, using caching based on environment settings."""
    return db.session.query(CodeValue).all()

def invalidate_code_values_cache():
    """Explicitly clears the cached CodeValue data."""
    cache.delete_memoized(get_code_values)
