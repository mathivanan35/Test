import openpyxl
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains


class DataDriven:
    def __init__(self,driver):
        self.driver = driver


    def home_page(self):
        self.driver.get('http://amazon.in')

    def cursor_action(self, ele):
        wait = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(ele))
        ActionChains(self.driver).move_to_element(wait).perform()

    def button(self, ele):
        wait = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(ele))
        wait.click()

    def text_box(self, ele, data):
        wait = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(ele))
        wait.clear()
        wait.send_keys(data)

    def exit_browser(self):
        self.driver.close()
