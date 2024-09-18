import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, InvalidArgumentException

tiempo = 10 #segundos
driver = webdriver.Chrome()

driver.get("https://pixabay.com/es/")
driver.maximize_window()
#driver.execute_script("window.scrollBy(0, 300);")
wait = WebDriverWait(driver, 10)

#driver.execute_script("window.scrollBy(0, 300);")


try:
    wait.until(EC.presence_of_element_located(("xpath", "//span[@class='label--Ngqjq' and text()='Descubre más']")))
    buscar = driver.find_element("xpath", "//span[@class='label--Ngqjq' and text()='Descubre más']")
    navegar = driver.execute_script("arguments[0].scrollIntoView();", buscar)

    time.sleep(6)

except TimeoutException as e:
    print("No se encontró el elemento, se lanza TimeoutException" + e.msg)



finally:
    print(driver.title)
    print("Fin de la prueba")
    driver.close()


