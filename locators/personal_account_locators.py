from selenium.webdriver.common.by import By

LOGIN_EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input[@type='text']")
LOGIN_PASSWORD = (
    By.XPATH, "//label[text()='Пароль']/following-sibling::input[@type='password']")
LOGIN_BUTTON = (By.XPATH, "//*[contains(text(),'Войти')]")

LOGIN_PAGE_LOGIN_TEXT = (By.XPATH, "//*[contains(text(),'Вход')]")

ORDER_HISTORY = By.XPATH, '//a[@href="/account/order-history" and text()="История заказов"]'

COMPLETED_ORDER = By.XPATH, '//p[@class="OrderHistory_visible__19YMB text text_type_main-small mb-7" and contains(@style, "color: rgb(0, 204, 204)") and text()="Выполнен"]'

LOGOUT_BUTTON = (
    By.XPATH,
    "//button[contains(@class, 'Account_button__14Yp3') and text()='Выход']")