from locators.general_locators import GeneralLocators
from locators.personal_account_locators import PersonalAccountLocators
from data import BASE_URL, EMAIL, PASSWORD
from .base_page import BasePage


class PersonalAccountPage(BasePage):

    def click_account_link(self):
        self.driver.get(BASE_URL)
        self.wait_for_modal_to_disappear()
        self.find_element(GeneralLocators.TEXT_ON_MAIN_PAGE)
        self.wait_for_modal_to_disappear()
        self.click_element(GeneralLocators.ACCOUNT)


    def click_order_history(self):
        self.driver.get(BASE_URL)
        self.wait_for_modal_to_disappear()
        self.find_element(GeneralLocators.TEXT_ON_MAIN_PAGE)
        self.wait_for_modal_to_disappear()
        self.click_element(GeneralLocators.ACCOUNT)
        self.wait_for_modal_to_disappear()
        self.click_element(PersonalAccountLocators.LOGIN_EMAIL)
        self.input_text(PersonalAccountLocators.LOGIN_EMAIL, EMAIL)
        self.click_element(PersonalAccountLocators.LOGIN_PASSWORD)
        self.input_text(PersonalAccountLocators.LOGIN_PASSWORD, PASSWORD)
        self.click_element(PersonalAccountLocators.LOGIN_BUTTON)
        self.wait_for_modal_to_disappear()
        self.click_element(GeneralLocators.ACCOUNT)
        self.wait_for_modal_to_disappear()
        self.click_element(PersonalAccountLocators.ORDER_HISTORY)
        self.wait_for_modal_to_disappear()

    def logout(self):
        self.driver.get(BASE_URL)
        self.wait_for_modal_to_disappear()
        self.find_element(GeneralLocators.TEXT_ON_MAIN_PAGE)
        self.wait_for_modal_to_disappear()
        self.click_element(GeneralLocators.ACCOUNT)
        self.wait_for_modal_to_disappear()
        self.click_element(PersonalAccountLocators.LOGIN_EMAIL)
        self.input_text(PersonalAccountLocators.LOGIN_EMAIL, EMAIL)
        self.click_element(PersonalAccountLocators.LOGIN_PASSWORD)
        self.input_text(PersonalAccountLocators.LOGIN_PASSWORD, PASSWORD)
        self.click_element(PersonalAccountLocators.LOGIN_BUTTON)
        self.wait_for_modal_to_disappear()
        self.click_element(GeneralLocators.ACCOUNT)
        self.wait_for_modal_to_disappear()
        self.click_element(PersonalAccountLocators.LOGOUT_BUTTON)
        self.wait_for_modal_to_disappear()
        self.click_element(GeneralLocators.ACCOUNT)
        self.wait_for_modal_to_disappear()