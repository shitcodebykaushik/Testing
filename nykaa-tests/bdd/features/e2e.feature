Feature: End-to-End Lipstick Purchase Flow
  As a customer
  I want to browse, filter, sort, view and add lipstick products to bag
  So that I can purchase lipstick online

  @e2e @step1
  Scenario: Step 1 - Navigate to lipstick listing page
    Given I am on the Nykaa homepage
    When I hover over Makeup and click Lipstick
    Then I should see the lipstick listing page heading

  @e2e @step2
  Scenario: Step 2 - Verify products are displayed on listing
    Given I navigate to the lipstick listing
    Then there should be products displayed on the listing

  @e2e @step3
  Scenario: Step 3 - Filter products by brand Lakme
    Given I navigate to the lipstick listing
    When I filter by brand "Lakme"
    Then the URL should contain the brand parameter

  @e2e @step4
  Scenario: Step 4 - Filter products by brand Maybelline
    Given I navigate to the lipstick listing
    When I filter by brand "Maybelline"
    Then the URL should contain the brand parameter

  @e2e @step5
  Scenario: Step 5 - Sort products by Price Low to High
    Given I navigate to the lipstick listing
    When I sort by price Low to High
    Then I should still be on the lipstick page

  @e2e @step6
  Scenario: Step 6 - Verify sort parameter in URL
    Given I navigate to the lipstick listing
    When I sort by price Low to High
    Then the URL should contain the sort parameter

  @e2e @step7
  Scenario: Step 7 - Verify product name on PDP
    Given I navigate to the lipstick listing
    When I click the first product
    And I switch to the product detail tab
    Then I should see the product name

  @e2e @step8
  Scenario: Step 8 - Verify product price on PDP
    Given I navigate to the lipstick listing
    When I click the first product
    And I switch to the product detail tab
    Then I should see the product price

  @e2e @step9
  Scenario: Step 9 - Add product to bag
    Given I navigate to the lipstick listing
    When I click the first product
    And I switch to the product detail tab
    And I add the product to bag
    Then the product should be added to bag

  @e2e @step10
  Scenario: Step 10 - Navigate to bag page
    Given I navigate to the lipstick listing
    When I add the first product to bag
    And I go to the bag page
    Then I should be on the bag page

  @e2e @step11
  Scenario: Step 11 - Search for lipstick
    Given I am on the Nykaa homepage
    When I search for "lipstick"
    Then I should see search results

  @e2e @step12
  Scenario: Step 12 - Search special characters should not crash
    Given I am on the Nykaa homepage
    When I search for "!@#$%"
    Then the page should load without errors

  @e2e @step13
  Scenario: Step 13 - Search results page renders
    Given I am on the Nykaa homepage
    When I search for "lipstick"
    Then the search results page should be visible
