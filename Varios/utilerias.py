from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def llamar_modal(driver):
    try:
        driver.find_element("id", "showSmallModal").click()
    except NoSuchElementException:
        #mostrar la excepcion ocurrida
        print("No se encontró el botón" + str(NoSuchElementException))
    driver.find_element("xpath", "//div[@class='modal-content']").click()
