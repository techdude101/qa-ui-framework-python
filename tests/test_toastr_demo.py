"""Test Examples - Toastr Demo Site"""

import allure

from src.pages.toastr_demo_page import ToastrDemoPage


class TestToastrDemo:
    """Tests for the Toastr Demo Site"""

    def test_toastr_default_settings(self, base_webdriver):
        """Toastr demo test"""
        driver = base_webdriver
        driver.maximize_window()

        url = "https://codeseven.github.io/toastr/demo.html"

        driver.get(url)

        toastr_demo_page = ToastrDemoPage(driver)

        with allure.step("Open the demo page"):
            driver.get(url)
            png_bytes = driver.get_screenshot_as_png()

            allure.attach(
                png_bytes,
                name="Toastr Demo Page",
                attachment_type=allure.attachment_type.PNG,
            )

        with allure.step("Show the default toast message"):
            toastr_demo_page.click_show_toast()
            png_bytes = driver.get_screenshot_as_png()

            allure.attach(
                png_bytes,
                name="Show toast",
                attachment_type=allure.attachment_type.PNG,
            )
            toastr_demo_page.wait_for_toast_popup()
        with allure.step("Verify toast message"):
            png_bytes = driver.get_screenshot_as_png()

            allure.attach(
                png_bytes,
                name="Toast displayed",
                attachment_type=allure.attachment_type.PNG,
            )
            message = toastr_demo_page.get_toast_message()
            assert message == "My name is Inigo Montoya. You killed my father. Prepare to die!"

    def test_toastr_custom_message(self, base_webdriver):
        """Toastr demo test - custom message"""
        driver = base_webdriver
        driver.maximize_window()

        url = "https://codeseven.github.io/toastr/demo.html"

        toast_message = "Testing 123"

        driver.get(url)

        toastr_demo_page = ToastrDemoPage(driver)

        with allure.step("Open the demo page"):
            driver.get(url)
            png_bytes = driver.get_screenshot_as_png()

            allure.attach(
                png_bytes,
                name="Toastr Demo Page",
                attachment_type=allure.attachment_type.PNG,
            )

        with allure.step("Set the toast message text"):
            toastr_demo_page.set_toast_message(toast_message)

        with allure.step("Show the toast message"):
            toastr_demo_page.click_show_toast()
            png_bytes = driver.get_screenshot_as_png()

            allure.attach(
                png_bytes,
                name="Show toast",
                attachment_type=allure.attachment_type.PNG,
            )
            toastr_demo_page.wait_for_toast_popup()
        with allure.step("Verify toast message"):
            png_bytes = driver.get_screenshot_as_png()

            allure.attach(
                png_bytes,
                name="Toast displayed",
                attachment_type=allure.attachment_type.PNG,
            )
            message = toastr_demo_page.get_toast_message()
            assert toast_message == message
