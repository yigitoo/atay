from typing import Any
from time import time as get_timestamp

from config import Config
from user import User


class DBMS:
    def __init__(self, config: dict = None):
        if config is None:
            self.config = Config().GetDBConfig()
        else:
            self.config = config

    def login(username: str = None, password: str = None) -> User:
        result = None

        #TODO: create a find sql query.

        if result not in [None, False]:
            return User.create({
                "username": result.username,
                "user_id": result.user_id,
                "is_admin": result.is_admin,
                "added_structures": result.added_structures
            })

    def get_user_by_id(user_id: str) -> User:
        #TODO: create a find sql query and return user from db.
        pass

    def create_user(self, user: dict = None):
        #TODO: check user and insert into database.
        pass

    def delete_user(self, user: dict = None):
        #TODO: check user and delete from database.
        pass

    def create_structures(self, struct: dict = None):
        #TODO: check structure and insert into database.
        pass

    def delete_structures(self, struct: dict = None):
        pass


    def create_complaint(self, user_id, struct_id):
        complaint_epoch = round(get_timestamp())
        #TODO: check complaint and insert into database.


# Some tests
if __name__ == '__main__':
    pass
