# coreserve/app/services/db_user_service.py

from app.models.user import User
from app import db
import bcrypt

class UserService:
    @staticmethod
    def create_user(username, email):
        user = User(username=username, email=email)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def db_create_user(username, email, password):
        """Create a user with username, email, hashed password"""
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        user = User(username=username, email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def get_user_by_username(username):
        """Query user by userame"""
        return User.query.get(username=username)

    @staticmethod
    def verify_password(username, password):
        """Verify the user's passowrd"""
        user = UserService.get_user_by_username(username)
        if user is not None:
            return bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8'))
        else:
            return False


###############################################################################
# Testing
##########################
if __name__ == "__main__":

    # Create the users table
    # Base.metadata.create_all(engine)

    # Create test users
    # # 1. create a test user
    username = 'wesley1'
    email = "test@gmail.com"
    password = '1234'
    UserService.create_user(username, email, password)

    # # # 2. create a test user
    # username = 'winter1'
    # email = "test2@gmail.com"
    # password = '1234'
    # db_create_user(username, email, password)

    # result = query_user_by_username('winter1')
    # if result is not None:
    #     print(result.user_id, result.password)
    # else:
    #     print("None")     

    result = UserService.verify_password('winter1', '12345')
    print(result)