Feature: Product Sorting
  As a customer
  I want to sort lipstick products by price
  So that I can find the best deals

  @sorting
  Scenario: Sort by price Low to High
    Given I navigate to the lipstick listing
    When I select sort by "Low to High"
    Then the products should be sorted by price
