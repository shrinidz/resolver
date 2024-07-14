Feature: Testing HTML page with Selenium and Behave

  Scenario: Test 1
    Given I am on the home page
    Then I should see email address and password inputs and the login button
    When I enter email "test@example.com" and password "password"
    Then the login form should be submitted

  Scenario: Test 2
    Given I am on the home page
    Then I should see 3 items in the list group in test 2 div
    And the second list item's text should be "List Item 2"
    And the second list item's badge value should be 6

  Scenario: Test 3
    Given I am on the home page
    Then "Option 1" should be the default selected value in the dropdown
    When I select "Option 3" from the dropdown
    Then "Option 3" should be the selected value in the dropdown

  Scenario: Test 4
    Given I am on the home page
    Then the first button in test 4 div should be enabled
    And the second button in test 4 div should be disabled

  Scenario: Test 5
    Given I am on the home page
    When I wait for the button to be displayed in test 5 div
    And I click the button in test 5 div
    Then I should see a success message in test 5 div
    And the button in test 5 div should be disabled

  Scenario: Test 6
    Given I am on the home page
    When I get the value of the cell at row 2, column 2
    Then the cell value should be "Ventosanzap"
