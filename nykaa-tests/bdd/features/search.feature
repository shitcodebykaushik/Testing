Feature: Search Error Handling
  As a customer
  I want to search with special characters
  So that the site handles invalid input gracefully

  @search
  Scenario: Search with special characters does not crash
    Given I am on the Nykaa homepage
    When I search for "!@#$%"
    Then the page should load without errors
