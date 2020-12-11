from selenium import webdriver
import pytest


@pytest.fixture()
def browser():
    driver = webdriver.Chrome(executable_path=r'D:\chromedriver.exe')
    driver.maximize_window()
    return driver
