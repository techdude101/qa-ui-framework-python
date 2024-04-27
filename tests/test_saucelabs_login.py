"""Test Examples - Saucelabs"""

import pytest
import allure

from src.pages.saucelabs_login_page import LoginPage


# NOTE: tests aren't found by pytest if a class has a constructor
# pylint: disable=too-few-public-methods
class TestSauceLabsLogin:
    """Saucelabs Login Tests"""

    @pytest.mark.parametrize("username, password",
                             [("standard_user", "secret_sauce"),
                              ("visual_user", "secret_sauce")])
    def test_saucelabs_login(self, base_webdriver, username, password):
        """Login tests"""
        base_url = "https://www.saucedemo.com"
        driver = base_webdriver
        login_page = LoginPage(driver)
        driver.maximize_window()

        with allure.step("Open the home page"):
            driver.get(base_url)

        with allure.step("Login"):
            login_page.enter_username(username)
            login_page.enter_password(password)
            login_page.click_login()

        with allure.step("Verify the home page is displayed"):
            png_bytes = driver.get_screenshot_as_png()
            allure.attach(
                png_bytes,
                name="Home Page",
                attachment_type=allure.attachment_type.PNG,
            )
            assert driver.current_url == base_url + "/inventory.html"
