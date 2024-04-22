import time
import pytest
import allure

from pages.login_page import LoginPage


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
