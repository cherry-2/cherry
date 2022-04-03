from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT,"Click Here").click()
driver.switch_to.window(driver.window_handles[1])
print(driver.find_element(By.TAG_NAME,"h3").text)
driver.switch_to.window(driver.window_handles[0])
print(driver.find_element(By.TAG_NAME,"h3").text)