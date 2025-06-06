import allure

from data import BASE_URL, FEED
from locators.feed_page_locators import FeedPageLocators
from pages.feed_page import FeedPage


class TestFeedPage:

    @allure.title('Делаем заказ и нажимаем на него чтобы открыть всплывающее окно с деталями')
    def test_check_order_details(self, driver):
        browser = FeedPage(driver)
        browser.check_order_details()
        assert browser.find_element(FeedPageLocators.ORDER_MODAL_WINDOW_TEXT)

    @allure.title('заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов» / после оформления заказа его номер появляется в разделе В работе')
    def test_order_in_feed_order(self, driver):
        browser = FeedPage(driver)
        browser.login_and_make_an_order()
        order_number = browser.get_track_num_order()
        driver.get(f'{BASE_URL}{FEED}')
        assert order_number == browser.get_track_num_order_from_list()

    @allure.title('при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_completed_all_time_counter(self, driver):
        browser = FeedPage(driver)
        before = browser.get_all_orders_count()
        browser.login_and_make_an_order()
        after = browser.get_all_orders_count()

        assert before < after

    @allure.title('при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_completed_today_counter(self, driver):
        browser = FeedPage(driver)
        before = browser.get_orders_for_today()
        browser.login_and_make_an_order()
        after = browser.get_orders_for_today()

        assert before < after