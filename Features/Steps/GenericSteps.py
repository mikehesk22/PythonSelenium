from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I launch the chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome("Drivers/chromedriver.exe")


@when('I open the OrangeHRM home page')
def navigateToUrl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@then('I close the browser')
def closeBrowser(context):
    context.driver.close()