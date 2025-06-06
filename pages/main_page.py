from data import BASE_URL, EMAIL, PASSWORD
from locators.general_locators import GeneralLocators
from locators.main_page_locators import MainPageLocators
from locators.personal_account_locators import PersonalAccountLocators
from .base_page import BasePage



class MainPage(BasePage):

    def click_constructor_link(self):
        self.driver.get(BASE_URL)
        self.wait_for_modal_to_disappear()
        self.click_element(MainPageLocators.FEED_BUTTON_ON_HEADER)
        self.find_element(MainPageLocators.TEXT_ON_FEED_PAGE)
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON_ON_HEADER)


    def click_feed_link(self):
        self.driver.get(BASE_URL)
        self.wait_for_modal_to_disappear()
        self.click_element(MainPageLocators.FEED_BUTTON_ON_HEADER)

    def click_ingredient(self):
        self.driver.get(BASE_URL)
        self.wait_for_modal_to_disappear()
        self.click_element(MainPageLocators.INGREDIENT)

    def close_ingredient_detail(self):
        self.driver.get(BASE_URL)
        self.wait_for_modal_to_disappear()
        self.click_element(MainPageLocators.INGREDIENT)
        self.click_element(MainPageLocators.CLOSE_WINDOW_BUTTON)
        self.wait_for_modal_to_disappear()
        self.click_element(MainPageLocators.FEED_BUTTON_ON_HEADER)
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON_ON_HEADER)

    def add_ingredient_to_order(self):
        self.driver.get(BASE_URL)
        self.wait_for_modal_to_disappear()
        self.drag_and_drop(MainPageLocators.INGREDIENT, MainPageLocators.ORDER_CONSTRUCTOR)

    def order_as_logged_user(self):
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
        self.drag_and_drop(MainPageLocators.INGREDIENT, MainPageLocators.ORDER_CONSTRUCTOR)
        self.click_element(MainPageLocators.MAKE_AN_ORDER)
