from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

@allure.suite("UI тесты")
@allure.title("Тест добавления и удаления книг в корзину на сайте Читай-город.")
@allure.description("Тестирование добавления и удаления книг в корзину на сайте Читай-город.")
@allure.severity(allure.severity_level.BLOCKER)
@allure.feature("Корзина")
class CartUI:
    def __init__(self, driver):
        self.driver = driver
        self.search_field = (By.XPATH, '//input[@class="header-search__input"]')
        self.add_to_cart_button = (By.XPATH, "//div[@class='button action-button blue']")
        self.pop_close = (By.XPATH, "//div[@class='popmechanic-close']")

    def add_to_cart(self, book_name: str) -> None:
        search_button = self.driver.find_element(By.CSS_SELECTOR, "button[aria-label='Искать']")
        
        with allure.step("Выбор поисковой строки и ввод имени автора."):
            WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located(self.search_field)
            ).send_keys(book_name)
        with allure.step("Клик по кнопке поиска."):
            search_button.click()
        with allure.step("Выбор книги и добавление в корзину."):
            add_to_cart_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.add_to_cart_button)
            )
            pop_close = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(self.pop_close)
            )
            pop_close.click()
            self.driver.execute_script("window.scrollBy(0, 300);")
            self.driver.execute_script("window.scrollBy(0, 300);")
            self.driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart_btn)
            add_to_cart_btn.click()
