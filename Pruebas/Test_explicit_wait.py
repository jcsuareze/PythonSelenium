import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from Varios.utilerias import llamar_modal
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://demoqa.com/modal-dialogs")
driver.maximize_window()
driver.execute_script("window.scrollBy(0, 300);")
try:
    llamar_modal(driver)
except NoSuchElementException as e:
    print("No se encontro el boton")
#Ejemplo util cuando aparecen modales o ventanas emergentes
modal = WebDriverWait(driver, 10).until(EC.presence_of_element_located(("xpath", "//div[@class='modal-body' and contains(text(),'This is a small modal')]")))
print(modal.is_enabled())

time.sleep(5)

print("Fin del test")
driver.close()