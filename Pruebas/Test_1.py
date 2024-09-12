import time

from selenium import webdriver


driver = webdriver.Chrome()

driver.get("https://demoqa.com/text-box")
#maximiza la ventana

driver.maximize_window()
time.sleep(2)


nom = driver.find_element("id", "userName")
nom.send_keys("Juan Carlos")
driver.find_element("id", "userEmail").send_keys("loquesea@algunDominio.com")
driver.find_element("id", "currentAddress").send_keys("Calle 123")
driver.find_element("id", "permanentAddress").send_keys("Calle 456")

#ejecuta un script de javascript para hacer scroll down
driver.execute_script("window.scrollBy(0, 300);")

time.sleep(2)

driver.find_element("id", "submit").click()





time.sleep(2)



driver.close()

#ejemplos de find_element
#nom = driver.find_element_by_id("userName")
#nom = driver.find_element_by_name("userName")
#nom = driver.find_element_by_class_name("mr-sm-2")
#nom = driver.find_element_by_tag_name("input")
#nom = driver.find_element_by_link_text("GitHub")
#nom = driver.find_element_by_partial_link_text("GitHub")
#nom = driver.find_element_by_css_selector("#userName")
