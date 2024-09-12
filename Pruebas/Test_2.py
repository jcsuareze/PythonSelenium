import time

from selenium import webdriver


driver = webdriver.Chrome()

driver.get("https://demoqa.com/text-box")
#maximiza la ventana

driver.maximize_window()
time.sleep(2)


nom = driver.find_element("xpath", "//input[@id='userName']")
nom.send_keys("Juan Carlos")
driver.find_element("CSS", "//input[@id='userEmail' and @type='email']").send_keys("loquesea@algunDominio.com")
driver.find_element("xpath", "//textarea[@id='currentAddress' and @class='form-control']").send_keys("Calle 123")
driver.find_element("xpath", "//textarea[@id='permanentAddress' and @class='form-control']").send_keys("Calle 456")

#ejecuta un script de javascript para hacer scroll down
driver.execute_script("window.scrollBy(0, 300);")

time.sleep(2)

driver.find_element("xpath", "//button[@id='submit' and @class='btn btn-primary']").click()

time.sleep(2)

driver.close()
