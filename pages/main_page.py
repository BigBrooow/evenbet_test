from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from test_data import BASE_URL


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_base_page(self):
        self.open(BASE_URL)

    def click_login_button(self):
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)
        ).click()

    def enter_login(self, login):
        WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(MainPageLocators.LOGIN_FIELD)
        ).send_keys(login)

    def enter_password(self, password):
        WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(MainPageLocators.PASSWORD_FIELD)
        ).send_keys(password)

    def click_submit_button(self):
        WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(MainPageLocators.SUBMIT_LOGIN_BUTTON)
        ).click()

    def assert_login(self):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(MainPageLocators.AVATAR)
        ).is_displayed()

    def click_casino_button(self):
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(MainPageLocators.CASINO_BUTTON)
        ).click()

    def click_register_button(self):
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(MainPageLocators.CASINO_BUTTON)
        ).click()

    def enter_name(self, name):
        WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(MainPageLocators.NAME_FIELD)
        ).send_keys(name)

    def enter_email(self, email):
        WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(MainPageLocators.EMAIL_FIELD)
        ).send_keys(email)

    def enter_first_password(self, password):
        WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(MainPageLocators.FIRST_PASSWORD_FIELD)
        ).send_keys(password)

    def confirm_password(self, password):
        WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(MainPageLocators.CONFIRM_PASSWORD)
        ).send_keys(password)

    def click_submit_register_button(self):
        WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(MainPageLocators.SUBMIT_EMAIL_BUTTON)
        ).click()