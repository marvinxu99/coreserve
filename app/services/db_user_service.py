# coreserve/app/services/db_user_service.py
import re
from datetime import datetime
import bcrypt

from app.extensions import db
from app.models import User
from app.utils import convert_to_key,is_valid_email
from flask import current_app


def is_hashed_password(password):
    # Bcrypt hash pattern typically starts with $2b$, $2a$, or $2y$ and is 60 chars long
    return bool(re.match(r"^\$2[aby]\$\d{2}\$.{53}$", password))


# CREATE: Add a new user with hashed password
def create_user(email, password):
    
    if not is_valid_email(email):
        return None
    
    try:
        hashed_password = password if is_hashed_password(password) else bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        new_user = User(
            email=email,
            password=hashed_password.decode('utf-8'),
            create_dt_tm=datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()
    
        return new_user
    
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(f"Error creating user: {e}")
        return None

# READ: Retrieve a user by ID
def get_user_by_id(user_id):
    try:
        return User.query.get(user_id)
    except Exception as e:
        current_app.logger.error(f"Error retrieving user with ID {user_id}: {e}")
        return None

# READ: Retrieve a user by username
def get_user_by_username(username):
    try:
        return User.query.filter_by(username=username).first()
    except Exception as e:
        current_app.logger.error(f"Error retrieving user with username {username}: {e}")
        return None

# READ: Retrieve a user by username
def get_user_by_email(email):
    try:
        return User.query.filter_by(email=email).first()
    except Exception as e:
        current_app.logger.error(f"Error retrieving user with email {email}: {e}")
        return None

# READ: Retrieve all users
def get_all_users():
    try:
        return User.query.all()
    except Exception as e:
        current_app.logger.error(f"Error retrieving all users: {e}")
        return []

# UPDATE: Update an existing user's details
def update_user(
    user_id, 
    username=None, 
    email=None, 
    password=None, 
    name_first=None, 
    name_last=None, 
    name_middle=None,
    is_confirmed=None,
    is_active=None,
):
    try:
        user = User.query.get(user_id)
        if user is None:
            current_app.logger.info(f"User with ID {user_id} not found.")
            return None

        # Update user fields conditionally
        updates = {
            "username": username,
            "email": email,
            "name_first": name_first,
            "name_middle": name_middle,
            "name_last": name_last,
            "is_confirmed": is_confirmed,
            "is_active": is_active,
        }

        # Apply updates for each provided value
        for field, value in updates.items():
            if value is not None:
                setattr(user, field, value)

        # Handle password update separately with hashing
        if password:
            user.password = (
                password if is_hashed_password(password) 
                else bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            )

        # Convert names to keys if updated
        if name_first:
            user.name_first_key = convert_to_key(name_first)
        if name_last:
            user.name_last_key = convert_to_key(name_last)

        # Update derived fields
        user.updt_cnt += 1
        user.updt_dt_tm = datetime.now()
        user.name_full_format = f"{user.name_first or ''} {user.name_last or ''}".strip() or ' '

        db.session.commit()
        return user

    except Exception as e:
        db.session.rollback()
        current_app.logger.error(f"Error updating user with ID {user_id}: {e}")
        return None
    

# DELETE: Delete a user by ID
def delete_user(user_id):
    try:
        user = User.query.get(user_id)
        if user is None:
            print(f"User with ID {user_id} not found.")
            return False
        db.session.delete(user)
        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(f"Error deleting user with ID {user_id}: {e}")
        return False

def verify_password(email, password):
    """Verify the user's password, handling both plain text and hashed incoming passwords."""
    user = get_user_by_email(email)    
    if not user:
        return None

    # If the incoming password is already hashed, compare it directly
    if is_hashed_password(password):
        return user if password == user.password else None
    
    # Otherwise, hash the incoming plain text password and compare
    return user if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')) else None
