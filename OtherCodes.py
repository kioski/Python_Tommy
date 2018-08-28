






# -------------------------------------------------------


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
    #     self.driver.quit()





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
    #     self.driver.quit()





    #  No more SMS
    # # def test_1gAbout_InviteAFriendSMS(self):

    # #     driver = self.driver

    # #     WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located((By.ID, SelectorId_LoginUserName)))
    # #     time.sleep(5)
    # #     driver.find_element_by_name(SelectorName_Username).send_keys(Email_Add)
    # #     driver.find_element_by_class_name(SelectorClass_NextButton).click()
    # #     WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_SubmitButton)))
    # #     time.sleep(1)
    # #     driver.find_element_by_class_name(SelectorClass_LoginPassword).send_keys(Password)
    # #     driver.find_element_by_class_name(SelectorClass_SubmitButton).click()
    # #     WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_ChatIcon)))
    # #     time.sleep(2)
    # #     driver.find_element_by_id(SelectorId_SidebarExpand).click()
    # #     WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, SelectorClass_SideBarChatIcon), "Chats"))
    # #     (driver.find_element_by_id(SelectorId_AdministrationMenu).find_elements_by_tag_name("img"))[1].click()
    # #     WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, SelectorClass_About_InviteFriend)))
    # #     (driver.find_element_by_id(SelectorId_About).find_elements_by_tag_name("a"))[0].click()
    # #     WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, SelectorClass_About_Title), "About"))
    # #     WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_About_Menu)))
    # #     (driver.find_element_by_class_name(SelectorClass_About_Menu).find_elements_by_tag_name("div"))[0].click()
    # #     WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_AddNewMenu_OverlayInvite)))
    # #     driver.find_element_by_name(SelectorName_AddNewMenu_InviteSMS_Name).send_keys("Tommy Test")
    # #     driver.find_element_by_name(SelectorName_AddNewMenu_InviteSMS_Mobile).send_keys("+63" + '912' + '{:07}'.format(random.randrange(1, 9**3)))
    # #     (driver.find_element_by_class_name(SelectorClass_AddNewMenu_InviteSMS_Send).find_elements_by_tag_name("span"))[1].click()
    # #     WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_AddNewMenu_InviteSMS_DialogBox)))
    # #     WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, SelectorClass_AddNewMenu_InviteSMS_DialogBox)))
    # #     WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, SelectorClass_AddNewMenu_InviteSMS_DialogBoxTitle), "Tommy"))

    # #     # Confirmation not correct. It should say Sent or Confirm   
    # #     try:
    # #         self.assertEqual("Sent", driver.find_element_by_class_name(SelectorClass_AddNewMenu_InviteSMS_Confirmation).find_elements_by_tag_name("div")[1].get_attribute("innerText"))

    # #     except AssertionError as Error:

    # #         print("Error_7: " + str(Error))
        

    ## def tearDown(self):
    ##     self.driver.quit()




    #  Cannot determine the email
    # # def test_1iAbout_InviteAFriendInviteEmail(self):

    # #     driver = self.driver

    # #     WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located((By.ID, SelectorId_LoginUserName)))
    # #     time.sleep(5)
    # #     driver.find_element_by_name(SelectorName_Username).send_keys(Email_Add)
    # #     driver.find_element_by_class_name(SelectorClass_NextButton).click()
    # #     WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_SubmitButton)))
    # #     time.sleep(1)
    # #     driver.find_element_by_class_name(SelectorClass_LoginPassword).send_keys(Password)
    # #     driver.find_element_by_class_name(SelectorClass_SubmitButton).click()
    # #     WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_ChatIcon)))
    # #     time.sleep(2)
    # #     driver.find_element_by_id(SelectorId_SidebarExpand).click()
    # #     WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, SelectorClass_SideBarChatIcon), "Chats"))
    # #     (driver.find_element_by_id(SelectorId_AdministrationMenu).find_elements_by_tag_name("img"))[1].click()
    # #     WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, SelectorClass_About_InviteFriend)))
    # #     (driver.find_element_by_id(SelectorId_About).find_elements_by_tag_name("a"))[0].click()
    # #     WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, SelectorClass_About_Title), "About"))
    # #     WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_About_Menu)))
    # #     (driver.find_element_by_class_name(SelectorClass_About_Menu).find_elements_by_tag_name("div"))[0].click()
    # #     WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_AddNewMenu_OverlayInvite)))
    # #     WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, SelectorClass_AddNewMenu_InviteSMS_DialogBoxTitle)))
    # #     WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, SelectorClass_AddNewMenu_InviteSMS_DialogBoxTitle), "Invitation Link"))
    # #     driver.get(driver.find_element_by_name(SelectorName_AddNewMenu_InviteEmail_Link).get_attribute("value"))

    # #     try:
    # #         self.assertTrue("Welcome to Tommy!" in driver.page_source)

    # #     except AssertionError as Error:

    # #         print("Error_9: " + str(Error))


    # # def tearDown(self):
    # #     self.driver.quit()




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
    #     self.driver.quit()


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
    #     self.driver.quit()


