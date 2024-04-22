import time
import pytest
import allure

from pages.login_page import LoginPage
from pages.toastr_demo_page import ToastrDemoPage


@pytest.mark.usefixtures("driver_init_chrome")
class BasicTest:
    pass


class Test_Examples_Chrome(BasicTest):

    def test_saucelabs_login(self):

        login_page = LoginPage(self.driver)
        self.driver.maximize_window()
        
        with allure.step("Open the home page"):
            self.driver.get("https://www.saucedemo.com/")

        with allure.step("Login"):
            login_page.enter_username("standard_user")
            login_page.enter_password("secret_sauce")
            login_page.click_login()

    def test_lambdatest_todo_app(self):

        self.driver.maximize_window()
        
        with allure.step("Open the home page"):
            self.driver.get("https://lambdatest.github.io/sample-todo-app/")

            title = "Sample page - lambdatest.com"

            time.sleep(10)

            assert title == self.driver.title

    def test_lambdatest_load(self):

        self.driver.maximize_window()
        
        with allure.step("Open the home page"):
            self.driver.get("https://www.lambdatest.com/")


            expected_title = (
                "cross-browser Testing Tools | Free Automated Website Testing | LambdaTest"
            )

            time.sleep(10)

            png_bytes = self.driver.get_screenshot_as_png()
            allure.attach(
                png_bytes,
                name="Lambda Test Home Page",
                attachment_type=allure.attachment_type.PNG,
            )

            assert expected_title == self.driver.title
    
    def test_toastr_default_settings(self):
        """Toastr demo test"""
        self.driver.maximize_window()

        URL = "https://codeseven.github.io/toastr/demo.html"

        self.driver.get(URL)
        
        toastr_demo_page = ToastrDemoPage(self.driver)

        with allure.step("Open the demo page"):
            self.driver.get(URL)
            png_bytes = self.driver.get_screenshot_as_png()
            allure.attach(
                png_bytes,
                name="Toastr Demo Page",
                attachment_type=allure.attachment_type.PNG,
            )
        
        with allure.step("Show the default toast message"):
            toastr_demo_page.click_show_toast()
            png_bytes = self.driver.get_screenshot_as_png()
            allure.attach(
                png_bytes,
                name="Show toast",
                attachment_type=allure.attachment_type.PNG,
            )
            toastr_demo_page.wait_for_toast_popup()
        with allure.step("Verify toast message"):
            png_bytes = self.driver.get_screenshot_as_png()
            allure.attach(
                png_bytes,
                name="Toast displayed",
                attachment_type=allure.attachment_type.PNG,
            )
            message = toastr_demo_page.get_toast_message()
            assert message == "My name is Inigo Montoya. You killed my father. Prepare to die!"
    
    def test_toastr_custom_message(self):
        """Toastr demo test - custom message"""
        self.driver.maximize_window()

        URL = "https://codeseven.github.io/toastr/demo.html"

        TOAST_MESSAGE = "Testing 123"

        self.driver.get(URL)
        
        toastr_demo_page = ToastrDemoPage(self.driver)

        with allure.step("Open the demo page"):
            self.driver.get(URL)
            png_bytes = self.driver.get_screenshot_as_png()
            allure.attach(
                png_bytes,
                name="Toastr Demo Page",
                attachment_type=allure.attachment_type.PNG,
            )
        
        with allure.step("Set the toast message text"):
            toastr_demo_page.set_toast_message(TOAST_MESSAGE)

        with allure.step("Show the toast message"):
            toastr_demo_page.click_show_toast()
            png_bytes = self.driver.get_screenshot_as_png()
            allure.attach(
                png_bytes,
                name="Show toast",
                attachment_type=allure.attachment_type.PNG,
            )
            toastr_demo_page.wait_for_toast_popup()
        with allure.step("Verify toast message"):
            png_bytes = self.driver.get_screenshot_as_png()
            allure.attach(
                png_bytes,
                name="Toast displayed",
                attachment_type=allure.attachment_type.PNG,
            )
            message = toastr_demo_page.get_toast_message()
            assert TOAST_MESSAGE == message