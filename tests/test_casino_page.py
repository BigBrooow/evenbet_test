from pages.casino_page import CasinoPage


def test_open_first_game(driver, login):
    page = CasinoPage(driver)
    page.open_casino_page()
    page.open_first_game()
    assert page.assert_opened_game()
