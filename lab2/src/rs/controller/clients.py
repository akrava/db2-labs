import re
from rs.wrappers.set import Set
from rs.settings import USERS_SET_NAME, ADMINS_SET_NAME, USERS_ONLINE_SET_NAME


class Clients:
    def __init__(self):
        self.__users = Set(USERS_SET_NAME)
        self.__admins = Set(ADMINS_SET_NAME)
        self.__online_users = Set(USERS_ONLINE_SET_NAME)

    def register_client(self, username: str, is_admin: bool = False):
        if not self.validate_username(username):
            raise Exception("Username is not valid: use only `a-zA-Z0-9_`, minimal length is 4")
        target_set = self.__users
        set_to_check = self.__admins
        if is_admin:
            target_set, set_to_check = set_to_check, target_set

        if set_to_check.contains(username) or not target_set.add(username):
            raise Exception("Client with username `%s` has already registered" % username)

    def is_client(self, username: str):
        return self.is_admin(username) or self.is_user(username)

    def is_admin(self, username: str):
        return self.__admins.contains(username)

    def is_user(self, username: str):
        return self.__users.contains(username)

    """
    :return True if admin, False if user or None if not registered
    """
    def login_client(self, username: str):
        if self.__admins.contains(username):
            return True
        elif self.__users.contains(username):
            self.__online_users.add(username)
            return False
        return None

    def logout_user(self, username: str):
        self.__online_users.remove(username)

    @staticmethod
    def validate_username(username: str):
        return re.match("^[a-zA-Z0-9_]{4,}$", username)

    def get_all_users(self):
        return self.__users.get_all()

    def get_all_users_online(self):
        return self.__online_users.get_all()
