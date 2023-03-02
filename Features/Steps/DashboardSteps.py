from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Pages.DashboardPage import DashboardPage

@Then('I verify that the user is successfully logged in to dashboard page')
def verifyDashboard(context):
    context.dashboardPage.verifyDashboardHeading()
