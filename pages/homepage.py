from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def home_page(self):
        self.driver.get('http://amazon.in')

    def text_box(self, ele, data):
        wait = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(ele))
        wait.send_keys(data)

    def button(self, ele):
        wait = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(ele))
        wait.click()

    def exit_browser(self):
        self.driver.close()
