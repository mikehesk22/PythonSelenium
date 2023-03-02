from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    
#region Elements
    dashboardHeading = (By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[1]/div[1]/span/h6")

#endregion

    def verifyDashboardHeading(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.dashboardHeading))
        text = self.driver.find_element(self.dashboardHeading).text
        assert text == "Dashboard"