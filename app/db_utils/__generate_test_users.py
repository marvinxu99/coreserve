from app.models import User
from app.services import create_user
from flask import current_app


def create_test_users_(db):
    current_app.logger.info("Startinng to create users")

    # Example of creating users
    try:
        # create_user(username, email, password, name_first, name_last, name_middle=None)
        user1 = create_user("winter3", "winter2@example.com", "123456", "Winter", "Xu")
        user2 = create_user("wesley3", "wesley2@example.com", "123456", "Wesley", "Xu")
        
        current_app.logger.info("Test users created successfully")

    except Exception as e:
        current_app.logger.error(f"Error creating test users: {e}")
        db.session.rollback()