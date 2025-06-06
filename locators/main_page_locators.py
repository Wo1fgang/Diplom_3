from selenium.webdriver.common.by import By


FEED_BUTTON_ON_HEADER = By.XPATH, '//p[@class="AppHeader_header__linkText__3q_va ml-2" and text()="Лента Заказов"]'
TEXT_ON_FEED_PAGE = By.XPATH, '//h1[@class="text text_type_main-large mt-10 mb-5" and text()="Лента заказов"]'
CONSTRUCTOR_BUTTON_ON_HEADER = By.XPATH, '//p[@class="AppHeader_header__linkText__3q_va ml-2" and text()="Конструктор"]'
INGREDIENT = By.XPATH, '//p[@class="BurgerIngredient_ingredient__text__yp3dH" and text()="Флюоресцентная булка R2-D3"]'
INGREDIENT_DETAILS_TEXT = By.XPATH, '//h2[contains(@class, "Modal_modal__title") and text()="Детали ингредиента"]'
CLOSE_WINDOW_BUTTON = By.XPATH, '//button[contains(@class, "Modal_modal__close")]'
ORDER_CONSTRUCTOR = By.XPATH, '//ul[@class="BurgerConstructor_basket__list__l9dp_"]'
INGREDIENT_COUNT = By. XPATH, '//p[@class="counter_counter__num__3nue1" and text()="2"]'
MAKE_AN_ORDER = By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and text()='Оформить заказ']"
ORDER_ID_TEXT = By.XPATH, '//p[contains(@class, "text_type_main-medium") and text()="идентификатор заказа"]'