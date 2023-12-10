import requests
import pytest
from pydantic import BaseModel
import allure

base_url = "https://petstore.swagger.io/v2/"


class UserResponse(BaseModel):
    id: int
    username: str
    firstName: str
    lastName: str
    email: str
    password: str
    phone: str
    userStatus: int


class AnswerOrderResponse(BaseModel):
    id: int
    petId: int
    quantity: int
    shipDate: str
    status: str
    complete: bool


class AnswerUserResponse(BaseModel):
    code: int
    type: str
    message: str


@allure.feature("User API")
class TestPetUsers:

    @allure.title("GET /user")
    def test_get_user(self):
        response_user = requests.get(base_url + "user/string")
        assert response_user.status_code == 200
        with allure.step("Check the response JSON"):
            user_data = response_user.json()
            UserResponse(**user_data)
        allure.attach(response_user.text, "Response", allure.attachment_type.JSON)

    @allure.title("POST /user")
    def test_post_user(self):
        data = {"id": 1, "username": "new_user", "firstname": "string", "lastname": "string",
                "email": "user@example.com", "password": "string", "phone": "79096895085", "userStatus": 0}
        response_post_user = requests.post(base_url + "user", json=data)
        assert response_post_user.status_code == 200
        with allure.step("Check the response JSON"):
            user_data = response_post_user.json()
            AnswerUserResponse(**user_data)
        allure.attach(response_post_user.text, "Response", allure.attachment_type.JSON)


@allure.feature("Store API")
class TestPetStore:

    @allure.title("GET /store")
    def test_get_store(self):
        response_store = requests.get(base_url + "store/inventory")
        assert response_store.status_code == 200
        with allure.step("Check the response JSON"):
            store_data = response_store.json()
        allure.attach(response_store.text, "Response", allure.attachment_type.JSON)


    @allure.title("GET /order")
    def test_post_order(self):
        data = {"id": 0, "petId": 0, "quantity": 0, "shipDate": "2023-11-17T08:03:55.254Z", "status": "placed", "complete": True}
        response_order = requests.post(base_url + "store/order", json=data)
        assert response_order.status_code == 200
        with allure.step("Check the response JSON"):
            order_data = response_order.json()
            AnswerOrderResponse(**order_data)
        allure.attach(response_order.text, "Response", allure.attachment_type.JSON)


if __name__ == "__main__":
    pytest.main()