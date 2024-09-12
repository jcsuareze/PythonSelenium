import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

tiempo = 10 #segundos
driver = webdriver.Chrome()

driver.get("https://demoqa.com/select-menu")
driver.maximize_window()
driver.implicitly_wait(tiempo)


driver.execute_script("window.scrollBy(0, 300);")

#Seleccionar una opcion de un comboBox
opciones = driver.find_element("xpath", "//select[@id='oldSelectMenu']")
#seleccionar por texto visible
select = Select(opciones)

select.select_by_visible_text("Yellow")

time.sleep(2)

select.select_by_index(4)

time.sleep(2)

select.select_by_value("10")

time.sleep(2)

driver.close()




