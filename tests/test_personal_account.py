import allure

from locators.personal_account_locators import PersonalAccountLocators
from pages.personal_account_page import PersonalAccountPage


class TestPersonalAccount:

    @allure.title('переход по клику на «Личный кабинет»')
    def test_click_account_link(self, driver):
        browser = PersonalAccountPage(driver)
        browser.click_account_link()
        assert browser.find_element(PersonalAccountLocators.LOGIN_BUTTON)

    @allure.title('переход в раздел «История заказов»')
    def test_click_order_history(self, driver):
        browser = PersonalAccountPage(driver)
        browser.click_order_history()
        assert browser.find_element(PersonalAccountLocators.COMPLETED_ORDER)

    @allure.title('выход из аккаунта')
    def test_logout(self, driver):
        browser = PersonalAccountPage(driver)
        browser.logout()
        assert browser.find_element(PersonalAccountLocators.LOGIN_EMAIL)