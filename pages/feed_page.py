from locators.general_locators import TEXT_ON_MAIN_PAGE, ACCOUNT
from locators.main_page_locators import FEED_BUTTON_ON_HEADER, INGREDIENT, ORDER_CONSTRUCTOR, MAKE_AN_ORDER, \
    CLOSE_WINDOW_BUTTON
from locators.personal_account_locators import LOGIN_EMAIL, LOGIN_PASSWORD, LOGIN_BUTTON
from .base_page import BasePage
from data import BASE_URL, EMAIL, PASSWORD, FEED
from locators.feed_page_locators import ANY_ORDER, LOADING_ORDER_NUMBER, \
    ORDER_NUMBER, LIST_ORDER_NUMBERS, ORDERS_OF_ALL_TIME, ORDERS_FOR_TODAY


class FeedPage(BasePage):

    def check_order_details(self):
        self.driver.get(BASE_URL)
        self.wait_for_modal_to_disappear()
        self.click_element(FEED_BUTTON_ON_HEADER)
        self.scroll_to_locator(ANY_ORDER)
        self.click_element(ANY_ORDER)


    def login_and_make_an_order(self):
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
        self.find_element(CLOSE_WINDOW_BUTTON)
        self.wait_for_modal_to_disappear()
        self.wait_for_modal_to_disappear()

    def get_track_num_order(self):
        self.wait_to_disappear(LOADING_ORDER_NUMBER)
        return int(self.get_text_from_element(ORDER_NUMBER))

    def get_track_num_order_from_list(self):
        self.wait_for_modal_to_disappear()
        return int(self.get_text_from_element(LIST_ORDER_NUMBERS))

    def get_all_orders_count(self):
        self.driver.get(f'{BASE_URL}{FEED}')
        return int(self.get_text_from_element(ORDERS_OF_ALL_TIME))

    def get_orders_for_today(self):
        self.driver.get(f'{BASE_URL}{FEED}')
        return self.get_text_from_element(ORDERS_FOR_TODAY)


