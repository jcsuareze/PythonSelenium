
from selenium import webdriver

tiempo = 10 #segundos
driver = webdriver.Chrome()

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
driver.implicitly_wait(tiempo)

nom = driver.find_element("id", "userName")
nom.send_keys("Juan Carlos")
driver.find_element("id", "userEmail").send_keys("loquesea@algunDominio.com")
driver.find_element("id", "currentAddress").send_keys("Calle 123")
driver.find_element("id", "permanentAddress").send_keys("Calle 456")

#ejecuta un script de javascript para hacer scroll down
driver.execute_script("window.scrollBy(0, 300);")

try:
    driver.find_element("id", "surbmit").click()

except:
    print("No se encontró el botón")






driver.close()
