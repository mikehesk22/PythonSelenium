Feature: This feature contains tests for login to OrangeHRM

Background: 
    Given I launch the chrome browser
    When I open the OrangeHRM home page

Scenario: Login to OrangeHRM with Valid Parameters    
    When I enter username "Admin" and password "admin123"
    And I click login button
    Then I verify that the user is successfully logged in to dashboard page
    And I close the browser