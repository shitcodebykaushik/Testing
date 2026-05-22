Feature: Product Details
  As a customer
  I want to view product details
  So that I can see the product name and price

  @product-detail
  Scenario: Product detail page displays name and price
    Given I navigate to the lipstick listing
    When I click the first product
    And I switch to the product detail tab
    Then the product name should be visible
    And the product price should be visible
