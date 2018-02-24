import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class  Verify_Share_Via_Social_Media(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        
        

    def test_Open_Website(self):

        # self.driver.maximize_window()
        driver = self.driver
        driver.get("https://app.mytommy.com/")
        

        driver.implicitly_wait(10)
        driver.find_element_by_name("username").send_keys("eagalleto@gmail.com")
        driver.implicitly_wait(5)
        driver.find_element_by_class_name("button-fill").click();

        assert "eagalleto@gmail.com" in driver.find_element_by_name("username").get_attribute("value")

        driver.implicitly_wait(5)
        driver.find_element_by_class_name("password").send_keys("Tommy123");
        driver.find_element_by_class_name("submit-login").click();
        self.assertTrue("Chats" in driver.find_element_by_class_name("chat-tab-link").get_attribute("innerText"))

        driver.find_element_by_id("main-menu-drag-handle").click();
        driver.find_element_by_xpath("//*[@id=\"main-menu-administration\"]/div[2]/ul/li[1]/a").click();
        driver.find_element_by_class_name("logout-button").click();

        self.assertEqual("Email address / Phone", driver.find_element_by_class_name("username").get_attribute("placeholder"))

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
