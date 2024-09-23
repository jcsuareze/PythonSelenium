import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.implicitly_wait(2)

browserSortedVeggies = []

#click en el boton header de la tabla
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

#Recolectar todos los elementos de la tabla
veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")

for ele in veggieWebElements:
    browserSortedVeggies.append(ele.text)

original = browserSortedVeggies.copy()
browserSortedVeggies.sort()
assert browserSortedVeggies == original


time.sleep(2)
driver.close()
driver.quit()
