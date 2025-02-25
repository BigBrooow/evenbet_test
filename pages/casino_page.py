from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.main_page import MainPage
from locators.casino_page_locators import CasinoPageLocators


class CasinoPage(MainPage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_casino_page(self):
        self.click_casino_button()

    def open_first_game(self):
        WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(CasinoPageLocators.FIRST_GAME)
        ).click()
        WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(CasinoPageLocators.FIRST_GAME_PLAY_BUTTON)
        ).click()

    def assert_opened_game(self):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(CasinoPageLocators.GAME_SCREEN)
        ).is_displayed()
