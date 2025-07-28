import pytest
from selene import browser

@pytest.fixture()
def setup_browser():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 5
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.quit()