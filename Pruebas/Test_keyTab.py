import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://demoqa.com/text-box")
#maximiza la ventana

driver.maximize_window()
time.sleep(2)


nom = driver.find_element("id", "userName")
nom.send_keys("Juan Carlos")
nom.send_keys(Keys.TAB+ "loquesea@someDomain.com" + Keys.TAB
              + "Calle 123" + Keys.TAB + "Calle 456" + Keys.TAB + Keys.ENTER)


#driver.find_element("id", "submit").click()

time.sleep(2)

driver.close()
