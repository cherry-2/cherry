
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(Service=s)
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
print(driver.title)
print(driver.current_url)
driver.maximise_window
driver.refresh
driver.close
'''from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By'''