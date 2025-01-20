import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
from ui_data.search_ui import SearchUI
import allure
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.chitai-gorod.ru')
    yield driver
    driver.quit()

@allure.feature("Поиск")
@allure.title("Тест поиска книг на сайте Читай-город по автору. POSITIVE")
@allure.suite("UI тесты")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Проверка проводится на наличие элемента 'Товары'. Если данного элемента нет - поиск неудачный.")
def test_search_by_author(driver):
    search_ui = SearchUI(driver)
    search_ui.search_by_author('Лев Толстой')
    with allure.step("Проверка успешного поиска по автору книги."):
        result_find = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='app-tabs__btn app-tabs__btn--active']"))
        )
        result_text = result_find.text
        assert result_text == "Товары"

@allure.feature("Поиск")
@allure.title("Тест поиска книг на сайте Читай-город по названию. POSITIVE")
@allure.suite("UI тесты")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Проверка проводится на наличие элемента 'Товары'. Если данного элемента нет - поиск неудачный.")
def test_search_by_title(driver):
    search_ui = SearchUI(driver)
    search_ui.search_by_title('Война и мир')
    with allure.step("Проверка успешного поиска по названию книги."):
        result_find = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='app-tabs__btn app-tabs__btn--active']"))
        )
        result_text = result_find.text
        assert result_text == "Товары"

@allure.feature("Поиск")
@allure.title("Тест поиска книг на сайте Читай-город по жанру. POSITIVE")
@allure.suite("UI тесты")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Проверка проводится на наличие элемента 'Товары'. Если данного элемента нет - поиск неудачный.")
def test_search_by_genre(driver):
    search_ui = SearchUI(driver)
    search_ui.search_by_genre('Роман')
    with allure.step("Проверка успешного поиска по жанру книги."):
        result_find = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='app-tabs__btn app-tabs__btn--active']"))
        )
        result_text = result_find.text
        assert result_text == "Товары"

@allure.feature("Поиск")
@allure.title("Тест поиска книг на сайте Читай-город по автору. NEGATIVE")
@allure.suite("UI тесты")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Проверка поиска по автору которого нет.")
def test_search_by_author_negative(driver):
    search_ui = SearchUI(driver)
    with allure.step("Поиск книг c отправкой пустого поля."):
        search_ui.search_by_author('Уфуфуфуфуфуфуф')
    with allure.step("Проверка наличия сообщения о неудачном поиске."):
        result_find = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h4[@class='catalog-empty-result__header']"))
        )
        result_text = result_find.text
        assert result_text == "Похоже, у нас такого нет"

@allure.feature("Поиск")
@allure.title("Тест поиска книг на сайте Читай-город по названию. NEGATIVE")
@allure.suite("UI тесты")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Проверка поиска по названию в котором присутствуют спецсимволы.")
def test_search_by_title_negative(driver):
    search_ui = SearchUI(driver)
    with allure.step("Поиск книг c отправкой названия в котором есть спецсимволы."):
        search_ui.search_by_title('!!"№Война и мир')
    with allure.step("Проверка наличия сообщения о поиске."):
        result_find = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='app-tabs__btn app-tabs__btn--active']"))
        )
        result_text = result_find.text
        assert result_text == "Товары"

@allure.feature("Поиск")
@allure.title("Тест поиска книг на сайте Читай-город по названию. NEGATIVE")
@allure.suite("UI тесты")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Проверка поиска по названию которое в верхнем регистре.")
def test_search_by_title_negative(driver):
    search_ui = SearchUI(driver)
    with allure.step("Поиск книг c отправкой названия в верхнем регистре."):
        search_ui.search_by_title('!!"№Война и мир')
    with allure.step("Проверка наличия сообщения о поиске."):
        result_find = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='app-tabs__btn app-tabs__btn--active']"))
        )
        result_text = result_find.text
        assert result_text == "Товары"
