from database import add_record_to_database
import aiohttp
import pytest
import asyncio
import threading


# 1
async def async_function_resolve():
    return "Expected Value"


@pytest.mark.asyncio
async def test_async_function_resolve(event_loop):
    result = await async_function_resolve()
    assert result == "Expected Value"

# 2
async def async_function_error():
    raise ValueError("An expected error occurred.")


@pytest.mark.asyncio
async def test_failed_promise_rejection(event_loop):
    with pytest.raises(ValueError, match="An expected error occurred."):
        await async_function_error()


# 3
async def async_http_request():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://petstore.swagger.io/v2/user/string") as response:
            return await response.json()



@pytest.mark.asyncio
async def test_async_http_request(event_loop):
    result = await async_http_request()
    assert "id" in result
    assert "username" in result
    assert "firstName" in result
    assert "lastName" in result
    assert "email" in result
    assert "password" in result
    assert "phone" in result
    assert "userStatus" in result


# 4
@pytest.mark.asyncio
async def test_add_record_to_database(event_loop):
    data_to_insert = ("value1", "value2")
    result = await add_record_to_database(data_to_insert)

    assert result is not None


# 5
def run_async_function_in_thread(async_function, *args, **kwargs):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    result = None  # Инициализируем result заранее

    def run():
        nonlocal result  # Используем nonlocal для изменения переменной внутри вложенной функции
        result = loop.run_until_complete(async_function(*args, **kwargs))
        loop.stop()

    thread = threading.Thread(target=run)
    thread.start()
    thread.join()

    return loop, result

async def async_function_to_run():
    await asyncio.sleep(1)
    return "Async Function Result"

@pytest.mark.asyncio
async def test_run_async_function_in_thread(event_loop):
    loop, result = run_async_function_in_thread(async_function_to_run)
    assert result == "Async Function Result"
    loop.close()
