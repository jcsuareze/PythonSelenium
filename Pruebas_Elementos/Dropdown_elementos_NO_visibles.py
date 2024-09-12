import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

tiempo = 10 #segundos
driver = webdriver.Chrome()

driver.get("https://demoqa.com/select-menu")
driver.maximize_window()
driver.implicitly_wait(tiempo)


driver.execute_script("window.scrollBy(0, 300);")

#Seleccionar una opcion de un comboBox
dropdown = driver.find_element("xpath", "//div[@id='selectOne']")
dropdown.click()
wait = WebDriverWait(driver, tiempo)

#Esperar a que se carguen las opciones visibles

opciones = wait.until(EC.presence_of_all_elements_located(("xpath", "//div[@id='selectOne']//div[contains(@class, 'css-26l3qy-menu')]//div[starts-with(@id, 'react-select-3-opti')]")))
print(f"Se encontraron {len(opciones)} opciones")
for opcion in opciones:
    texto_opcion = opcion.text.strip().lower()
    print(f"Opción encontrada: {texto_opcion}")
    if wait.until(EC.element_to_be_clickable(opcion)):
        print("Es clickable :" + texto_opcion)
        break

time.sleep(5)


driver.close()




