from data import BASE_URL, EMAIL, PASSWORD
from locators.general_locators import TEXT_ON_MAIN_PAGE, ACCOUNT
from locators.main_page_locators import FEED_BUTTON_ON_HEADER, TEXT_ON_FEED_PAGE, CONSTRUCTOR_BUTTON_ON_HEADER, \
    INGREDIENT, CLOSE_WINDOW_BUTTON, ORDER_CONSTRUCTOR, MAKE_AN_ORDER
from locators.personal_account_locators import LOGIN_EMAIL, LOGIN_PASSWORD, LOGIN_BUTTON
from .base_page import BasePage



class MainPage(BasePage):

    def click_constructor_link(self):
        self.driver.get(BASE_URL)
        self.wait_for_modal_to_disappear()
        self.click_element(FEED_BUTTON_ON_HEADER)
        self.find_element(TEXT_ON_FEED_PAGE)
        self.click_element(CONSTRUCTOR_BUTTON_ON_HEADER)


    def click_feed_link(self):
        self.driver.get(BASE_URL)
        self.wait_for_modal_to_disappear()
        self.click_element(FEED_BUTTON_ON_HEADER)

    def click_ingredient(self):
        self.driver.get(BASE_URL)
        self.wait_for_modal_to_disappear()
        self.click_element(INGREDIENT)

    def close_ingredient_detail(self):
        self.driver.get(BASE_URL)
        self.wait_for_modal_to_disappear()
        self.click_element(INGREDIENT)
        self.click_element(CLOSE_WINDOW_BUTTON)
        self.wait_for_modal_to_disappear()
        self.click_element(FEED_BUTTON_ON_HEADER)
        self.click_element(CONSTRUCTOR_BUTTON_ON_HEADER)

    def add_ingredient_to_order(self):
        self.driver.get(BASE_URL)
        self.wait_for_modal_to_disappear()
        self.drag_and_drop(INGREDIENT, ORDER_CONSTRUCTOR)

    def order_as_logged_user(self):
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
        self.drag_and_drop(INGREDIENT, ORDER_CONSTRUCTOR)
        self.click_element(MAKE_AN_ORDER)