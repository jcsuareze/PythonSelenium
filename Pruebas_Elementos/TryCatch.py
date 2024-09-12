import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

tiempo = 10 #segundos
driver = webdriver.Chrome()

driver.get("https://demoqa.com/select-menu")
driver.maximize_window()
driver.implicitly_wait(tiempo)
driver.execute_script("window.scrollBy(0, 300);")

wait = WebDriverWait(driver, 10)

try:
    print("entra a try, espera 10 segundos para encontrar el webElement")
    select = Select(wait.until(EC.presence_of_element_located(("xpath", "//select[@id='oldSelectMenu']"))))
    select.select_by_visible_text("Yellow")
    select.select_by_index(4)
    select.select_by_value("10")
    time.sleep(5)
except TimeoutException as e:
    print("No se encontró el elemento, se lanza TimeoutException" + e.msg)
finally:
    print("Fin de la prueba")
    driver.close()

