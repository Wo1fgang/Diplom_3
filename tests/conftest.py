import pytest
from selenium import webdriver


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()

    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()


@pytest.fixture
def firefox():
    firefox = webdriver.Firefox()
    firefox.set_window_size(1920, 1080)
    yield firefox
    firefox.quit()


@pytest.fixture
def chrome():
    chrome = webdriver.Chrome()
    chrome.set_window_size(1920, 1080)
    yield chrome
    chrome.quit()
