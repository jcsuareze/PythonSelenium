import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID, "autosuggest").send_keys("Ind")
time.sleep(2)
#Ya que los valores son dinamicos, el orden puede variar y no se puede hacer un click directo
# Seleccionar un CSS selector que tenga elementos coincidentes con el texto que se busca <li class=ui-menu-item>
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")

#imprime la cantidad de elementos que se encontraron
print(len(countries))

#iterar sobre los elementos encontrados
for country in countries: #Country es un WebElement
    print(type(country.text))
    if country.text == "India":
        print("Elemento encontrado")
        country.click()
        break

#Tratando de imprimir el texto del elemento seleccionado, pero al tratarlo se pierde el texto porque es dinamico
print("Texto perdido con .text "+ driver.find_element(By.ID, "autosuggest").text)


#Validar que el elemento seleccionado sea el correcto
#con get_attribute se obtiene el valor del atributo ya que el texto es dinamico y sera guardado en el atributo value
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"










time.sleep(2)
driver.close()
driver.quit()


