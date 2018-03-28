import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
import random
import uuid
from Keywords import *

class TommyTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://app.mytommy.com/")

    def test_1LoginAndLogout(self):

        driver = self.driver

        #For Login
        WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.ID, SelectorId_LoginUserName)))
        driver.find_element_by_name(SelectorName_Username).send_keys(Email_Add)
        driver.find_element_by_class_name(SelectorClass_NextButton).click()

        self.assertEqual(Email_Add, driver.find_element_by_name(SelectorName_Username).get_attribute("value"))

        WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_SubmitButton)))
        driver.find_element_by_class_name(SelectorClass_LoginPassword).send_keys(Password)
        driver.find_element_by_class_name(SelectorClass_SubmitButton).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_ChatIcon)))
        
        self.assertEqual("Chats", driver.find_element_by_class_name(SelectorClass_ChatTitle).get_attribute("innerText"))

        #For Logout
        driver.find_element_by_id(SelectorId_SidebarExpand).click()
        WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, SelectorClass_SideBarChatIcon), "Chats"))
        (driver.find_element_by_id(SelectorId_AdministrationMenu).find_elements_by_tag_name("img"))[0].click()
        WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, SelectorClass_SaveButton), "Save"))
        WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, SelectorClass_LogoutButton), "Logout"))
        driver.find_element_by_class_name(SelectorClass_LogoutButton).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_NextButton)))
        
        self.assertEqual("Email address / Phone", driver.find_element_by_class_name(SelectorName_Username).get_attribute("placeholder"))

    def tearDown(self):
        self.driver.close()



    # def test_2Contacts_NewChat(self):
        
    #     driver = self.driver

    #     WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.ID, SelectorId_LoginUserName)))
    #     driver.find_element_by_name(SelectorName_Username).send_keys(Email_Add)
    #     driver.find_element_by_class_name(SelectorClass_NextButton).click()
    #     WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_SubmitButton)))
    #     driver.find_element_by_class_name(SelectorClass_LoginPassword).send_keys(Password)
    #     driver.find_element_by_class_name(SelectorClass_SubmitButton).click()
    #     WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_ChatIcon)))
    #     driver.find_element_by_class_name(SelectorClass_AddNewMenu).click()
    #     WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_ModalContacts)))
    #     (driver.find_element_by_class_name(SelectorClass_AddNewMenu_NewChat).find_elements_by_tag_name("img"))[0].click()
    #     WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_OverLay)))
    #     (driver.find_element_by_class_name(SelectorClass_AddNewMenu_NewChatCheckBox).find_elements_by_tag_name("div"))[0].click()
    #     WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_CheckBox)))
    #     driver.find_element_by_class_name(SelectorClass_AddNewMenu_NewChatOkButton).click()
    #     WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID, SelectorId_AddNewMenu_TextBox)))
    #     driver.find_element_by_id(SelectorId_AddNewMenu_TextBox).send_keys("This is a test text")
    #     (driver.find_element_by_class_name(SelectorClass_AddNewMenu_TextBoxSendBUtton).find_elements_by_tag_name("a"))[0].click()
    #     WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, SelectorClass_InputtedText), "This is a test text"))
      
    #     # Need to delete always the text
    #     self.assertEqual("This is a test text", driver.find_element_by_class_name(SelectorClass_AssertInputtedText).find_elements_by_tag_name("div")[1].get_attribute("innerText"))


    # def tearDown(self):
    #     self.driver.close()




    # def test_3Contacts_AddContacts_SMS(self):
        
    #     driver = self.driver
    #     driver.get("https://app.mytommy.com/")

    #     try:
    #         WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.ID, "login_username")))
    #     finally:

    #         driver.find_element_by_name("username").send_keys("eagalleto@gmail.com")
    #         driver.find_element_by_class_name("button-fill").click()

    #         self.assertTrue("eagalleto@gmail.com" in driver.find_element_by_name("username").get_attribute("value"))

    #     try:
    #         WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "submit-login")))
    #     finally:
    #         driver.find_element_by_class_name("password").send_keys("Tommy123")
    #         driver.find_element_by_class_name("submit-login").click()
    #     try:
    #         WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "icon-chat")))
    #     finally:
    #         self.assertTrue("Chats" in driver.find_element_by_class_name("chat-tab-link").get_attribute("innerText"))

    #         driver.find_element_by_id("main-menu-drag-handle").click()
        
    #     try:

    #         WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, "menu-label"), "Chats"))

    #     finally:

    #         driver.find_element_by_class_name("menu-link").click()



    #     try:

    #         WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, "sliding"), "Chats"))
    #         time.sleep(2)
    #     finally:

    #         driver.find_element_by_class_name("open-popover").click()
    #         time.sleep(2)
    #         (driver.find_element_by_class_name("popover-inner").find_elements_by_tag_name("img"))[1].click()
    #         time.sleep(2)
    #         driver.find_element_by_id("invite").click()
    #         time.sleep(2)
    #         (driver.find_element_by_class_name("actions-modal-group").find_elements_by_tag_name("div"))[0].click()
    #         time.sleep(2)
    #         driver.find_element_by_name("first_name").send_keys("test")
    #         time.sleep(2)
    #         driver.find_element_by_name("mobile").send_keys("+63" + '{:09}'.format(random.randrange(1, 10**3)))
    #         time.sleep(2)
    #         (driver.find_element_by_class_name("modal-buttons-2").find_elements_by_tag_name("span"))[1].click()
    #         time.sleep(2)
    #         # Confirmation not correct
    #         self.assertEqual("Tommy", driver.find_element_by_class_name("modal-inner").find_elements_by_tag_name("div")[0].get_attribute("innerText"))


    # def tearDown(self):
    #     self.driver.close()



    # def test_4Contacts_AddContacts_Email(self):
        
    #     driver = self.driver
    #     driver.get("https://app.mytommy.com/")

    #     try:
    #         WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.ID, "login_username")))
    #     finally:

    #         driver.find_element_by_name("username").send_keys("eagalleto@gmail.com")
    #         driver.find_element_by_class_name("button-fill").click()

    #         self.assertTrue("eagalleto@gmail.com" in driver.find_element_by_name("username").get_attribute("value"))

    #     try:
    #         WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "submit-login")))
    #     finally:
    #         driver.find_element_by_class_name("password").send_keys("Tommy123")
    #         driver.find_element_by_class_name("submit-login").click()
    #     try:
    #         WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "icon-chat")))
    #     finally:
    #         self.assertTrue("Chats" in driver.find_element_by_class_name("chat-tab-link").get_attribute("innerText"))

    #         driver.find_element_by_id("main-menu-drag-handle").click()
        
    #     try:
    #         time.sleep(1)

    #         WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, "menu-label"), "Chats"))

    #     finally:
    #         driver.find_element_by_class_name("menu-link").click()



    #     try:

    #         WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, "sliding"), "Chats"))
    #         time.sleep(2)
    #     finally:

    #         driver.find_element_by_class_name("open-popover").click()
    #         time.sleep(2)
    #         (driver.find_element_by_class_name("popover-inner").find_elements_by_tag_name("img"))[1].click()
    #         time.sleep(2)
    #         driver.find_element_by_id("invite").click()
    #         time.sleep(2)
    #         (driver.find_element_by_class_name("actions-modal-group").find_elements_by_tag_name("div"))[1].click()
    #         time.sleep(2)
    #         driver.find_element_by_name("first_name").send_keys("test")
    #         time.sleep(2)
    #         driver.find_element_by_name("email").send_keys('{:09}'.format(random.randrange(1, 10**3)) + "@gmail.com")
    #         time.sleep(2)
    #         (driver.find_element_by_class_name("modal-buttons-2").find_elements_by_tag_name("span"))[1].click()
    #         time.sleep(2)
    #         # No Confirmation so it is wrong
    #         self.assertFalse("Tommy" in driver.find_element_by_class_name("modal-inner").find_elements_by_tag_name("div")[0].get_attribute("innerText"))


    # def tearDown(self):
    #     self.driver.close()



    # def test_5Contacts_AddContacts_InvitationLink(self):
        
    #     driver = self.driver
    #     driver.get("https://app.mytommy.com/")

    #     try:
    #         WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.ID, "login_username")))
    #     finally:

    #         driver.find_element_by_name("username").send_keys("eagalleto@gmail.com")
    #         driver.find_element_by_class_name("button-fill").click()

    #         self.assertTrue("eagalleto@gmail.com" in driver.find_element_by_name("username").get_attribute("value"))

    #     try:
    #         WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "submit-login")))
    #     finally:
    #         driver.find_element_by_class_name("password").send_keys("Tommy123")
    #         driver.find_element_by_class_name("submit-login").click()
    #     try:
    #         WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "icon-chat")))
    #     finally:
    #         self.assertTrue("Chats" in driver.find_element_by_class_name("chat-tab-link").get_attribute("innerText"))

    #         driver.find_element_by_id("main-menu-drag-handle").click()
        
    #     try:
    #         time.sleep(1)

    #         WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, "menu-label"), "Chats"))

    #     finally:
    #         driver.find_element_by_class_name("menu-link").click()



    #     try:

    #         WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, "sliding"), "Chats"))
    #         time.sleep(2)
    #     finally:

    #         driver.find_element_by_class_name("open-popover").click()
    #         time.sleep(2)
    #         (driver.find_element_by_class_name("popover-inner").find_elements_by_tag_name("img"))[1].click()
    #         time.sleep(2)
    #         driver.find_element_by_id("invite").click()
    #         time.sleep(2)
    #         (driver.find_element_by_class_name("actions-modal-group").find_elements_by_tag_name("div"))[2].click()
    #         time.sleep(2)
    #         driver.get(driver.find_element_by_name("invitation_link").get_attribute("value"))
    #         time.sleep(2)
    #         self.assertTrue("Welcome to Tommy!" in driver.page_source)


    # def tearDown(self):
    #     self.driver.close()




    # def test_6AddTeam(self):
        
    #     driver = self.driver
    #     driver.get("https://app.mytommy.com/")

    #     try:
    #         WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.ID, "login_username")))
    #     finally:

    #         driver.find_element_by_name("username").send_keys("eagalleto@gmail.com")
    #         driver.find_element_by_class_name("button-fill").click()

    #         self.assertTrue("eagalleto@gmail.com" in driver.find_element_by_name("username").get_attribute("value"))

    #     try:
    #         WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "submit-login")))
    #     finally:
    #         driver.find_element_by_class_name("password").send_keys("Tommy123")
    #         driver.find_element_by_class_name("submit-login").click()
    #     try:
    #         WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "icon-chat")))
    #     finally:
    #         self.assertTrue("Chats" in driver.find_element_by_class_name("chat-tab-link").get_attribute("innerText"))

    #         driver.find_element_by_id("main-menu-drag-handle").click()
        
    #     try:
    #         time.sleep(1)

    #         WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, "menu-label"), "Chats"))

    #     finally:
    #         time.sleep(2)

    #         (driver.find_element_by_class_name("menu-block").find_elements_by_tag_name("a"))[2].click()
    #         time.sleep(2)
            
    #         driver.find_element_by_name("name").send_keys(str(uuid.uuid1()))
    #         driver.find_element_by_name("email").send_keys(str(uuid.uuid1())+"@gmail.com")
    #         driver.find_element_by_name("phone").send_keys("+63" +'{:09}'.format(random.randrange(1, 10**2)))
    #         driver.find_element_by_class_name("button-fill").click()
    #         time.sleep(2)

    #         self.assertEqual("Your team account has been created!", (driver.find_element_by_class_name("notification-item").find_elements_by_tag_name("div"))[5].get_attribute("innerText"))


    # def tearDown(self):
    #     self.driver.close()



    # def test_7About_InviteAFriend(self):
        
    #     driver = self.driver
    #     driver.get("https://app.mytommy.com/")

    #     try:
    #         WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.ID, "login_username")))
    #     finally:

    #         driver.find_element_by_name("username").send_keys("eagalleto@gmail.com")
    #         driver.find_element_by_class_name("button-fill").click()

    #         self.assertTrue("eagalleto@gmail.com" in driver.find_element_by_name("username").get_attribute("value"))

    #     try:
    #         WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "submit-login")))
    #     finally:
    #         driver.find_element_by_class_name("password").send_keys("Tommy123")
    #         driver.find_element_by_class_name("submit-login").click()
    #     try:
    #         WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "icon-chat")))
    #     finally:
    #         self.assertTrue("Chats" in driver.find_element_by_class_name("chat-tab-link").get_attribute("innerText"))

    #         driver.find_element_by_id("main-menu-drag-handle").click()
        
    #     try:
    #         time.sleep(1)

    #         WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, "menu-label"), "Chats"))

    #     finally:
    #         time.sleep(2)

    #         (driver.find_element_by_class_name("menu-block").find_elements_by_tag_name("a"))[1].click()
    #         time.sleep(2)
    #         (driver.find_element_by_id("about-page").find_elements_by_tag_name("a"))[0].click()
    #         # (driver.find_element_by_class_name("list-block").find_elements_by_tag_name("li"))[1.click()
    #         time.sleep(2)

    #         (driver.find_element_by_class_name("actions-modal-group").find_elements_by_tag_name("div"))[0].click()
    #         time.sleep(2)
    #         driver.find_element_by_name("first_name").send_keys("test")
    #         time.sleep(2)
    #         driver.find_element_by_name("mobile").send_keys("+63" + '{:09}'.format(random.randrange(1, 10**3)))
    #         time.sleep(2)
    #         (driver.find_element_by_class_name("modal-buttons-2").find_elements_by_tag_name("span"))[1].click()
    #         time.sleep(2)
    #         # Confirmation not correct
    #         self.assertEqual("Tommy", driver.find_element_by_class_name("modal-inner").find_elements_by_tag_name("div")[0].get_attribute("innerText"))

    # def tearDown(self):
    #     self.driver.close()

    # def test_8About_Feedback(self):
        
    #     driver = self.driver
    #     driver.get("https://app.mytommy.com/")

    #     try:
    #         WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.ID, "login_username")))
    #     finally:

    #         driver.find_element_by_name("username").send_keys("eagalleto@gmail.com")
    #         driver.find_element_by_class_name("button-fill").click()

    #         self.assertTrue("eagalleto@gmail.com" in driver.find_element_by_name("username").get_attribute("value"))

    #     try:
    #         WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "submit-login")))
    #     finally:
    #         driver.find_element_by_class_name("password").send_keys("Tommy123")
    #         driver.find_element_by_class_name("submit-login").click()
    #     try:
    #         WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "icon-chat")))
    #     finally:
    #         self.assertTrue("Chats" in driver.find_element_by_class_name("chat-tab-link").get_attribute("innerText"))

    #         driver.find_element_by_id("main-menu-drag-handle").click()
        
    #     try:
    #         time.sleep(1)

    #         WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, "menu-label"), "Chats"))

    #     finally:
    #         time.sleep(2)

    #         (driver.find_element_by_class_name("menu-block").find_elements_by_tag_name("a"))[1].click()
    #         time.sleep(2)
    #         (driver.find_element_by_id("about-page").find_elements_by_tag_name("a"))[1].click()
    #         time.sleep(2)

    #         self.assertEqual("Feedback", driver.find_element_by_id("about-external").find_elements_by_tag_name("p")[0].get_attribute("innerText"))

    # def tearDown(self):
    #     self.driver.close()


    # def test_9About_Acknowledgements(self):
        
    #     driver = self.driver
    #     driver.get("https://app.mytommy.com/")

    #     try:
    #         WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.ID, "login_username")))
    #     finally:

    #         driver.find_element_by_name("username").send_keys("eagalleto@gmail.com")
    #         driver.find_element_by_class_name("button-fill").click()

    #         self.assertTrue("eagalleto@gmail.com" in driver.find_element_by_name("username").get_attribute("value"))

    #     try:
    #         WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "submit-login")))
    #     finally:
    #         driver.find_element_by_class_name("password").send_keys("Tommy123")
    #         driver.find_element_by_class_name("submit-login").click()
    #     try:
    #         WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "icon-chat")))
    #     finally:
    #         self.assertTrue("Chats" in driver.find_element_by_class_name("chat-tab-link").get_attribute("innerText"))

    #         driver.find_element_by_id("main-menu-drag-handle").click()
        
    #     try:
    #         time.sleep(1)

    #         WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, "menu-label"), "Chats"))

    #     finally:
    #         time.sleep(2)

    #         (driver.find_element_by_class_name("menu-block").find_elements_by_tag_name("a"))[1].click()
    #         time.sleep(2)
    #         (driver.find_element_by_id("about-page").find_elements_by_tag_name("a"))[2].click()
    #         time.sleep(2)

    #         self.assertEqual("Acknowledgements", driver.find_element_by_id("about-external").find_elements_by_tag_name("p")[0].get_attribute("innerText"))

    # def tearDown(self):
    #     self.driver.close()

    # def test_9About_Account(self):
        
    #     driver = self.driver
    #     driver.get("https://app.mytommy.com/")

    #     try:
    #         WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.ID, "login_username")))
    #     finally:

    #         driver.find_element_by_name("username").send_keys("eagalleto@gmail.com")
    #         driver.find_element_by_class_name("button-fill").click()

    #         self.assertTrue("eagalleto@gmail.com" in driver.find_element_by_name("username").get_attribute("value"))

    #     try:
    #         WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "submit-login")))
    #     finally:
    #         driver.find_element_by_class_name("password").send_keys("Tommy123")
    #         driver.find_element_by_class_name("submit-login").click()
    #     try:
    #         WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "icon-chat")))
    #     finally:
    #         self.assertTrue("Chats" in driver.find_element_by_class_name("chat-tab-link").get_attribute("innerText"))

    #         driver.find_element_by_id("main-menu-drag-handle").click()
        
    #     try:
    #         time.sleep(1)

    #         WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, "menu-label"), "Chats"))

    #     finally:
    #         time.sleep(2)

    #         (driver.find_element_by_class_name("menu-block").find_elements_by_tag_name("a"))[0].click()
    #         time.sleep(3)

    #         details = ("Emman",       "Galleto",   "2018-03-13<","eagalleto@gmail.com", "+6391233026697")

    #         selector = ("first_name", "last_name", "dob",         "email",               "mobile")

    #         self.assertEqual(details[0], driver.find_element_by_name(selector[0]).get_attribute("value"))
    #         self.assertEqual(details[1], driver.find_element_by_name(selector[1]).get_attribute("value"))
    #         # self.assertEqual(details[2], driver.find_element_by_name(selector[2]).get_attribute("value"))
    #         # self.assertEqual(details[3], driver.find_element_by_name(selector[3]).get_attribute("value"))
    #         self.assertEqual(details[4], driver.find_element_by_name(selector[4]).get_attribute("value"))


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
