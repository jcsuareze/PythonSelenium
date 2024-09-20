import time

from selenium import webdriver
#Chrome driver service, sirve para no descargar

#en caso de existir un error con Chrome,  se puede descargar el chromedriver y pasarlo como argumento dentro de Chrome()

#driver es responsable de ejecutar las acciones en el navegador
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice")
driver.maximize_window()
print(driver.title)
print(driver.current_url)



time.sleep(2)
