import time

from selenium import webdriver

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

tiempo = 10 #segundos
driver = webdriver.Chrome()

driver.get("https://demoqa.com/checkbox")
driver.maximize_window()
driver.implicitly_wait(tiempo)

btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("css selector", "span.rct-checkbox")))
btn.click()

driver.execute_script("window.scrollBy(0, 300);")
time.sleep(2)


driver.close()
