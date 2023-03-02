from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.LoginPage import LoginPage 


@When('I enter username "{user}" and password "{pwd}"')
def enterUsernamePwd(context, user, pwd):
    context.loginPage.enterUserName(user)
    context.loginPage.enterPwd(pwd)


@When('I click login button')
def clickLogin(context):
    context.loginPage.clickLogin()



