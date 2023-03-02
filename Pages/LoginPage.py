from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage():

    #region Elements
    username = (By.NAME, "username")
    password = (By.NAME, "password")
    loginButton = (By.CLASS_NAME, "orangehrm-login-button")
    #endregion

    def enterUserName(self, user):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.username))
        self.driver.find_element(self.username).send_keys(user)
        

    def enterPwd(self, pwd):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.password))
        self.driver.find_element(self.password).send_keys(pwd)

    
    def clickLogin(self):
        self.driver.find_element(self.loginButton).click()