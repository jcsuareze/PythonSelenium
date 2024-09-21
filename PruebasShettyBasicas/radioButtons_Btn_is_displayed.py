import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
radioButtons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")

print(len(radioButtons))

radioButtons[0].click()
radioButtons[2].click()

assert radioButtons[2].is_selected()

assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not  driver.find_element(By.ID, "displayed-text").is_displayed()


time.sleep(2)
driver.close()
driver.quit()


