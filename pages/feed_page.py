from locators.general_locators import GeneralLocators
from locators.main_page_locators import MainPageLocators
from locators.personal_account_locators import PersonalAccountLocators
from .base_page import BasePage
from data import BASE_URL, EMAIL, PASSWORD, FEED
from locators.feed_page_locators import FeedPageLocators


class FeedPage(BasePage):

    def check_order_details(self):
        self.driver.get(BASE_URL)
        self.wait_for_modal_to_disappear()
        self.click_element(MainPageLocators.FEED_BUTTON_ON_HEADER)
        self.scroll_to_locator(FeedPageLocators.ANY_ORDER)
        self.click_element(FeedPageLocators.ANY_ORDER)


    def login_and_make_an_order(self):
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
        self.find_element(MainPageLocators.CLOSE_WINDOW_BUTTON)
        self.wait_for_modal_to_disappear()

    def get_track_num_order(self):
        self.wait_to_disappear(FeedPageLocators.LOADING_ORDER_NUMBER)
        return int(self.get_text_from_element(FeedPageLocators.ORDER_NUMBER))

    def get_track_num_order_from_list(self):
        self.wait_for_modal_to_disappear()
        return int(self.get_text_from_element(FeedPageLocators.LIST_ORDER_NUMBERS))

    def get_all_orders_count(self):
        self.driver.get(f'{BASE_URL}{FEED}')
        return int(self.get_text_from_element(FeedPageLocators.ORDERS_OF_ALL_TIME))

    def get_orders_for_today(self):
        self.driver.get(f'{BASE_URL}{FEED}')
        return self.get_text_from_element(FeedPageLocators.ORDERS_FOR_TODAY)


