from selenium.webdriver.common.by import By


class RecoverPasswordLocators:
    FORGOT_PASSWORD_LINK = By.XPATH, '//a[@class="Auth_link__1fOlj" and @href="/forgot-password" and text()="Восстановить пароль"]'
    FORGOT_PASSWORD_EMAIL_TEXTBOX = By.XPATH, '//input[@class="text input__textfield text_type_main-default" and @type="text" and @name="name"]'
    RECOVER_PASSWORD_BUTTON = (By.LINK_TEXT, '//button[contains(@class, "button_button__33qZ0") and contains(@class, "button_button_type_primary__1O7Bx") and contains(@class, "button_button_size_medium__3zxIa") and text()="Восстановить"]')
    RECOVER_PASSWORD_TEXT_AFTER_REDIRECT = By.XPATH, '//label[@class="input__placeholder text noselect text_type_main-default" and text()="Введите код из письма"]'
    SHOW_HIDE_PASSWORD_EYE_BUTTON = By.CSS_SELECTOR, 'svg[width="24"][height="24"][fill="#F2F2F3"]'
    RECOVER_PASSWORD_PAGE_PASSWORD_INPUT = By.XPATH, '//input[@type="password" and @name="Введите новый пароль"]'
    ACTIVE_RECOVER_PASSWORD_PAGE_PASSWORD_INPUT = By.XPATH, "//div[contains(@class, 'input') and contains(@class, 'input_type_text') and contains(@class, 'input_size_default') and contains(@class, 'input_status_active')]"
