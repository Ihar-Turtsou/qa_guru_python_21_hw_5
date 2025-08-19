import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os
from selene import browser

@pytest.fixture(scope="session", autouse=True)
def load_env():
    path = os.path.join(os.getcwd(), ".env")
    load_dotenv(path)
    required = ["SELENOID_LOGIN", "SELENOID_PASS", "SELENOID_URL"]
    missing = [k for k in required if not os.getenv(k)]
    assert not missing, f"Missing env vars: {missing}  (pwd={os.getcwd()}, env_path={path})"


@pytest.fixture(scope="function")
def remote_browser_setup():

    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_pass = os.getenv("SELENOID_PASS")
    selenoid_url = os.getenv("SELENOID_URL")

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVideo": False
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
        options=options)

    browser.config.driver = driver
    yield browser
    browser.quit()