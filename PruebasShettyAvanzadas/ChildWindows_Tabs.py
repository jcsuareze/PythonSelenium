import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")
driver.implicitly_wait(2)

# Click en el link "Click Here"
driver.find_element(By.LINK_TEXT, "Click Here").click()

# Cambiar de ventana
#Este metodo devuelve una lista con los identificadores de las ventanas abiertas
#donde el primer elemento de la lista es el identificador de la ventana padre tiene indice 0 y el segundo elemento es el identificador de la ventana hija tiene indice 1
#   ['91B75AB242FB792ert9F00BDAEC36D1F', '4E50E797064D9E3B8ffdE510713EA2AC']
ventanasAbiertas = driver.window_handles
print(ventanasAbiertas)

# Cambiar a la ventana hija
driver.switch_to.window(ventanasAbiertas[1])
print(driver.title)
print(driver.current_url)
print(driver.find_element(By.TAG_NAME, "h3").text)

#cerrar la ventana hija
driver.close()

# Cambiar a la ventana padre
driver.switch_to.window(ventanasAbiertas[0])
print(driver.find_element(By.TAG_NAME, "h3").text)

assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text


time.sleep(2)
driver.close()
driver.quit()
