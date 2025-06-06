from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as Wait

from locators.general_locators import OVERLAYING_ELEMENT
from data import script


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        Wait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        Wait(self.driver, 10).until(EC.presence_of_all_elements_located(locator))
        return self.driver.find_element(locator)

    def click_element(self, locator):
        Wait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    def input_text(self, locator, text):
        self.find_element(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element(locator).text

    def scroll_to_locator(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    def get_current_url(self):
        return self.driver.current_url

    def wait_to_disappear(self, locator):
        Wait(self.driver, 10).until(EC.invisibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def wait_for_modal_to_disappear(self):
        try:
            Wait(self.driver, 20).until_not(
                EC.visibility_of_element_located(OVERLAYING_ELEMENT)
            )
        except TimeoutException:
            raise TimeoutException("Модальное окно не исчезло в течение 20 секунд")

    def drag_and_drop(self, locator1, locator2):
        drag = Wait(self.driver, 20).until(
            EC.element_to_be_clickable(locator1))
        drop = Wait(self.driver, 20).until(
            EC.element_to_be_clickable(locator2))
        self.driver.execute_script(script, drag, drop)

