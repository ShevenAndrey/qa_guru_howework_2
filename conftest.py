import pytest
from selene import browser


@pytest.fixture
def browser_config():
    browser.config.window_width = 1500
    browser.config.window_height = 800


@pytest.fixture
def browser_open_url():
    yield browser.open("https://google.com")
    browser.close()
