Feature: Product Filtering
  As a customer
  I want to filter lipstick products by brand
  So that I can find products from specific brands

  @filtering
  Scenario: Filter by brand Lakme
    Given I navigate to the lipstick listing
    When I filter by brand "Lakme"
    Then the filtered results should be displayed
