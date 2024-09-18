from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://demoqa.com/")
driver.maximize_window()
driver.implicitly_wait(10)

print(driver.title)

titulo = driver.find_element("xpath", "//img[@src='/images/Toolsqa.jpg']")
btn = driver.find_element("xpath", "(//div[contains(@class,'card-up')])[1]")

if titulo.is_displayed():
    print("El titulo es visible")
    btn.click()

driver.close()

