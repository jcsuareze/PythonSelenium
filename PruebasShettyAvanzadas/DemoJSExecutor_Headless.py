import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

#Para ignorar los errores de certificado
chrome_options.add_argument("--ignore-certificate-errors")


#Al ejecutar el navegador en modo headless, no se puede realizar scroll en la pagina
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(2)

#Esta clase nos permite ejecutar codigo javascript en el navegador.  Esto es util cuando no se puede interactuar con un elemento de la pagina
#Esta en particular nos permite hacer scroll en la pagina hasta el final
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


driver.get_screenshot_as_file("screen.png")



#Este metodo nos permite obtener el texto de la pagina
#En este caso se obtiene el texto de la pagina y se imprime en la consola
print(driver.execute_script("return document.documentElement.innerText;"))



time.sleep(2)
driver.close()
driver.quit()
