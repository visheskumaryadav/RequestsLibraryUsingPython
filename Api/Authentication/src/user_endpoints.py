import requests
from Authentication.src.routes import Routes


class UserEndpoints:

    @classmethod
    def register_user(cls, headers, payload):
        url = Routes.register_user()
        return requests.post(url=url, headers=headers, json=payload)

    @classmethod
    def login_user(cls, headers, payload):
        url = Routes.login_user()
        return requests.post(url=url, headers=headers, json=payload)

    @classmethod
    def logout_user(cls, headers, payload):
        url = Routes.logout_user()
        return requests.post(url=url, headers=headers, json=payload)
    @classmethod
    def get_logged_in_user(cls, headers, payload):
        url = Routes.get_logged_in_user()
        return requests.post(url=url, headers=headers, json=payload)
