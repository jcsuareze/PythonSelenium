import unittest

from selenium import webdriver


class Base_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("https://demoqa.com/text-box")

    def test_search(self):
        driver = self.driver
        print(driver.title)
        if driver.title == "DEMOQfA":
            print("Correcto")
        else:
            print("Incorrecto")



    def tearDown(self):
        driver = self.driver
        driver.quit()


if __name__ == '__main__':
    unittest.main()
