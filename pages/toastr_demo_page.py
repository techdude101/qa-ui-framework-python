from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from seleniumpagefactory.Pagefactory import PageFactory


class ToastrDemoPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        "show_toast_button": ("ID", "showtoast"),
        "toast_message_input": ("ID", "message"),
    }

    def click_show_toast(self):
        self.show_toast_button.click()

    def set_toast_message(self, message):
        self.toast_message_input.set_text(message)

    def wait_for_toast_popup(self, timeout_in_seconds=10):
        toast_popup = WebDriverWait(self.driver, timeout_in_seconds).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "toast"))
        )

    def get_toast_message(self):
        toast_message = self.driver.find_element(By.CLASS_NAME, "toast-message")
        return toast_message.get_text()
