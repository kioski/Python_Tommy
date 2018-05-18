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

class TommyTests(unittest.TestCase):


    def setUp(self):

        self.driver = webdriver.Remote(command_executor,desired_capabilities_ios)
        # self.driver = webdriver.Remote(command_executor,desired_capabilities_android)

        # self.driver = webdriver.Chrome()
        # self.driver.maximize_window()

        self.driver.get("https://app.mytommy.com/")


    # def test_1aLoginAndLogout(self):

    #     driver = self.driver

    #     #For Login
    #     WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located((By.ID, SelectorId_LoginUserName)))
    #     time.sleep(5)
    #     driver.find_element_by_name(SelectorName_Username).send_keys(Email_Add)
    #     driver.find_element_by_class_name(SelectorClass_NextButton).click()
    #     WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_SubmitButton)))
    #     time.sleep(1)
    #     driver.find_element_by_class_name(SelectorClass_LoginPassword).send_keys(Password)
    #     driver.find_element_by_class_name(SelectorClass_SubmitButton).click()
    #     WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_ChatIcon)))
        
    #     self.assertEqual("Chats", driver.find_element_by_class_name(SelectorClass_ChatTitle).get_attribute("innerText"))

    #     #For Logout
    #     driver.find_element_by_id(SelectorId_SidebarExpand).click()
    #     WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, SelectorClass_Administrator), "Administration"))
    #     (driver.find_element_by_id(SelectorId_AdministrationMenu).find_elements_by_tag_name("img"))[0].click()
    #     WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, SelectorClass_LogoutButton),"Logout"))
    #     time.sleep(1)
    #     driver.find_element_by_class_name(SelectorClass_LogoutButton).click()
    #     time.sleep(1)
    #     WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_NextButton)))

    #     try:
    #         self.assertEqual("Email address / Phone", driver.find_element_by_class_name(SelectorName_Username).get_attribute("placeholder"))

    #     except AssertionError as Error:

    #         print("Error_1: " + str(Error))

    # def tearDown(self):
    #     self.driver.quit()



    # def test_1bContacts_NewChat(self):
        
    #     driver = self.driver

    #     WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located((By.ID, SelectorId_LoginUserName)))
    #     time.sleep(5)
    #     driver.find_element_by_name(SelectorName_Username).send_keys(Email_Add)
    #     driver.find_element_by_class_name(SelectorClass_NextButton).click()
    #     WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_SubmitButton)))
    #     time.sleep(1)
    #     driver.find_element_by_class_name(SelectorClass_LoginPassword).send_keys(Password)
    #     driver.find_element_by_class_name(SelectorClass_SubmitButton).click()
    #     WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_ChatIcon)))
    #     time.sleep(3)
    #     WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, SelectorClass_AddNewMenu)))
    #     driver.find_element_by_class_name(SelectorClass_AddNewMenu).click()
    #     WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, SelectorClass_AddNewMenu)))
    #     time.sleep(2)
    #     (driver.find_element_by_class_name(SelectorClass_AddNewMenu_NewChat).find_elements_by_tag_name("img"))[0].click()
    #     WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_OverLay)))
    #     time.sleep(2)
    #     (driver.find_element_by_class_name(SelectorClass_AddNewMenu_NewChatCheckBox).find_elements_by_tag_name("div"))[0].click()
    #     WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_CheckBox)))
    #     driver.find_element_by_class_name(SelectorClass_AddNewMenu_NewChatOkButton).click()
    #     WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID, SelectorId_AddNewMenu_TextBox)))
    #     Sample_Text = str(uuid.uuid1())[:8] + str(uuid.uuid1())[2:6]
    #     time.sleep(1)
    #     driver.find_element_by_id(SelectorId_AddNewMenu_TextBox).send_keys(Sample_Text)
    #     (driver.find_element_by_class_name(SelectorClass_AddNewMenu_TextBoxSendBUtton).find_elements_by_tag_name("a"))[0].click()
    #     time.sleep(2)
      

    #     try:

    #         self.assertTrue(Sample_Text in driver.page_source)

    #     except AssertionError as Error:

    #         print("Error_2: " + str(Error) + " [Word Not Found]")



    # def tearDown(self):
    #     self.driver.quit()




    #Remove SMS in Hybrid
    # # def test_1cContacts_AddContacts_SMS(self):
        
    # #     driver = self.driver

    # #     WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.ID, SelectorId_LoginUserName)))
    # #     driver.find_element_by_name(SelectorName_Username).send_keys(Email_Add)
    # #     driver.find_element_by_class_name(SelectorClass_NextButton).click()
    # #     WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_SubmitButton)))
    # #     driver.find_element_by_class_name(SelectorClass_LoginPassword).send_keys(Password)
    # #     driver.find_element_by_class_name(SelectorClass_SubmitButton).click()
    # #     WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_ChatIcon)))
    # #     time.sleep(3)
    # #     WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, SelectorClass_AddNewMenu)))
    # #     driver.find_element_by_class_name(SelectorClass_AddNewMenu).click()
    # #     WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, SelectorClass_AddNewMenu)))
    # #     time.sleep(2)
    # #     (driver.find_element_by_class_name(SelectorClass_AddNewMenu_NewChat).find_elements_by_tag_name("img"))[1].click()
    # #     WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID, SelectorId_AddNewMenu_Invite)))
    # #     driver.find_element_by_id(SelectorId_AddNewMenu_Invite).click()
    # #     WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_AddNewMenu_Overlay)))
    # #     time.sleep(2)
    # #     (driver.find_element_by_class_name(SelectorClass_AddNewMenu_InviteSMS).find_elements_by_tag_name("div"))[0].click()
    # #     WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_AddNewMenu_OverlayInvite)))
    # #     driver.find_element_by_name(SelectorName_AddNewMenu_InviteSMS_Name).send_keys("Tommy Test")
    # #     driver.find_element_by_name(SelectorName_AddNewMenu_InviteSMS_Mobile).send_keys("+63" + '912' + '{:05}'.format(random.randrange(1, 9**3)))
    # #     (driver.find_element_by_class_name(SelectorClass_AddNewMenu_InviteSMS_Send).find_elements_by_tag_name("span"))[1].click()
    # #     WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_AddNewMenu_InviteSMS_DialogBox)))
    # #     WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, SelectorClass_AddNewMenu_InviteSMS_DialogBox)))
    # #     WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, SelectorClass_AddNewMenu_InviteSMS_DialogBoxTitle), "Tommy"))


    # #     # Confirmation not correct. It should say Sent or Confirm
    # #     try:
    # #         self.assertEqual("Sent", driver.find_element_by_class_name(SelectorClass_AddNewMenu_InviteSMS_Confirmation).find_elements_by_tag_name("div")[1].get_attribute("innerText"))

    # #     except AssertionError as Error:

    # #         print("Error_3: " + str(Error))
        


    # def tearDown(self):
    #     self.driver.close()




    # def test_1dContacts_AddContacts_Email(self):
        
    #     driver = self.driver

    #     WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.ID, SelectorId_LoginUserName)))
    #     driver.find_element_by_name(SelectorName_Username).send_keys(Email_Add)
    #     driver.find_element_by_class_name(SelectorClass_NextButton).click()
    #     WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_SubmitButton)))
    #     driver.find_element_by_class_name(SelectorClass_LoginPassword).send_keys(Password)
    #     driver.find_element_by_class_name(SelectorClass_SubmitButton).click()
    #     WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_ChatIcon)))
    #     WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, SelectorClass_AddNewMenu)))
    #     driver.find_element_by_class_name(SelectorClass_AddNewMenu).click()
    #     WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, SelectorClass_AddNewMenu)))
    #     (driver.find_element_by_class_name(SelectorClass_AddNewMenu_NewChat).find_elements_by_tag_name("img"))[1].click()
    #     WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID, SelectorId_AddNewMenu_Invite)))
    #     driver.find_element_by_id(SelectorId_AddNewMenu_Invite).click()
    #     WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_AddNewMenu_Overlay)))
    #     (driver.find_element_by_class_name(SelectorClass_AddNewMenu_InviteSMS).find_elements_by_tag_name("div"))[1].click()
    #     WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_AddNewMenu_OverlayInvite)))
    #     driver.find_element_by_name(SelectorName_AddNewMenu_InviteEmail_Name).send_keys("Tommy Test")
    #     driver.find_element_by_name(SelectorName_AddNewMenu_InviteEmail_Email).send_keys(str(uuid.uuid1())+"@gmail.com")
    #     (driver.find_element_by_class_name(SelectorClass_AddNewMenu_InviteSMS_Send).find_elements_by_tag_name("span"))[1].click()

    #     # No Confirmation Dialog Box. Wait must be consider   
    #     try:
    #         WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_AddNewMenu_InviteSMS_DialogBox)))
    #         WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, SelectorClass_AddNewMenu_InviteSMS_DialogBox)))
    #         WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, SelectorClass_AddNewMenu_InviteSMS_DialogBoxTitle), "Tommy"))
        
    #     except:

    #         print("Error_4: No Dialog Box Confirmation")


    # def tearDown(self):
    #     self.driver.close()




    def test_1eContacts_AddContacts_InvitationLink(self):
        
        driver = self.driver

        WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.ID, SelectorId_LoginUserName)))
        time.sleep(5)
        driver.find_element_by_name(SelectorName_Username).send_keys(Email_Add)
        driver.find_element_by_class_name(SelectorClass_NextButton).click()
        WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_SubmitButton)))
        driver.find_element_by_class_name(SelectorClass_LoginPassword).send_keys(Password)
        driver.find_element_by_class_name(SelectorClass_SubmitButton).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_ChatIcon)))
        time.sleep(3)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, SelectorClass_AddNewMenu)))
        driver.find_element_by_class_name(SelectorClass_AddNewMenu).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, SelectorClass_AddNewMenu)))
        time.sleep(2)
        (driver.find_element_by_class_name(SelectorClass_AddNewMenu_NewChat).find_elements_by_tag_name("img"))[1].click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID, SelectorId_AddNewMenu_Invite)))
        driver.find_element_by_id(SelectorId_AddNewMenu_Invite).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_AddNewMenu_Overlay)))
        time.sleep(1)
        (driver.find_element_by_class_name(SelectorClass_AddNewMenu_InviteSMS).find_elements_by_tag_name("div"))[1].click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_AddNewMenu_OverlayInvite)))
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_AddNewMenu_InviteSMS_DialogBoxTitle)))
        WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, SelectorClass_AddNewMenu_InviteSMS_DialogBoxTitle), "Invitation Link"))
        driver.get(driver.find_element_by_name(SelectorName_AddNewMenu_InviteEmail_Link).get_attribute("value"))

        try:
            self.assertTrue("Welcome to Tommy!" in driver.page_source)

        except AssertionError as Error:

            print("Error_5: " + str(Error))


    def tearDown(self):
        self.driver.quit()




    def test_1fAddTeam(self):
        
        driver = self.driver

        WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.ID, SelectorId_LoginUserName)))
        time.sleep(5)
        driver.find_element_by_name(SelectorName_Username).send_keys(Email_Add)
        driver.find_element_by_class_name(SelectorClass_NextButton).click()
        WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_SubmitButton)))
        driver.find_element_by_class_name(SelectorClass_LoginPassword).send_keys(Password)
        driver.find_element_by_class_name(SelectorClass_SubmitButton).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_ChatIcon)))
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
        time.sleep(2)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, SelectorClass_AddTeam_Notification)))
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_AddTeam_Notification)))

        try:
            self.assertEqual("Your team account has been created!", (driver.find_element_by_class_name(SelectorClass_AddTeam_Notification).find_elements_by_tag_name("div"))[5].get_attribute("innerText"))

        except AssertionError as Error:

            print("Error_6: " + str(Error))
        


    def tearDown(self):
        self.driver.quit()



    # def test_1gAbout_InviteAFriendSMS(self):

    #     driver = self.driver

    #     WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.ID, SelectorId_LoginUserName)))
    #     driver.find_element_by_name(SelectorName_Username).send_keys(Email_Add)
    #     driver.find_element_by_class_name(SelectorClass_NextButton).click()
    #     WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_SubmitButton)))
    #     driver.find_element_by_class_name(SelectorClass_LoginPassword).send_keys(Password)
    #     driver.find_element_by_class_name(SelectorClass_SubmitButton).click()
    #     WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_ChatIcon)))
    #     driver.find_element_by_id(SelectorId_SidebarExpand).click()
    #     WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, SelectorClass_SideBarChatIcon), "Chats"))
    #     (driver.find_element_by_id(SelectorId_AdministrationMenu).find_elements_by_tag_name("img"))[1].click()
    #     WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, SelectorClass_About_InviteFriend)))
    #     (driver.find_element_by_id(SelectorId_About).find_elements_by_tag_name("a"))[0].click()
    #     WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, SelectorClass_About_Title), "About"))
    #     WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_About_Menu)))
    #     (driver.find_element_by_class_name(SelectorClass_About_Menu).find_elements_by_tag_name("div"))[0].click()
    #     WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_AddNewMenu_OverlayInvite)))
    #     driver.find_element_by_name(SelectorName_AddNewMenu_InviteSMS_Name).send_keys("Tommy Test")
    #     driver.find_element_by_name(SelectorName_AddNewMenu_InviteSMS_Mobile).send_keys("+63" + '912' + '{:07}'.format(random.randrange(1, 9**3)))
    #     (driver.find_element_by_class_name(SelectorClass_AddNewMenu_InviteSMS_Send).find_elements_by_tag_name("span"))[1].click()
    #     WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_AddNewMenu_InviteSMS_DialogBox)))
    #     WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, SelectorClass_AddNewMenu_InviteSMS_DialogBox)))
    #     WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, SelectorClass_AddNewMenu_InviteSMS_DialogBoxTitle), "Tommy"))

    #     # Confirmation not correct. It should say Sent or Confirm   
    #     try:
    #         self.assertEqual("Sent", driver.find_element_by_class_name(SelectorClass_AddNewMenu_InviteSMS_Confirmation).find_elements_by_tag_name("div")[1].get_attribute("innerText"))

    #     except AssertionError as Error:

    #         print("Error_7: " + str(Error))
        

    # def tearDown(self):
    #     self.driver.close()



    # def test_1hAbout_InviteAFriendEmail(self):

    #     driver = self.driver

    #     WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.ID, SelectorId_LoginUserName)))
    #     driver.find_element_by_name(SelectorName_Username).send_keys(Email_Add)
    #     driver.find_element_by_class_name(SelectorClass_NextButton).click()
    #     WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_SubmitButton)))
    #     driver.find_element_by_class_name(SelectorClass_LoginPassword).send_keys(Password)
    #     driver.find_element_by_class_name(SelectorClass_SubmitButton).click()
    #     WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_ChatIcon)))
    #     driver.find_element_by_id(SelectorId_SidebarExpand).click()
    #     WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, SelectorClass_SideBarChatIcon), "Chats"))
    #     (driver.find_element_by_id(SelectorId_AdministrationMenu).find_elements_by_tag_name("img"))[1].click()
    #     WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, SelectorClass_About_InviteFriend)))
    #     (driver.find_element_by_id(SelectorId_About).find_elements_by_tag_name("a"))[0].click()
    #     WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, SelectorClass_About_Title), "About"))
    #     WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_About_Menu)))
    #     (driver.find_element_by_class_name(SelectorClass_About_Menu).find_elements_by_tag_name("div"))[1].click()
    #     WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_AddNewMenu_OverlayInvite)))
    #     driver.find_element_by_name(SelectorName_AddNewMenu_InviteEmail_Name).send_keys("Tommy Test")
    #     driver.find_element_by_name(SelectorName_AddNewMenu_InviteEmail_Email).send_keys(str(uuid.uuid1())[:8]+"@gmail.com")
    #     (driver.find_element_by_class_name(SelectorClass_AddNewMenu_InviteSMS_Send).find_elements_by_tag_name("span"))[1].click()

    # #     # No Confirmation Dialog Box. Wait must be consider   
    #     try:
    #         WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_AddNewMenu_InviteSMS_DialogBox)))
    #         WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, SelectorClass_AddNewMenu_InviteSMS_DialogBox)))
    #         WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, SelectorClass_AddNewMenu_InviteSMS_DialogBoxTitle), "Tommy"))
        
    #     except:

    #         print("Error_8: No Dialog Box Confirmation")


    # def tearDown(self):
    #     self.driver.close()




    # def test_1iAbout_InviteAFriendInvitelink(self):

    #     driver = self.driver

    #     WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.ID, SelectorId_LoginUserName)))
    #     driver.find_element_by_name(SelectorName_Username).send_keys(Email_Add)
    #     driver.find_element_by_class_name(SelectorClass_NextButton).click()
    #     WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_SubmitButton)))
    #     driver.find_element_by_class_name(SelectorClass_LoginPassword).send_keys(Password)
    #     driver.find_element_by_class_name(SelectorClass_SubmitButton).click()
    #     WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_ChatIcon)))
    #     driver.find_element_by_id(SelectorId_SidebarExpand).click()
    #     WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, SelectorClass_SideBarChatIcon), "Chats"))
    #     (driver.find_element_by_id(SelectorId_AdministrationMenu).find_elements_by_tag_name("img"))[1].click()
    #     WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, SelectorClass_About_InviteFriend)))
    #     (driver.find_element_by_id(SelectorId_About).find_elements_by_tag_name("a"))[0].click()
    #     WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, SelectorClass_About_Title), "About"))
    #     WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_About_Menu)))
    #     (driver.find_element_by_class_name(SelectorClass_About_Menu).find_elements_by_tag_name("div"))[2].click()
    #     WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_AddNewMenu_OverlayInvite)))
    #     WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_AddNewMenu_InviteSMS_DialogBoxTitle)))
    #     WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, SelectorClass_AddNewMenu_InviteSMS_DialogBoxTitle), "Invitation Link"))
    #     driver.get(driver.find_element_by_name(SelectorName_AddNewMenu_InviteEmail_Link).get_attribute("value"))

    #     try:
    #         self.assertTrue("Welcome to Tommy!" in driver.page_source)

    #     except AssertionError as Error:

    #         print("Error_9: " + str(Error))


    # def tearDown(self):
    #     self.driver.close()




    # def test_1jAbout_Feedback(self):
        
    #     driver = self.driver

    #     WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.ID, SelectorId_LoginUserName)))
    #     driver.find_element_by_name(SelectorName_Username).send_keys(Email_Add)
    #     driver.find_element_by_class_name(SelectorClass_NextButton).click()
    #     WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_SubmitButton)))
    #     driver.find_element_by_class_name(SelectorClass_LoginPassword).send_keys(Password)
    #     driver.find_element_by_class_name(SelectorClass_SubmitButton).click()
    #     WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_ChatIcon)))
    #     driver.find_element_by_id(SelectorId_SidebarExpand).click()
    #     WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, SelectorClass_SideBarChatIcon), "Chats"))
    #     (driver.find_element_by_id(SelectorId_AdministrationMenu).find_elements_by_tag_name("img"))[1].click()
    #     WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, SelectorClass_About_InviteFriend)))
    #     (driver.find_element_by_id(SelectorId_About).find_elements_by_tag_name("a"))[1].click()
    #     WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID, SelectorId_Feedback)))
    #     WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID, SelectorId_Feedback)))

    #     try:
    #         self.assertEqual("Feedback", driver.find_element_by_id(SelectorId_Feedback).find_elements_by_tag_name("p")[0].get_attribute("innerText"))

    #     except AssertionError as Error:

    #         print("Error_10: " + str(Error))

        

    # def tearDown(self):
    #     self.driver.close()


    # def test_1kAbout_Acknowledgements(self):
        
    #     driver = self.driver

    #     WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.ID, SelectorId_LoginUserName)))
    #     driver.find_element_by_name(SelectorName_Username).send_keys(Email_Add)
    #     driver.find_element_by_class_name(SelectorClass_NextButton).click()
    #     WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_SubmitButton)))
    #     driver.find_element_by_class_name(SelectorClass_LoginPassword).send_keys(Password)
    #     driver.find_element_by_class_name(SelectorClass_SubmitButton).click()
    #     WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_ChatIcon)))
    #     driver.find_element_by_id(SelectorId_SidebarExpand).click()
    #     WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, SelectorClass_SideBarChatIcon), "Chats"))
    #     (driver.find_element_by_id(SelectorId_AdministrationMenu).find_elements_by_tag_name("img"))[1].click()
    #     WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, SelectorClass_About_InviteFriend)))
    #     (driver.find_element_by_id(SelectorId_About).find_elements_by_tag_name("a"))[2].click()
    #     WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID, SelectorId_Feedback)))
    #     WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID, SelectorId_Feedback)))

    #     try:
    #         self.assertEqual("Acknowledgements", driver.find_element_by_id(SelectorId_Feedback).find_elements_by_tag_name("p")[0].get_attribute("innerText"))

    #     except AssertionError as Error:

    #         print("Error_11: " + str(Error))

        

    # def tearDown(self):
    #     self.driver.close()



    # def test_1lAbout_Account(self):
        
    #     driver = self.driver

    #     WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.ID, SelectorId_LoginUserName)))
    #     driver.find_element_by_name(SelectorName_Username).send_keys(Email_Add)
    #     driver.find_element_by_class_name(SelectorClass_NextButton).click()
    #     WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_SubmitButton)))
    #     driver.find_element_by_class_name(SelectorClass_LoginPassword).send_keys(Password)
    #     driver.find_element_by_class_name(SelectorClass_SubmitButton).click()
    #     WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_ChatIcon)))
    #     driver.find_element_by_id(SelectorId_SidebarExpand).click()
    #     WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, SelectorClass_SideBarChatIcon), "Chats"))
    #     (driver.find_element_by_id(SelectorId_AdministrationMenu).find_elements_by_tag_name("img"))[0].click()
    #     WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, SelectorClass_SaveButton), "Save"))
    #     WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, SelectorClass_LogoutButton), "Logout"))

    #     details = ("Emman",       "Galleto",   "1989-10-30<","eagalleto@gmail.com", "+6391233026697")
    #     selector = ("first_name", "last_name", "dob",         "email",               "mobile")

    #     try:
    #         self.assertEqual(details[0], driver.find_element_by_name(selector[0]).get_attribute("value"))
    #     except AssertionError as Error:
    #         print("Error_12: " + str(Error))
    #     try:
    #         self.assertEqual(details[1], driver.find_element_by_name(selector[1]).get_attribute("value"))
    #     except AssertionError as Error:
    #         print("Error_12: " + str(Error))
    #     try:
    #         self.assertEqual(details[2], driver.find_element_by_name(selector[2]).get_attribute("value"))
    #     except AssertionError as Error:
    #         print("Error_12: " + str(Error))
    #     try:
    #         self.assertEqual(details[3], driver.find_element_by_name(selector[3]).get_attribute("value"))
    #     except AssertionError as Error:
    #         print("Error_12: " + str(Error))
    #     try:      
    #         self.assertEqual(details[4], driver.find_element_by_name(selector[4]).get_attribute("value"))
    #     except AssertionError as Error:
    #         print("Error_12: " + str(Error))


    # def tearDown(self):
    #     self.driver.close()



if __name__ == "__main__":
    unittest.main()