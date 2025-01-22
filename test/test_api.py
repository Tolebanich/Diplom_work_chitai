from api_data.cart_api import CartApi
import allure

@allure.feature("Корзина")
@allure.title("Тест добавления книги в корзину. POSITIVE")
@allure.suite("API тесты")
@allure.severity(allure.severity_level.BLOCKER)
@allure.description("Проверка успешного добавления книги в корзину.")
def test_add_to_cart_positive():
    cart_api = CartApi('https://web-gate.chitai-gorod.ru/api/v1/cart/product')
    response = cart_api.add_to_cart(3060351)
    assert response.status_code == 200, f"Ошибка: {response.status_code}"

@allure.feature("Корзина")
@allure.title("Тест изменения количества книг в корзине. POSITIVE")
@allure.suite("API тесты")
@allure.severity(allure.severity_level.BLOCKER)
@allure.description("Проверка успешного изменения количества книг в корзине.")
def test_change_quantity_positive():
    cart_api = CartApi('https://web-gate.chitai-gorod.ru/api/v1/cart')
    response = cart_api.change_quantity(151230787, 2)
    assert response.status_code == 200, f"Ошибка: {response.status_code}"

@allure.feature("Корзина")
@allure.title("Тест удаления книги из корзины. POSITIVE")
@allure.suite("API тесты")
@allure.severity(allure.severity_level.BLOCKER)
@allure.description("Проверка успешного удаления книги из корзины.")
def test_delete_from_cart_positive():
    cart_api = CartApi('https://web-gate.chitai-gorod.ru/api/v1/cart/')
    response = cart_api.delete_from_cart(151230787)
    assert response.status_code == 204, f"Ошибка: {response.status_code}"

@allure.feature("Корзина")
@allure.title("Тест добавления книги в корзину. NEGATIVE")
@allure.suite("API тесты")
@allure.severity(allure.severity_level.BLOCKER)
@allure.description("Проверка неуспешного добавления книги c неверным айди в корзину.")
def test_add_to_cart_negative():
    cart_api = CartApi('https://web-gate.chitai-gorod.ru/api/v1/cart/product')
    response = cart_api.add_to_cart(1234568879)
    assert response.status_code == 500, f"Ошибка: {response.status_code}"

@allure.feature("Корзина")
@allure.title("Запрос без тела. NEGATIVE")
@allure.suite("API тесты")
@allure.severity(allure.severity_level.BLOCKER)
@allure.description("Проверка запроса без тела.")
def test_request_without_body():
    cart_api = CartApi('https://web-gate.chitai-gorod.ru/api/v1/cart/product')
    response = cart_api.no_body(1234568879)
    assert response.status_code == 422, f"Ошибка: {response.status_code}"