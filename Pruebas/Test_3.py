import time

from selenium import webdriver


driver = webdriver.Chrome()

driver.get("https://demoqa.com/text-box")
#maximiza la ventana

driver.maximize_window()
time.sleep(2)


nom = driver.find_element("css selector", "input#userName.mr-sm-2.form-control")
nom.send_keys("Juan Carlos")
driver.find_element("css selector", "input#userEmail.mr-sm-2.form-control").send_keys("loquesea@algunDominio.com")
driver.find_element("css selector", "textarea#currentAddress.form-control").send_keys("Calle 123")
driver.find_element("css selector", "textarea#permanentAddress.form-control").send_keys("Calle 456")

#ejecuta un script de javascript para hacer scroll down
driver.execute_script("window.scrollBy(0, 300);")

time.sleep(2)

driver.find_element("css selector", "button#submit.btn.btn-primary").click()

time.sleep(2)

driver.close()
