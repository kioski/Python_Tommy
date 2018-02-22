import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class  Verify_Share_Via_Social_Media(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver.maximize_window()
        

    def test_Open_Website(self):

        self.driver.get("https://app.mytommy.com/")
        driver = self.driver
        wait = WebDriverWait(self.driver, 180)
        # new WebDriverWait(driver, TimeSpan.FromSeconds(60)).Until(ExpectedConditions.ElementExists((By.Id("login_username"))));
        # driver.FindElement(By.Name("username")).SendKeys("eagalleto@gmail.com");
        driver.find_element_by_name("username").SendKeys("eagalleto@gmail.com")

        driver.FindElement(By.ClassName("button-fill")).Click();
        Assert.AreEqual(driver.FindElement(By.Name("username")).GetAttribute("value"), "eagalleto@gmail.com");

        # new WebDriverWait(driver, TimeSpan.FromSeconds(60)).Until(ExpectedConditions.ElementExists((By.ClassName("submit-login"))));
        driver.FindElement(By.ClassName("password")).SendKeys("Tommy123");
        # new WebDriverWait(driver, TimeSpan.FromSeconds(60)).Until(ExpectedConditions.ElementToBeClickable((By.ClassName("submit-login"))));
        driver.FindElement(By.ClassName("submit-login")).Click();
        # new WebDriverWait(driver, TimeSpan.FromSeconds(60)).Until(ExpectedConditions.ElementExists((By.ClassName("icon-chat"))));

        Assert.IsTrue(driver.FindElement(By.ClassName("chat-tab-link")).GetAttribute("innerText").Contains("Chats"));

        driver.FindElement(By.Id("main-menu-drag-handle")).Click();
        # new WebDriverWait(driver, TimeSpan.FromSeconds(60)).Until(ExpectedConditions.ElementToBeClickable((By.XPath("//*[@id=\"main-menu-administration\"]/div[2]/ul/li[1]/a"))));
        driver.FindElement(By.XPath("//*[@id=\"main-menu-administration\"]/div[2]/ul/li[1]/a")).Click();
        # new WebDriverWait(driver, TimeSpan.FromSeconds(60)).Until(ExpectedConditions.ElementToBeClickable((By.ClassName("logout-button"))));
        # Thread.Sleep(1000);
        driver.FindElement(By.ClassName("logout-button")).Click();
        # new WebDriverWait(driver, TimeSpan.FromSeconds(60)).Until(ExpectedConditions.ElementExists((By.Name("username"))));

        Assert.AreEqual(driver.FindElement(By.Name("username")).GetAttribute("placeholder"), "Email address / Phone");

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
