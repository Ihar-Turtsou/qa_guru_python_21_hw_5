import pytest
from selene import browser

@pytest.fixture()
def setup_browser():
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.config.timeout = 5
    yield
    browser.quit()