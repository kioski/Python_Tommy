import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time, random, string, uuid
from Keywords import *
from Credentials import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

class TommyTests(unittest.TestCase):


    def setUp(self):

        # self.driver = webdriver.Remote(command_executor,desired_capabilities_ios)
        # self.driver = webdriver.Remote(command_executor,desired_capabilities_android)


        mobileEmulation = { "deviceName": "Galaxy S5" }
        options = webdriver.ChromeOptions()
        options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(executable_path='D:\webdriver\chromedriver', chrome_options=options)

        # self.driver = webdriver.Chrome(executable_path='D:\webdriver\chromedriver') # <-- If you want browser only

        self.driver.get("https://app.mytommy.com/")


    def test_1aLoginAndLogout(self):

        driver = self.driver

        #For Login
        WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located((By.ID, SelectorId_LoginUserName)))
        time.sleep(5)
        driver.find_element_by_name(SelectorName_Username).send_keys(Email_Add)
        driver.find_element_by_class_name(SelectorClass_NextButton).click()
        WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_SubmitButton)))
        time.sleep(1)
        driver.find_element_by_class_name(SelectorClass_LoginPassword).send_keys(Password)
        driver.find_element_by_class_name(SelectorClass_SubmitButton).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_ChatIcon)))
        
        #For Logout
        driver.find_element_by_id(SelectorId_SidebarExpand).click()
        WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, SelectorClass_Administrator), "Administration"))
        (driver.find_element_by_id(SelectorId_AdministrationMenu).find_elements_by_tag_name("img"))[0].click()
        WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, SelectorClass_LogoutButton),"Logout"))
        time.sleep(1)
        driver.find_element_by_class_name(SelectorClass_LogoutButton).click()
        time.sleep(1)
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_NextButton)))

        if self.assertEqual("Email address / Phone", driver.find_element_by_class_name(SelectorName_Username).get_attribute("placeholder")) is True:
            False


    def tearDown(self):
        self.driver.quit()



    def test_1bContacts_NewChat(self):
        
        driver = self.driver

        WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located((By.ID, SelectorId_LoginUserName)))
        time.sleep(5)
        driver.find_element_by_name(SelectorName_Username).send_keys(Email_Add)
        driver.find_element_by_class_name(SelectorClass_NextButton).click()
        WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_SubmitButton)))
        time.sleep(1)
        driver.find_element_by_class_name(SelectorClass_LoginPassword).send_keys(Password)
        driver.find_element_by_class_name(SelectorClass_SubmitButton).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_ChatIcon)))
        time.sleep(5)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, SelectorClass_AddNewMenu)))
        driver.find_element_by_class_name(SelectorClass_AddNewMenu).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, SelectorClass_AddNewMenu)))
        time.sleep(2)
        (driver.find_element_by_class_name(SelectorClass_AddNewMenu_NewChat).find_elements_by_tag_name("img"))[0].click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_OverLay)))
        time.sleep(2)
        (driver.find_element_by_class_name(SelectorClass_AddNewMenu_NewChatCheckBox).find_elements_by_tag_name("div"))[0].click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_CheckBox)))
        driver.find_element_by_class_name(SelectorClass_AddNewMenu_NewChatOkButton).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID, SelectorId_AddNewMenu_TextBox)))
        Sample_Text = str(uuid.uuid1())[:8] + str(uuid.uuid1())[2:6]
        time.sleep(1)
        driver.find_element_by_id(SelectorId_AddNewMenu_TextBox).send_keys(Sample_Text)
        (driver.find_element_by_class_name(SelectorClass_AddNewMenu_TextBoxSendBUtton).find_elements_by_tag_name("a"))[0].click()
        time.sleep(2)
      
        if self.assertTrue(Sample_Text in driver.page_source) is True:
            False




    def tearDown(self):
        self.driver.quit()





    def test_1eContacts_AddContacts_InvitationLink(self):
        
        driver = self.driver

        WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located((By.ID, SelectorId_LoginUserName)))
        time.sleep(5)
        driver.find_element_by_name(SelectorName_Username).send_keys(Email_Add)
        driver.find_element_by_class_name(SelectorClass_NextButton).click()
        WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_SubmitButton)))
        time.sleep(1)
        driver.find_element_by_class_name(SelectorClass_LoginPassword).send_keys(Password)
        driver.find_element_by_class_name(SelectorClass_SubmitButton).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_ChatIcon)))
        time.sleep(5)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, SelectorClass_AddNewMenu)))
        driver.find_element_by_class_name(SelectorClass_AddNewMenu).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, SelectorClass_AddNewMenu)))
        time.sleep(5)
        (driver.find_element_by_class_name(SelectorClass_AddNewMenu_NewChat).find_elements_by_tag_name("a"))[1].click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID, SelectorId_AddNewMenu_Invite)))
        time.sleep(3)
        driver.find_element_by_id(SelectorId_AddNewMenu_Invite).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_AddNewMenu_Overlay)))
        time.sleep(1)
        (driver.find_element_by_class_name(SelectorClass_AddNewMenu_InviteSMS).find_elements_by_tag_name("div"))[1].click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_AddNewMenu_OverlayInvite)))
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_AddNewMenu_InviteSMS_DialogBoxTitle)))
        WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, SelectorClass_AddNewMenu_InviteSMS_DialogBoxTitle), "Invitation Link"))
        driver.get(driver.find_element_by_name(SelectorName_AddNewMenu_InviteEmail_Link).get_attribute("value"))

        if self.assertTrue("Welcome to Tommy!" in driver.page_source) is True:
            False


    def tearDown(self):
        self.driver.quit()




    def test_1fAddTeam(self):
        
        driver = self.driver

        WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located((By.ID, SelectorId_LoginUserName)))
        time.sleep(5)
        driver.find_element_by_name(SelectorName_Username).send_keys(Email_Add)
        driver.find_element_by_class_name(SelectorClass_NextButton).click()
        WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_SubmitButton)))
        time.sleep(1)
        driver.find_element_by_class_name(SelectorClass_LoginPassword).send_keys(Password)
        driver.find_element_by_class_name(SelectorClass_SubmitButton).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_ChatIcon)))
        time.sleep(2)
        driver.find_element_by_id(SelectorId_SidebarExpand).click()
        WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, SelectorClass_Administrator), "Administration"))
        (driver.find_element_by_id(SelectorId_AdministrationMenu).find_elements_by_tag_name("img"))[2].click()
        WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, SelectorClass_Administrator), "Administration"))

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.ID, SelectorId_AddTeamMenu)))
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID, SelectorId_AddTeamMenu)))
        WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, SelectorClass_AddTeam_Continue), "Continue"))
        driver.find_element_by_name(SelectorName_AddTeam_Name).send_keys(str(uuid.uuid1())[:8])
        driver.find_element_by_name(SelectorName_AddTeam_Email).send_keys(str(uuid.uuid1())[:8]+"@gmail.com")
        driver.find_element_by_name(SelectorName_AddTeam_Phone).send_keys("+63" + "912" + '{:07}'.format(random.randrange(1, 9**3)))
        driver.find_element_by_class_name(SelectorClass_AddTeam_ContinueButton).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, SelectorClass_AddTeam_Notification)))
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_AddTeam_Notification)))
        time.sleep(1)

        if self.assertEqual("Your team account has been created!", (driver.find_element_by_class_name(SelectorClass_AddTeam_Notification).find_elements_by_tag_name("div"))[5].get_attribute("innerText")) is True:
            False




    def tearDown(self):
        self.driver.quit()



    def test_1hAbout_InviteAFriendLink(self):

        driver = self.driver

        WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located((By.ID, SelectorId_LoginUserName)))
        time.sleep(5)
        driver.find_element_by_name(SelectorName_Username).send_keys(Email_Add)
        driver.find_element_by_class_name(SelectorClass_NextButton).click()
        WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_SubmitButton)))
        time.sleep(1)
        driver.find_element_by_class_name(SelectorClass_LoginPassword).send_keys(Password)
        driver.find_element_by_class_name(SelectorClass_SubmitButton).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_ChatIcon)))
        time.sleep(2)
        driver.find_element_by_id(SelectorId_SidebarExpand).click()
        WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, SelectorClass_SideBarChatIcon), "Chats"))
        time.sleep(5)
        (driver.find_element_by_id(SelectorId_AdministrationMenu).find_elements_by_tag_name("img"))[1].click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, SelectorClass_About_InviteFriend)))
        (driver.find_element_by_id(SelectorId_About).find_elements_by_tag_name("a"))[0].click()
        WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, SelectorClass_About_Title), "About"))
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_About_Menu)))
        (driver.find_element_by_class_name(SelectorClass_About_Menu).find_elements_by_tag_name("div"))[1].click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_AddNewMenu_OverlayInvite)))
        time.sleep(1)
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_AddNewMenu_OverlayInvite)))
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_AddNewMenu_InviteSMS_DialogBoxTitle)))
        WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, SelectorClass_AddNewMenu_InviteSMS_DialogBoxTitle), "Invitation Link"))
        driver.get(driver.find_element_by_name(SelectorName_AddNewMenu_InviteEmail_Link).get_attribute("value"))

        if self.assertTrue("Welcome to Tommy!" in driver.page_source) is True:
            False


    def tearDown(self):
        self.driver.quit()





    def test_1lAbout_Account(self):
        
        driver = self.driver

        WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located((By.ID, SelectorId_LoginUserName)))
        time.sleep(5)
        driver.find_element_by_name(SelectorName_Username).send_keys(Email_Add)
        driver.find_element_by_class_name(SelectorClass_NextButton).click()
        WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_SubmitButton)))
        time.sleep(1)
        driver.find_element_by_class_name(SelectorClass_LoginPassword).send_keys(Password)
        driver.find_element_by_class_name(SelectorClass_SubmitButton).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_ChatIcon)))
        time.sleep(2)
        driver.find_element_by_id(SelectorId_SidebarExpand).click()
        WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, SelectorClass_SideBarChatIcon), "Chats"))
        (driver.find_element_by_id(SelectorId_AdministrationMenu).find_elements_by_tag_name("img"))[0].click()
        WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, SelectorClass_LogoutButton),"Logout"))

        details = ("Emman",       "Galleto",   "1989-10-30","eagalleto@gmail.com", "+6391233026697")
        selector = ("first_name", "last_name", "dob",         "email",               "mobile")


        if self.assertEqual(details[0], driver.find_element_by_name(selector[0]).get_attribute("value")) is True:
            False

        if self.assertEqual(details[1], driver.find_element_by_name(selector[1]).get_attribute("value")) is True:
            False

        if self.assertEqual(details[2], driver.find_element_by_name(selector[2]).get_attribute("value")) is True:
            False

        if self.assertEqual(details[3], driver.find_element_by_name(selector[3]).get_attribute("value")) is True:
            False

        if self.assertEqual(details[4], driver.find_element_by_name(selector[4]).get_attribute("value")) is True:
            False



    def tearDown(self):
        self.driver.quit()












    # def test_1mCreateTask(self):

    #     driver = self.driver

    #     #For Login
    #     WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located((By.ID, SelectorId_LoginUserName)))
    #     time.sleep(5)
    #     driver.find_element_by_name(SelectorName_Username).send_keys(Email_Add2)
    #     driver.find_element_by_class_name(SelectorClass_NextButton).click()
    #     WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_SubmitButton)))
    #     time.sleep(1)
    #     driver.find_element_by_class_name(SelectorClass_LoginPassword).send_keys(Password)
    #     driver.find_element_by_class_name(SelectorClass_SubmitButton).click()
    #     WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_ChatIcon)))
    #     driver.find_element_by_id(SelectorId_SidebarExpand).click()
    #     WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, SelectorClass_Administrator), "Administration"))
    #     time.sleep(10)
    #     WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID, SelectorId_SidebarTask)))
    #     driver.find_element_by_id(SelectorId_SidebarTask).click()
    #     WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.ID, "tasks__tasks")))
    #     WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "list-footer")))
    #     driver.find_element_by_class_name("f7-icons").click()


        # (driver.find_element_by_id(SelectorId_AdministrationMenu).find_elements_by_tag_name("img"))[0].click()
        # WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, SelectorClass_LogoutButton),"Logout"))
        # time.sleep(1)
        # driver.find_element_by_class_name(SelectorClass_LogoutButton).click()
        # time.sleep(1)
        # WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_NextButton)))

        # if self.assertEqual("Email address / Phone", driver.find_element_by_class_name(SelectorName_Username).get_attribute("placeholder")) is True:
        #     False


    def tearDown(self):
        self.driver.quit()







if __name__ == "__main__":
    unittest.main()