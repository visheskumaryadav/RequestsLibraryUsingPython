import pytest
from Authentication.src.user_endpoints import UserEndpoints

parameters = [
    {
        "email": "s8ruy@yopmail.com",
        "password": "12345678",
        "role": "ADMIN",
        "username": "su8ary77"
    },
    {
        "email": "m8onry@yopmail.com",
        "password": "Adin123",
        "role": "ADMIN",
        "username": "morn8day44"
    },
    {
        "email": "w8erd@gmail.com",
        "password": "we8d66",
        "role": "ADMIN",
        "username": "weidrhr"
    }

]


@pytest.fixture(scope="class", params=parameters)
def post_register_user(request):
    print("----------------------SENDING post_register_user REQUEST---------------------------- ", end="\n")
    print(f"payload>>{request.param}", end="\n")
    global headers, response
    headers = {"accept": "application/json", "Content-Type": "application/json"}
    response = UserEndpoints.register_user(headers=headers, payload=request.param)
    print("----------------------Executing TestCases----------------------------------------- ", end="\n")
    print(f"RESPONSE::::>>{response.json()}", end="\n")

    payload = request.param
    yield [payload, response, headers]
    print("----------------------Execution Complete------------------------------------------ ")


class TestRegisterUser:

    def test_status_code(self, post_register_user):
        assert response.status_code in [200, 201] and response.json().get(
            "success") == True, "status code is not 200/success is not true"

    def test_message(self, post_register_user):
        assert response.json().get("message") == ("Users registered successfully and verification email has been sent "
                                                  "on your email."), "Message is incorrect"

    def test_data_existence(self, post_register_user):
        assert "data" in response.json(), "Data is absent in the response"

    def test_user_attributes(self, post_register_user):
        user = response.json()["data"]["user"]

        assert user["_id"] is not None, "user id is none"
        assert user["username"] == post_register_user[0]["username"], "username is not correct"
        assert user["email"] == post_register_user[0]["email"], "email is not correct"
        assert user["role"] == post_register_user[0]["role"], "role is not correct"
        assert user["isEmailVerified"] == False, "Email is already verified"
        assert user["loginType"] == "EMAIL_PASSWORD"
