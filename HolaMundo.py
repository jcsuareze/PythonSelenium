from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Instanciamos un objeto 'webdriver' de chrome
#driver = webdriver.Chrome()
driver = webdriver.Edge()


# Accedemos a la URL de la página
driver.get("https://demoqa.com/text-box")
print("Bienvenido a Selenium")

# Obtenemos el elemento de la página
print(driver.title)

# cerrar el navegador
driver.close()







