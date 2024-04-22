from seleniumpagefactory.Pagefactory import PageFactory


class LoginPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        "user_name": ("ID", "user-name"),
        "password": ("ID", "password"),
        "login_btn": ("ID", "login-button"),
    }

    def enter_username(self, username):
        self.user_name.set_text(username)

    def enter_password(self, password):
        self.password.set_text(password)

    def click_login(self):
        self.login_btn.click()
