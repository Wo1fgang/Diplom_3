import allure

from data import BASE_URL, FEED
from locators.main_page_locators import INGREDIENT_DETAILS_TEXT, FEED_BUTTON_ON_HEADER, INGREDIENT_COUNT, ORDER_ID_TEXT
from pages.main_page import MainPage


class TestMainPage:

    @allure.step('переход по клику на «Конструктор»')
    def test_click_constructor_link(self, driver):
        browser = MainPage(driver)
        browser.click_constructor_link()
        assert browser.get_current_url() == BASE_URL

    @allure.step('переход по клику на «Лента заказов»')
    def test_click_feed_link(self, driver):
        browser = MainPage(driver)
        browser.click_feed_link()
        assert browser.get_current_url() == f'{BASE_URL}{FEED}'

    @allure.step('если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_click_ingredient(self, driver):
        browser = MainPage(driver)
        browser.click_ingredient()
        assert browser.find_element(INGREDIENT_DETAILS_TEXT)

    @allure.step('всплывающее окно закрывается кликом по крестику')
    def test_close_ingredient_detail(self, driver):
        browser = MainPage(driver)
        browser.close_ingredient_detail()
        assert browser.find_element(FEED_BUTTON_ON_HEADER) and browser.get_current_url() == BASE_URL

    @allure.step('при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_add_ingredient_to_order(self, driver):
        browser = MainPage(driver)
        browser.add_ingredient_to_order()
        assert browser.find_element(INGREDIENT_COUNT)

    @allure.step('залогиненный пользователь может оформить заказ')
    def test_order_as_logged_user(self, driver):
        browser = MainPage(driver)
        browser.order_as_logged_user()
        assert browser.find_element(ORDER_ID_TEXT)