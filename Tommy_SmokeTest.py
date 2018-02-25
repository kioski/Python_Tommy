import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TommyTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login_logout(self):

        # self.driver.maximize_window()
        driver = self.driver
        driver.get("https://app.mytommy.com/")

        try:
            WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.ID, "login_username")))
        finally:

            driver.find_element_by_name("username").send_keys("eagalleto@gmail.com")
            driver.find_element_by_class_name("button-fill").click()

            self.assertTrue("eagalleto@gmail.com" in driver.find_element_by_name("username").get_attribute("value"))

        try:
            WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "submit-login")))
        finally:
            driver.find_element_by_class_name("password").send_keys("Tommy123")
            driver.find_element_by_class_name("submit-login").click()
        try:
            WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "icon-chat")))
        finally:
            self.assertTrue("Chats" in driver.find_element_by_class_name("chat-tab-link").get_attribute("innerText"))

            driver.find_element_by_id("main-menu-drag-handle").click()

        try:

            WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, "menu-label"), "Chats"))

        finally:

            (driver.find_element_by_id("main-menu-administration").find_elements_by_tag_name("img"))[0].click()


        try:
            WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "logout-button")))
        finally:

            driver.find_element_by_class_name("logout-button").click()

            self.assertEqual("Email address / Phone", driver.find_element_by_class_name("username").get_attribute("placeholder"))

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
