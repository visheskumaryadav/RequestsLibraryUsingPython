class Routes:
    base_url = "https://api.freeapi.app/api/v1"

    @classmethod
    def register_user(cls):
        return cls.base_url + "/users/register"

    @classmethod
    def login_user(cls):
        return cls.base_url + "/users/login"

    @classmethod
    def logout_user(cls):
        return cls.base_url + "/users/logout"

    @classmethod
    def get_logged_in_user(cls):
        return cls.base_url + "/users/current-user"

    @classmethod
    def assign_role(cls, userId):
        return cls.base_url + f"/users/assign-role/{userId}"
