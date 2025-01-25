import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from api_data.cart_api import CartApi


@pytest.fixture(scope="session")
def browser():
    s = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def api_url():
    return "https://web-gate.chitai-gorod.ru/api"


@pytest.fixture(scope="session")
def ui_url():
    return 'https://www.chitai-gorod.ru'
