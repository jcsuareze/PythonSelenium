import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.implicitly_wait(2)
varAssert = "Code applied ..!"
wait = WebDriverWait(driver, 10)

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")

#Solo en algunas ocasiones es util usar time.sleep(2)
time.sleep(2)

products = wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH, "//div[@class='product-action']"))) #  ->  List = []

for result in products:
    print(result.text)
    #result.click()
  # This is a bad practice, we should use waits
'''
driver.find_element(By.CSS_SELECTOR, ".cart-icon").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

#Esperara HASTA por 10 segundos antes de lanzar una expcecion unicamente por el elemento seleccionado
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))  #ojo,  usar dos parentesis
result = driver.find_element(By.CSS_SELECTOR, ".promoInfo").text

print(result)
assert result == varAssert
'''
driver.close()
driver.quit()
