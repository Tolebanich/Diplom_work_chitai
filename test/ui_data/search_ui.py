from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


@allure.suite("UI тесты")
@allure.title("Тест поиска книг на сайте Читай-город.")
@allure.description("Тестирование поля поиска на сайте Читай-город.")
@allure.severity(allure.severity_level.BLOCKER)
@allure.feature("UI тесты")
class SearchUI:
    def __init__(self, driver):
        self.driver = driver
        self.search_field = (
            By.XPATH, '//input[@class="header-search__input"]'
            )

    def search_by_author(self, author_name: str) -> None:
        search_button = self.driver.find_element(
            By.CSS_SELECTOR, "button[aria-label='Искать']"
            )
        with allure.step("Выбор поисковой строки и ввод имени автора."):
            WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located(self.search_field)
            ).send_keys(author_name)
        with allure.step("Клик по кнопке поиска."):
            search_button.click()

    def search_by_title(self, title: str) -> None:
        search_button = self.driver.find_element(
            By.CSS_SELECTOR, "button[aria-label='Искать']"
            )
        with allure.step("Выбор поисковой строки и ввод названия книги."):
            WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located(self.search_field)
            ).send_keys(title)
        with allure.step("Клик по кнопке поиска."):
            search_button.click()

    def search_by_genre(self, genre: str) -> None:
        search_button = self.driver.find_element(
            By.CSS_SELECTOR, "button[aria-label='Искать']"
            )
        with allure.step("Выбор поисковой строки и ввод жанра книги."):
            WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located(self.search_field)
            ).send_keys(genre)
        with allure.step("Клик по кнопке поиска."):
            search_button.click()
