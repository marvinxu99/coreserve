import pytest
from unittest.mock import patch, MagicMock
from app import create_app, db, cache
from app.services.db_uar_service import (
    get_global_cv_dicts,
    uar_update_code_values,
    uar_get_code_by,
    uar_get_code_display,
    g_descriptor_cv,
    g_meaning_cv,
    g_cv_display
)

@pytest.fixture(scope="module")
def app():
    """Create and configure a new app instance for each test module."""
    app = create_app("testing")

    with app.app_context():
        # Directly create all tables for in-memory database
        db.create_all()
        cache.init_app(app)  # Ensure cache is initialized with app context

        yield app

        # Tear down by dropping all tables after tests
        db.drop_all()


@pytest.fixture
def mock_code_values():
    """Fixture to provide sample code value data."""
    return [
        ("Active", "ACTIVE", "Active status", "ACTIVE_MEANING", 48, 1),
        ("Pending", "PENDING", "Pending status", "PENDING_MEANING", 48, 2),
        ("New", "NEW", "New status", "NEW_MEANING", 48, 3),
    ]


@pytest.fixture
def clear_cache():
    """Clear cache and global dictionaries before each test."""
    g_descriptor_cv.clear()
    g_meaning_cv.clear()
    g_cv_display.clear()
    cache.clear()


def test_get_global_cv_dicts(app, mock_code_values, clear_cache):
    """Test that get_global_cv_dicts populates global dictionaries correctly."""
    with patch("app.services.db_uar_service.db.session") as mock_session:
        mock_session.query.return_value.filter.return_value.order_by.return_value.all.return_value = mock_code_values
        
        result = get_global_cv_dicts()
        assert result == "Cache populated with code values."

        assert g_descriptor_cv[("Active", 48)] == 1
        assert g_descriptor_cv[("ACTIVE", 48)] == 1
        assert g_descriptor_cv[("Active status", 48)] == 1

        assert g_meaning_cv[("ACTIVE_MEANING", 48)] == 1
        assert g_cv_display[1] == "Active"


def test_uar_update_code_values(app, mock_code_values, clear_cache):
    """Test that uar_update_code_values updates cache with new data."""
    with patch("app.services.db_uar_service.db.session") as mock_session:
        # Initial population of dictionaries with mock data
        mock_session.query.return_value.filter.return_value.order_by.return_value.all.return_value = mock_code_values
        get_global_cv_dicts()

        # Simulate cache update with additional mock data
        updated_code_values = mock_code_values + [("Inactive", "INACTIVE", "Inactive status", "INACTIVE_MEANING", 48, 4)]
        mock_session.query.return_value.filter.return_value.order_by.return_value.all.return_value = updated_code_values
        uar_update_code_values()

        # Verify new data is in cache
        assert g_descriptor_cv[("Inactive", 48)] == 4
        assert g_meaning_cv[("INACTIVE_MEANING", 48)] == 4
        assert g_cv_display[4] == "Inactive"


def test_uar_get_code_by(app, mock_code_values, clear_cache):
    """Test that uar_get_code_by retrieves the correct code values."""
    with patch("app.services.db_uar_service.db.session") as mock_session:
        mock_session.query.return_value.filter.return_value.order_by.return_value.all.return_value = mock_code_values
        get_global_cv_dicts()

        assert uar_get_code_by("DISPLAY", 48, "Active") == 1
        assert uar_get_code_by("DISPLAYKEY", 48, "ACTIVE") == 1
        assert uar_get_code_by("DESCRIPTION", 48, "Active status") == 1
        assert uar_get_code_by("MEANING", 48, "ACTIVE_MEANING") == 1
        assert uar_get_code_by("DISPLAY", 48, "NonExistent") is None


def test_uar_get_code_display(app, mock_code_values, clear_cache):
    """Test that uar_get_code_display retrieves the correct display values."""
    with patch("app.services.db_uar_service.db.session") as mock_session:
        mock_session.query.return_value.filter.return_value.order_by.return_value.all.return_value = mock_code_values
        get_global_cv_dicts()

        assert uar_get_code_display(1) == "Active"
        assert uar_get_code_display(2) == "Pending"
        assert uar_get_code_display(999) is None  # Non-existing code value
