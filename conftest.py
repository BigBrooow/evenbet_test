import pytest
from selenium import webdriver

from pages.main_page import MainPage
from test_data import LOGIN, PASSWORD


@pytest.fixture(scope='session')
def driver():
    chrome = webdriver.Chrome()
    yield chrome
    chrome.quit()


@pytest.fixture
def login(driver):
    page = MainPage(driver)
    page.open_base_page()
    page.click_login_button()
    page.enter_login(LOGIN)
    page.enter_password(PASSWORD)
    page.click_submit_button()
