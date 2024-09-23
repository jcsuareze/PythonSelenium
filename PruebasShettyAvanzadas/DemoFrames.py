import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(2)
driver.get("https://the-internet.herokuapp.com/iframe")
wait = WebDriverWait(driver, 10)
action = webdriver.ActionChains(driver)

equis = driver.find_element(By.CSS_SELECTOR, "button.tox-notification__dismiss")
action.move_to_element(equis).click().perform()


#El frame tiene un identificador unico que se puede utilizar para cambiar a el y trabajar con el contenido
# Se puede identificar el frame por su nombre, id, o por su indice en la pagina <iframe id="mce_0_ifr" > </iframe>

# Cambiar a un frame por su nombre
driver.switch_to.frame("mce_0_ifr")
time.sleep(2)

textBox = driver.find_element(By.ID, "tinymce")
textBox3 = driver.find_element(By.XPATH, "//body[@id='tinymce']")
wait.until(expected_conditions.visibility_of(textBox))
wait.until(expected_conditions.visibility_of(textBox3))

print(textBox.text)
print(textBox3.text)

#La pagina no funciona correctamente con el metodo clear() de la clase WebElement
#No permite interaciones con el elemento
#Pero si funciona cambiar de frame y enviar texto
textBox3.clear()
driver.find_element(By.ID, "tynymce").send_keys("Hola Mundo")




time.sleep(2)
driver.close()
driver.quit()
