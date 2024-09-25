import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.implicitly_wait(2)
wait = WebDriverWait(driver, 10)


driver.find_element(By.XPATH, "//a[contains(@href,'shop')]").click()
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for product in products:
    productName = product.find_element(By.XPATH, "div/h4/a").text
    if productName == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()
        break

driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
driver.find_element(By.CSS_SELECTOR, "button[class*='btn-success']").click()

driver.find_element(By.XPATH, "//input[@id='country']").send_keys("un")
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "United States of America"))).click()
driver.find_element(By.CSS_SELECTOR, "div[class*='checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

successText = driver.find_element(By.CSS_SELECTOR, "div[class*='alert-success']").text
print(successText)

#assert que una parte del texto sea igual a "Success! Thank you!"
assert "Success! Thank you!" in successText


time.sleep(2)
driver.close()
driver.quit()
