import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(2)
wait = WebDriverWait(driver, 10)

#ActionChais es una clase que nos permite realizar acciones con el raton como doble click, click derecho, arrastrar y soltar, etc.
action = webdriver.ActionChains(driver)
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()

#En este caso, el elemento que queremos seleccionar esta dentro de otro elemento, por lo que debemos hacer hover sobre el elemento padre
#para poder seleccionar el elemento hijo que queremos
childElement1 = driver.find_element(By.LINK_TEXT, "Top")
action.context_click(childElement1).perform()

childElement2 = driver.find_element(By.LINK_TEXT, "Reload")
action.move_to_element(childElement2).click().perform()




time.sleep(2)
driver.close()
driver.quit()
