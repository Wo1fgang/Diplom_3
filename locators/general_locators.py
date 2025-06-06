from selenium.webdriver.common.by import By

ACCOUNT = By.LINK_TEXT, 'Личный Кабинет'
TEXT_ON_MAIN_PAGE = By.XPATH, '//h1[@class="text text_type_main-large mb-5 mt-10" and text()="Соберите бургер"]'

OVERLAYING_ELEMENT = By.XPATH, '//*[contains(@class,  "Modal_modal__loading")]/following::div[@class="Modal_modal_overlay__x2ZCr"]'
