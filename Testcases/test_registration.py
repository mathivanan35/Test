from pages.new_registration import Register
from pages.page_objects import *


class TestRegister:
    def test_registration(self, browser):
        self.driver = browser
        self.b = Register(self.driver)
        self.b.home_page()
        self.b.cursor_action(registration)
        self.b.button(sign_up)
        self.b.exit_browser()

