import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://demoqa.com/text-box")
driver.maximize_window()

time.sleep(2)
driver.get("https://www.selenium.dev/es/documentation/webdriver/locating_elements/")
time.sleep(2)
driver.back()
#puede ser reemplazado el driver.back() por el siguiente comando
#driver.execute("window.history.go(-1)")

time.sleep(2)
driver.forward()
time.sleep(2)
driver.refresh()
time.sleep(2)


driver.close()
