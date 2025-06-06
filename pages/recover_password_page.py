from selenium.webdriver import Keys

from .base_page import BasePage
from data import BASE_URL, FORGOT_PASSWORD_PAGE, EMAIL_TO_RECOVER_PASSWORD, RESET_PASSWORD_PAGE, SOME_PASSWORD
from locators.general_locators import ACCOUNT, TEXT_ON_MAIN_PAGE
from locators.recover_password_locators import FORGOT_PASSWORD_LINK, FORGOT_PASSWORD_EMAIL_TEXTBOX, \
    RECOVER_PASSWORD_TEXT_AFTER_REDIRECT, RECOVER_PASSWORD_PAGE_PASSWORD_INPUT, SHOW_HIDE_PASSWORD_EYE_BUTTON


class RecoverPasswordPage(BasePage):
    def open_recover_password_page(self):
        self.driver.get(BASE_URL)
        self.find_element(TEXT_ON_MAIN_PAGE)
        self.wait_for_modal_to_disappear()
        self.click_element(ACCOUNT)
        self.wait_for_modal_to_disappear()
        self.click_element(FORGOT_PASSWORD_LINK)

    def enter_email_click_recover(self):
        self.driver.get(f'{BASE_URL}{FORGOT_PASSWORD_PAGE}')
        self.find_element(FORGOT_PASSWORD_EMAIL_TEXTBOX)
        self.input_text(FORGOT_PASSWORD_EMAIL_TEXTBOX, EMAIL_TO_RECOVER_PASSWORD)
        self.find_element(FORGOT_PASSWORD_EMAIL_TEXTBOX).send_keys(Keys.ENTER)
        self.find_element(RECOVER_PASSWORD_TEXT_AFTER_REDIRECT)

    def show_hide_password(self):
        self.driver.get(f'{BASE_URL}{RESET_PASSWORD_PAGE}')
        self.find_element(FORGOT_PASSWORD_EMAIL_TEXTBOX).send_keys(Keys.ENTER)
        self.input_text(RECOVER_PASSWORD_PAGE_PASSWORD_INPUT, SOME_PASSWORD)
        self.click_element(SHOW_HIDE_PASSWORD_EYE_BUTTON)