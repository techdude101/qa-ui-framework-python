"""Login Page"""
from seleniumpagefactory.Pagefactory import PageFactory


class LoginPage(PageFactory):
    """Login Page Class"""
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
        "user_name": ("ID", "user-name"),
        "password": ("ID", "password"),
        "login_btn": ("ID", "login-button"),
    }

    def enter_username(self, username):
        """Enter a username into an <input> field"""
        self.user_name.set_text(username)

    def enter_password(self, password):
        """Enter a password into an <input> field"""
        self.password.set_text(password)

    def click_login(self):
        """Click on the login button"""
        self.login_btn.click()
