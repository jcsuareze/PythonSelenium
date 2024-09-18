from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, InvalidArgumentException, NoSuchElementException

tiempo = 10 #segundos
driver = webdriver.Chrome()

driver.get("https://demoqa.com/links")
driver.maximize_window()
#driver.execute_script("window.scrollBy(0, 300);")
wait = WebDriverWait(driver, 10)

#driver.execute_script("window.scrollBy(0, 300);")


try:
    links = driver.find_elements("tag name", "a")
    print("Cantidad de links en la página: ", len(links))
    for num in links:
        print(num.text)
        print(num.get_attribute("href"))
        print("----------------------------------------------------")
except NoSuchElementException as e:
    print("No se encontró el elemento, se lanza NoSuchElementException" + e.msg)

finally:
    print(driver.title)
    print("Fin de la prueba")
    driver.close()


