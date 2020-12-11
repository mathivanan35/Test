from pages.homepage import HomePage
from pages.page_objects import *


class TestHomePage:
    def test_home(self, browser):
        self.driver = browser
        self.a = HomePage(self.driver)
        self.a.home_page()
        self.a.text_box(search_box,'macbook')
        self.a.button(product_search)
        self.a.exit_browser()
