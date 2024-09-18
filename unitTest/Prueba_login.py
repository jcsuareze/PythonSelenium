import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class Pueba_login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("https://saucedemo.com/")

    def test_login1(self):
        driver = self.driver
        user_name = driver.find_element ("xpath","//input[@id='user-name']")
        password = driver.find_element ("xpath","//input[@id='password']")
        btn_login = driver.find_element ("xpath","//input[@id='login-button']")
        user_name.send_keys("Juan Carlos")
        password.send_keys("123456")
        btn_login.click()
        error = driver.find_element("xpath","//h3[@data-test='error']")
        print(error.text)
        if error.text.strip() == "Epic sadface: Username and password do not match any user in this service":
            print("Los datos no son correctos")

    def test_login2(self):
        driver = self.driver
        user_name = driver.find_element ("xpath","//input[@id='user-name']")
        password = driver.find_element ("xpath","//input[@id='password']")
        btn_login = driver.find_element ("xpath","//input[@id='login-button']")
        user_name.send_keys("")
        password.send_keys("admin123")
        btn_login.click()
        error = driver.find_element("xpath","//h3[@data-test='error']")
        print(error.text)
        if error.text.strip() == "Epic sadface: Username is required":
            print("Los datos no son correctos")


    def tearDown(self):
        driver = self.driver
        driver.quit()


if __name__ == '__main__':
    unittest.main()
