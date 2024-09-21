import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.implicitly_wait(5)  # This is a global wait, it will wait for 5 seconds before throwing an exception

varAssert = "Code applied ..!"


driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
products = driver.find_elements(By.XPATH, "//div[@class='product-action']") # Devuelve una lista de elementos
#por lo que no devolvera una excepcion si no encuentra el elemento, se recomienda explicit wait  ->  List = []
count = len(products)
assert count > 0  # If there are products, the test will continue

for result in products:
    result.click()
    #time.sleep(2)   # This is a bad practice, we should use waits

driver.find_element(By.CSS_SELECTOR, ".cart-icon").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
result = driver.find_element(By.CSS_SELECTOR, ".promoInfo").text

print(result)
assert result == varAssert

driver.close()
driver.quit()
