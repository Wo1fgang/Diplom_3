import allure

from data import BASE_URL, FORGOT_PASSWORD_PAGE, RESET_PASSWORD_PAGE
from locators.recover_password_locators import RecoverPasswordLocators
from pages.recover_password_page import RecoverPasswordPage


class TestRecoverPasswordPage:

    @allure.title('переход на страницу восстановления пароля по кнопке «Восстановить пароль»,')
    def test_open_recover_password_page(self, driver):
        browser = RecoverPasswordPage(driver)
        browser.open_recover_password_page()
        assert browser.get_current_url() == f'{BASE_URL}{FORGOT_PASSWORD_PAGE}'

    @allure.title('ввод почты и клик по кнопке «Восстановить»')
    def test_enter_email_click_recover(self, driver):
        browser = RecoverPasswordPage(driver)
        browser.enter_email_click_recover()
        assert browser.get_current_url() == f'{BASE_URL}{RESET_PASSWORD_PAGE}' and browser.find_element(RecoverPasswordLocators.RECOVER_PASSWORD_TEXT_AFTER_REDIRECT)

    @allure.title('клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_show_hide_password(self, driver):
        browser = RecoverPasswordPage(driver)
        browser.show_hide_password()
        assert browser.find_element(RecoverPasswordLocators.ACTIVE_RECOVER_PASSWORD_PAGE_PASSWORD_INPUT)