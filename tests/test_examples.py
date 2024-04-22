import time
import pytest

from pages.login_page import LoginPage

@pytest.mark.usefixtures("driver_init_chrome")
class BasicTest:
    pass


class Test_URL_Chrome(BasicTest):

    def test_saucelabs_login(self):
        
        self.driver.get("https://www.saucedemo.com/")
        
        self.driver.maximize_window()
        
        login_page = LoginPage(self.driver)
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()


    def test_lambdatest_todo_app(self):

        self.driver.get("https://lambdatest.github.io/sample-todo-app/")

        self.driver.maximize_window()

        title = "Sample page - lambdatest.com"

        time.sleep(10)

        assert title == self.driver.title

    def test_lambdatest_load(self):

        self.driver.get("https://www.lambdatest.com/")

        self.driver.maximize_window()

        expected_title = (
            "cross-browser Testing Tools | Free Automated Website Testing | LambdaTest"
        )

        time.sleep(10)

        assert expected_title == self.driver.title
