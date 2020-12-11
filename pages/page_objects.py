from selenium.webdriver.common.by import By

search_box = By.ID,'twotabsearchtextbox'
product_search = By.XPATH, "(//input[@type='submit'])[1]"
registration = By.XPATH, "//span[contains(text(),'Hello,')]"
sign_up = By.XPATH, "(//a[contains(text(),'Start here.')])[1]"
username = By.XPATH, "//input[@type='text']"
mobile_no = By.XPATH, "//input[@type='tel']"
email = By.XPATH, "//input[@type='email']"
password = By.XPATH, "//input[@type='password']"
