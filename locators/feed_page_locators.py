from selenium.webdriver.common.by import By

ANY_ORDER = By.XPATH, '//p[@class="text text_type_main-default text_color_inactive" and contains(text(), "Сегодня")]'
ORDER_MODAL_WINDOW_TEXT = By.XPATH, '//p[@class="text text_type_main-medium mb-8" and text()="Cостав"]'
ORDER_HISTORY_ORDER_IN_PERSONAL_ACCOUNT = By.XPATH, '//p[@class="text text_type_digits-default" and contains(text(), "#{}")]'
LOADING_ORDER_NUMBER = By.CSS_SELECTOR, "img.Modal_modal__loading__3534A"
ORDER_NUMBER = By.CSS_SELECTOR, "h2.Modal_modal__title_shadow__3ikwq.Modal_modal__title__2L34m.text.text_type_digits-large.mb-8"
LIST_ORDER_NUMBERS = By.CSS_SELECTOR, "li.text.text_type_digits-default.mb-2"
ORDERS_OF_ALL_TIME = By.XPATH, "//p[@class='text text_type_main-medium' and text()='Выполнено за все время:']/following-sibling::*[1]"
ORDERS_FOR_TODAY = By.XPATH, "//p[@class='text text_type_main-medium' and text()='Выполнено за сегодня:']/following-sibling::*[1]"