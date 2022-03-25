from selenium import webdriver
import time
import unittest
from Pages.login import LoginPage

from Pages.homepage import HomePage

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
class LoginTest(unittest.TestCase):
    @classmethod



    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        # cls.driver.get("https://demoqa.com/alerts")
        cls.driver.maximize_window()

        # cls.driver = webdriver.Chrome()
        # cls.driver.implicitly_wait(10)
        # cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        time.sleep(3)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()
        time.sleep(3)
        homepage = HomePage(driver)
        time.sleep(3)
        homepage.click_welcome()
        time.sleep(3)
        homepage.click_logout()
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")


