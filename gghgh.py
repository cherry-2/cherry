

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\\chromedriver.exe")

driver = webdriver.Chrome(service=s)
driver.implicitly_wait(5)
list1 = []
list2 = []
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Search for Vegetables and Fruits"]').send_keys('ber')
buttons = driver.find_elements(By.XPATH, '//div[@class="product-action"]/button')
vegetables = driver.find_elements(By.CSS_SELECTOR, 'h4.product-name')
for veg in vegetables:
    list1.append(veg.text)
for button in buttons:
    button.click()
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, '//button[text()=PROCEED TO CHECKOUT]').click()
fruits = driver.find_elements(By.CSS_SELECTOR, 'p[class="product-name"]')
for fruit in fruits:
    list2.append(fruit.text)
assert list1 == list2

driver.find_element(By.CLASS_NAME, 'promoCode').send_keys('rahulshettyacademy')


driver.find_element(By.CSS_SELECTOR,'button[css="1"]').click()






