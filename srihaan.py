import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--ignore-certificate-errors")
s = Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=s,options= chrome_options)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
print(driver.title)
driver.find_element(By.CSS_SELECTOR,"input[class*='search-keyword']").send_keys("brocolli")
time.sleep(5)
print(driver.find_element(By.CSS_SELECTOR,"input[class*='search-keyword']").text)
print(driver.find_element(By.CSS_SELECTOR,"input[class*='search-keyword']").get_attribute("value"))
'''print(driver.execute_script('return document.getElementsByClassName("search-keyword")[0].value)'))
# driver.execute_script('return document.get')'''
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
