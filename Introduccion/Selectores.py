#Selectores en Selenium
from selenium import webdriver

#Los selectores son una parte fundamental de Selenium, ya que nos permiten interactuar con los elementos de una página web.

#Selenium nos permite seleccionar elementos de una página web utilizando diferentes selectores, como:

#Por I
#Por nombre

#Selectores CSS

#usando ID

driver = webdriver.Chrome()

driver.find_element_by_css_selector("#id")

#usando clase

driver.find_element_by_css_selector(".clase")

#usando atributo

driver.find_element_by_css_selector("[atributo='valor']")

#usando combinación de selectores

driver.find_element_by_css_selector("div#id.clase[atributo='valor']")


