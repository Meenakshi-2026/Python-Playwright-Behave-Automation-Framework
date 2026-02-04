Feature: Login Functionality

  Scenario: Successful Login
    Given I am on the Saucedemo login page
    When I login with valid credentials
    Then I should see the inventory page

  Scenario: Invalid Login
    Given I am on the Saucedemo login page
    When I login with invalid credentials "invalid_user" and "invalid_pass"
    Then I should see an error message
