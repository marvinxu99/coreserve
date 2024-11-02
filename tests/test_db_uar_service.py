import pytest
from unittest.mock import patch, MagicMock
from app import create_app
from app.extensions import db, cache
from app.services.db_uar_service import (
    create_global_cv_dicts,
    uar_update_code_values,
    uar_get_code_by,
    uar_get_code_display,
    g_display_codevalue,
    g_displaykey_codevalue,
    g_description_codevalue,
    g_meaning_codevalue,
    g_codevalue_display,
)
from app.models.user import Users
from alembic.config import Config
from alembic import command
from app.config import config


@pytest.fixture(scope="module")
def app():
    """Create and configure a new app instance for each test module."""
    app = create_app("testing")

    with app.app_context():
        # Directly create all tables for in-memory database
        from app.models.code_value import CodeValue
        from app.models.code_value_set import CodeSet
        
        db.create_all()

        yield app

        # Tear down by dropping all tables after tests
        db.drop_all()

@pytest.fixture
def mock_session():
    """Fixture to mock the database session and provide sample data."""
    with patch('app.services.db_uar_service.db.session') as mock_session:
        yield mock_session

@pytest.fixture
def mock_code_values():
    """Fixture to provide sample code value data."""
    return [
        ("Active", "ACTIVE", "Active status", "ACTIVE", 48, 1),
        ("Pending", "PENDING", "Pending status", "PENDING", 48, 2),
    ]

@pytest.fixture
def clear_cache(app):
    """Fixture to clear the cache and global dictionaries before each test."""
    yield
    g_display_codevalue.clear()
    g_displaykey_codevalue.clear()
    g_description_codevalue.clear()
    g_meaning_codevalue.clear()
    g_codevalue_display.clear()
    cache.clear()

def test_create_global_cv_dicts_caching(app, mock_session, mock_code_values, clear_cache):
    """Test that create_global_cv_dicts loads data and caches it properly."""
    # Mock the session query to return the test data
    stmt = MagicMock()
    stmt.execute.return_value.all.return_value = mock_code_values
    mock_session.execute.return_value = stmt

    # Run the function to load data into cache
    with app.app_context():
        create_global_cv_dicts()

    assert g_display_codevalue[("Active", 48)] == 1
    assert g_displaykey_codevalue[("ACTIVE", 48)] == 1
    assert g_description_codevalue[("Active status", 48)] == 1
    assert g_meaning_codevalue[("ACTIVE", 48)] == 1
    assert g_codevalue_display[1] == "Active"

    # Verify cache is set
    assert cache.get("global_code_values") is not None

def test_uar_update_code_values(app, mock_session, mock_code_values, clear_cache):
    """Test that uar_update_code_values refreshes cache with new data."""
    # Load initial data
    with app.app_context():
        create_global_cv_dicts()

    # Modify mock data to simulate an update
    mock_code_values.append(("New", "NEW", "New status", "NEW", 48, 3))
    stmt = MagicMock()
    stmt.execute.return_value.all.return_value = mock_code_values
    mock_session.execute.return_value = stmt

    # Run the update function to reload cache
    with app.app_context():
        uar_update_code_values()

    # Check if the new data is loaded
    assert g_display_codevalue[("New", 48)] == 3
    assert g_displaykey_codevalue[("NEW", 48)] == 3
    assert g_description_codevalue[("New status", 48)] == 3
    assert g_meaning_codevalue[("NEW", 48)] == 3
    assert g_codevalue_display[3] == "New"

def test_uar_get_code_by(app, mock_session, mock_code_values, clear_cache):
    """Test that uar_get_code_by retrieves the correct code values."""
    with app.app_context():
        create_global_cv_dicts()
    
    assert uar_get_code_by("DISPLAY", 48, "Active") == 1
    assert uar_get_code_by("DISPLAYKEY", 48, "ACTIVE") == 1
    assert uar_get_code_by("DESCRIPTION", 48, "Active status") == 1
    assert uar_get_code_by("MEANING", 48, "ACTIVE") == 1

    # Test for non-existing entry
    assert uar_get_code_by("DISPLAY", 48, "NonExistent") is None

def test_uar_get_code_display(app, mock_session, mock_code_values, clear_cache):
    """Test that uar_get_code_display retrieves the correct display values."""
    with app.app_context():
        create_global_cv_dicts()

    assert uar_get_code_display(1) == "Active"
    assert uar_get_code_display(2) == "Pending"
    assert uar_get_code_display(999) is None  # Test for non-existing code_value
