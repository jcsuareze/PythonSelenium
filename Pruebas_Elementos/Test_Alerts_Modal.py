import time
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://demoqa.com/modal-dialogs")
driver.maximize_window()
driver.execute_script("window.scrollBy(0, 300);")
driver.implicitly_wait(10)


try:
    modal = driver.find_element("xpath", "//button[@id='showSmallModal' and contains(text(),'Small modal')]")
    print(modal.is_enabled())
    modal.click()
    presence = WebDriverWait(driver, 10).until(EC.presence_of_element_located(("xpath", "//div[@class='modal-body' and contains(text(),'This is a small modal')]")))
    print(presence.is_enabled())
    closeButton = driver.find_element("xpath", "//button[@id='closeSmallModal']")
    closeButton.click()
    time.sleep(5)
except NoSuchElementException as e:
    print("No se encontró el botón para activar el modal" + e.msg)
except TimeoutException as e:
    print("No se encontró el modal" + e.msg)
finally:
    print("Fin del test")
    driver.close()