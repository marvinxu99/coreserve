# coreserve/app/services/db_user_service.py
import re
from datetime import datetime
import bcrypt

from app.extensions import db
from app.models import User
from app.utils import LoggingManager


logging_manager = LoggingManager()
logger = logging_manager.get_logger(__name__)


def is_hashed_password(password):
    # Bcrypt hash pattern typically starts with $2b$, $2a$, or $2y$ and is 60 chars long
    return bool(re.match(r"^\$2[aby]\$\d{2}\$.{53}$", password))


# CREATE: Add a new user with hashed password
def create_user(email, password):
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
        logger.error(f"Error creating user: {e}")
        return None

# READ: Retrieve a user by ID
def get_user_by_id(user_id):
    try:
        return User.query.get(user_id)
    except Exception as e:
        logger.error(f"Error retrieving user with ID {user_id}: {e}")
        return None

# READ: Retrieve a user by username
def get_user_by_username(username):
    try:
        return User.query.filter_by(username=username).first()
    except Exception as e:
        logger.error(f"Error retrieving user with username {username}: {e}")
        return None

# READ: Retrieve a user by username
def get_user_by_email(email):
    try:
        return User.query.filter_by(email=email).first()
    except Exception as e:
        logger.error(f"Error retrieving user with email {email}: {e}")
        return None

# READ: Retrieve all users
def get_all_users():
    try:
        return User.query.all()
    except Exception as e:
        logger.error(f"Error retrieving all users: {e}")
        return []

# UPDATE: Update an existing user's details
def update_user(user_id, username=None, email=None, password=None, name_first=None, name_last=None, name_middle=None):
    try:
        user = User.query.get(user_id)
        if user is None:
            print(f"User with ID {user_id} not found.")
            return None
        if username:
            user.username = username
        if email:
            user.email = email
        if password:
            user.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        if name_first:
            user.name_first = name_first
        if name_last:
            user.name_last = name_last
        if name_middle:
            user.name_middle = name_middle
        user.updt_dt_tm = datetime.now()
        db.session.commit()
        return user
    except Exception as e:
        db.session.rollback()
        logger.error(f"Error updating user with ID {user_id}: {e}")
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
        logger.error(f"Error deleting user with ID {user_id}: {e}")
        return False

def verify_password(email, password):
    """Verify the user's password, handling both plain text and hashed incoming passwords."""
    user = get_user_by_email(email)

    print(email, password )
    
    if user is None:
        return None

    # If the incoming password is already hashed, compare it directly
    if is_hashed_password(password):
        if password == user.password:
            return user
        else:
            return None

    else:
        # Otherwise, hash the incoming plain text password and compare
        if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            return user
        else:
            return None
