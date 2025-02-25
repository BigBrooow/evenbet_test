from generator import string_generator, email_generator
from pages.main_page import MainPage


def test_register_with_valid_data(driver):
    page = MainPage(driver)
    page.open_base_page()
    page.click_register_button()
    page.enter_name(string_generator(10))
    page.enter_email(email_generator())
    password = string_generator(10)
    page.enter_first_password(password)
    page.confirm_password(password)
    page.click_submit_register_button()
    assert page.assert_login()
