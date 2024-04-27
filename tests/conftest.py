"""Run Selenium tests in parallel with Python for Selenium Python tutorial"""

import os
import pytest

from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

capabilities_chrome = {
    "browserName": "chrome",
    "browserVersion": "122.0",
    "selenoid:options": {"enableVideo": False, "enableVNC": True},
}

capabilities_firefox = {
    "browserName": "firefox",
    "browserVersion": "124.0",
    "selenoid:options": {"enableVideo": False},
}

GRID_URL = os.environ.get("GRID_URL")
DEFAULT_WAIT_IN_SECONDS = 10


@pytest.fixture(scope="class", autouse=True)
def setup(request, browser):

    driver = None

    if browser == "chrome":
        driver = driver_init_chrome()
    elif browser == "firefox":
        driver = driver_init_firefox()

    request.cls.driver = driver
    yield
    driver.close()


@pytest.fixture(scope="class", autouse=True)
def browser(request):
    browser = request.config.getoption("--browser")
    if not browser:
        return "chrome"
    return browser


def pytest_addoption(parser):
    parser.addoption("--browser")


def driver_init_chrome():
    """Initialise a new Chrome WebDriver"""
    webdriver_chrome = None

    options = ChromeOptions()

    if GRID_URL:
        options.set_capability("selenoid:options", capabilities_chrome["selenoid:options"])

        webdriver_chrome = webdriver.Remote(command_executor=GRID_URL, options=options)
    else:
        service = ChromeService(ChromeDriverManager().install())
        # options.add_argument("--headless")
        webdriver_chrome = webdriver.Chrome(service=service, options=options)
    return webdriver_chrome


def driver_init_firefox():
    """Initialise a new Firefox WebDriver"""
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    return driver
