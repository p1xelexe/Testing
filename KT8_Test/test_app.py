
import pytest
import allure
from app import get_json



@pytest.mark.asyncio
@allure.feature("JSON response")
@allure.story("Swagger Petstore API")
@allure.title("Test get_json with Swagger Petstore API")
@allure.severity(allure.severity_level.NORMAL)

async def test_get_first(event_loop):
    url = "https://petstore.swagger.io/v2/store/order/10"

    result = await get_json(url)
    assert result is not None
    assert "id" in result
    assert "petId" in result
    assert "quantity" in result



@pytest.mark.asyncio
@allure.story("Json PlaceHolder API")
@allure.title("Test get_json with Json PlaceHolder API")
@allure.severity(allure.severity_level.NORMAL)

async def test_get_second(event_loop):
    url = "https://jsonplaceholder.typicode.com/todos/1"

    result = await get_json(url)
    assert result is not None
    assert "title" in result



@pytest.mark.asyncio
@allure.story("Json Dog API")
@allure.title("Test get_json with Dog API")
@allure.severity(allure.severity_level.NORMAL)

async def test_get_third(event_loop):
    url = "https://dog.ceo/api/breeds/image/random"

    result = await get_json(url)
    assert result is not None
    assert "message" in result
    assert "status" in result