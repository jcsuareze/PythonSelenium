import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice")

driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Hello")
driver.find_element(By.NAME, "email").send_keys("hello@somedomain.com.mx")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()

#Static dropdown,  cuando se ve un SELECT en el HTML es un dropdown estatico
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
time.sleep(2)
dropdown.select_by_index(0)








time.sleep(2)
driver.close()
driver.quit()


