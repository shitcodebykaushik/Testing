Feature: Makeup Navigation
  As a customer
  I want to navigate through the Makeup menu
  So that I can browse lipstick products

  @navigation
  Scenario: Hover Makeup and click Lipstick navigates to lipstick listing
    Given I am on the Nykaa homepage
    When I hover over Makeup and click Lipstick
    Then I should see the lipstick listing page heading
