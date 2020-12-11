from selenium import webdriver
import keyboard
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path=r'D:\chromedriver.exe')
driver.get('http://facebook.com')
qwe = driver.find_element_by_xpath("//input[@id='email']")
qwe.send_keys('abc')
x = ActionChains(driver)
x.move_to_element(qwe).double_click().context_click().perform()