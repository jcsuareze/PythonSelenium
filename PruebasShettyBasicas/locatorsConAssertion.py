import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/angularpractice")

driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Hello")
driver.find_element(By.NAME, "email").send_keys("hello@somedomain.com.mx")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()

# //tagname[@attribute = 'value'] -> Xpath Syntax for locating elements
# //input[@name='name'] -> Xpath Syntax for locating elements

message = driver.find_element(By.CLASS_NAME, "alert.alert-success.alert-dismissible").text # get the text of the element

print(message)

assert "success" in message
#assert message with an error message

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("_hola de nuevo")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()


time.sleep(2)
driver.close()
driver.quit()

