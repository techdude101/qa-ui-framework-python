"""Toastr Demo Page"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from seleniumpagefactory.Pagefactory import PageFactory


class ToastrDemoPage(PageFactory):
    """Toastr Demo Page Class"""
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
        "show_toast_button": ("ID", "showtoast"),
        "toast_message_input": ("ID", "message"),
    }

    def click_show_toast(self):
        """Click on the show toast button"""
        self.show_toast_button.click()

    def set_toast_message(self, message):
        """Set the message to be displayed in the toastr popup"""
        self.toast_message_input.set_text(message)

    def wait_for_toast_popup(self, timeout_in_seconds=10):
        """Wait for the toast popup to be displayed"""
        _ = WebDriverWait(self.driver, timeout_in_seconds).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, "toast"))
        )

    def get_toast_message(self):
        """Get the toast message displayed in the popup"""
        toast_message = self.driver.find_element(By.CLASS_NAME, "toast-message")
        return toast_message.get_text()
