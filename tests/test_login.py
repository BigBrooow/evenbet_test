from pages.main_page import MainPage
from test_data import LOGIN, PASSWORD


def test_register_with_valid_data(driver):
    page = MainPage(driver)
    page.open_base_page()
    page.click_login_button()
    page.enter_login(LOGIN)
    page.enter_password(PASSWORD)
    page.click_submit_button()
    assert page.assert_login()
