import time
from selenium import webdriver
from selenium.webdriver.common.by import By

name = "Juan Carlos"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")


driver.find_element(By.ID, "name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()

alert = driver.switch_to.alert # Cambiar el foco al alert
print(alert.text)

assert name in alert.text # Verificar que el texto que se envio al alert sea el mismo que se muestra en el alert

time.sleep(2)
alert.accept() # Aceptar el alert cuando se muestra unicamente un boton de aceptar/OK

# Para aceptar el alert con un boton de cancelar
# alert.dismiss()






time.sleep(4)
driver.close() # No se puede cerrar el alert con driver.close()
driver.quit()

