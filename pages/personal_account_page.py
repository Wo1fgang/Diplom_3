from locators.personal_account_locators import LOGIN_EMAIL, LOGIN_PASSWORD, LOGIN_BUTTON, ORDER_HISTORY, LOGOUT_BUTTON
from .base_page import BasePage
from data import BASE_URL, EMAIL, PASSWORD
from locators.general_locators import TEXT_ON_MAIN_PAGE, ACCOUNT


class PersonalAccountPage(BasePage):

    def click_account_link(self):
        self.driver.get(BASE_URL)
        self.wait_for_modal_to_disappear()
        self.find_element(TEXT_ON_MAIN_PAGE)
        self.wait_for_modal_to_disappear()
        self.click_element(ACCOUNT)


    def click_order_history(self):
        self.driver.get(BASE_URL)
        self.wait_for_modal_to_disappear()
        self.find_element(TEXT_ON_MAIN_PAGE)
        self.wait_for_modal_to_disappear()
        self.click_element(ACCOUNT)
        self.wait_for_modal_to_disappear()
        self.click_element(LOGIN_EMAIL)
        self.input_text(LOGIN_EMAIL, EMAIL)
        self.click_element(LOGIN_PASSWORD)
        self.input_text(LOGIN_PASSWORD, PASSWORD)
        self.click_element(LOGIN_BUTTON)
        self.wait_for_modal_to_disappear()
        self.click_element(ACCOUNT)
        self.wait_for_modal_to_disappear()
        self.click_element(ORDER_HISTORY)
        self.wait_for_modal_to_disappear()

    def logout(self):
        self.driver.get(BASE_URL)
        self.wait_for_modal_to_disappear()
        self.find_element(TEXT_ON_MAIN_PAGE)
        self.wait_for_modal_to_disappear()
        self.click_element(ACCOUNT)
        self.wait_for_modal_to_disappear()
        self.click_element(LOGIN_EMAIL)
        self.input_text(LOGIN_EMAIL, EMAIL)
        self.click_element(LOGIN_PASSWORD)
        self.input_text(LOGIN_PASSWORD, PASSWORD)
        self.click_element(LOGIN_BUTTON)
        self.wait_for_modal_to_disappear()
        self.click_element(ACCOUNT)
        self.wait_for_modal_to_disappear()
        self.click_element(LOGOUT_BUTTON)
        self.wait_for_modal_to_disappear()
        self.click_element(ACCOUNT)
        self.wait_for_modal_to_disappear()