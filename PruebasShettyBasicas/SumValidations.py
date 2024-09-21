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
    result.click()

driver.find_element(By.CSS_SELECTOR, ".cart-icon").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
result = driver.find_element(By.CSS_SELECTOR, ".promoInfo").text

#Sum validation
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum += int(price.text)
print(sum)

totalAmount = driver.find_element(By.CSS_SELECTOR, ".totAmt").text
assert sum == int(totalAmount), "La suma de los precios no es igual al total"

driver.close()
driver.quit()
