"""Run Selenium tests in parallel with Python for Selenium Python tutorial"""

import os
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

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


@pytest.fixture(scope="class")
def driver_init_remote_chrome(request):
    """Initialise a new Remote Chrome WebDriver"""

    options = webdriver.ChromeOptions()
    options.set_capability("selenoid:options", capabilities_chrome["selenoid:options"])

    web_driver = webdriver.Remote(command_executor=GRID_URL, options=options)

    request.cls.driver = web_driver
    yield
    web_driver.close()


@pytest.fixture(scope="class")
def driver_init_chrome(request):
    """Initialise a new Chrome WebDriver"""
    web_driver = None

    options = ChromeOptions()

    if GRID_URL:
        options.set_capability("selenoid:options", capabilities_chrome["selenoid:options"])

        web_driver = webdriver.Remote(command_executor=GRID_URL, options=options)
    else:
        service = ChromeService(ChromeDriverManager().install())
        # options.add_argument("--headless")
        options.set_capability("pageLoadStrategy", "eager")
        web_driver = webdriver.Chrome(service=service, options=options)

    request.cls.driver = web_driver
    yield
    web_driver.close()


@pytest.fixture(scope="class")
def driver_init_firefox(request):
    """Initialise a new Firefox WebDriver"""
    web_driver = webdriver.Firefox()

    request.cls.driver = web_driver

    yield

    web_driver.close()
