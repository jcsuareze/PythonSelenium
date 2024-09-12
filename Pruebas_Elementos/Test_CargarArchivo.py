import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, InvalidArgumentException

tiempo = 10 #segundos
driver = webdriver.Chrome()

driver.get("https://testpages.herokuapp.com/styled/file-upload-test.html")
driver.maximize_window()
#driver.execute_script("window.scrollBy(0, 300);")
wait = WebDriverWait(driver, 10)

try:
    wait.until(EC.presence_of_element_located(("css selector", "input#fileinput[name='filename']")))
    btnBuscar = driver.find_element("css selector", "input#fileinput[name='filename']")
    #btnBuscar.click()
    btnBuscar.send_keys("C:\\Carpeta practicas\\PracticaBasicaPython\\PythonSelenium\\Imagenes\\fpepsi.jpg")
    btnUpload = driver.find_element("xpath", "//input[@type='submit' and @name='upload']")
    btnUpload.click()

except TimeoutException as e:
    print("No se encontró el elemento, se lanza TimeoutException" + e.msg)
except InvalidArgumentException as e:
    print("Error en los argumentos: " + e.msg)


finally:
    print(driver.title)
    print("Fin de la prueba")
    driver.close()


