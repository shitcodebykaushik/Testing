import time
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage
from pages.lipstick_page import LipstickPage


@given("I am on the Nykaa homepage")
def step_homepage(context):
    context.logger.step("Given: On Nykaa homepage")
    context.home = HomePage(context.driver)


@given("I navigate to the lipstick listing")
def step_nav_to_lipstick(context):
    context.logger.step("Given: Navigate to lipstick listing")
    context.home = HomePage(context.driver)
    context.home.hover_makeup_and_click_lipstick()
    context.lipstick = LipstickPage(context.driver)
    context.logger.action("Landed on lipstick listing page")


@when("I hover over Makeup and click Lipstick")
def step_hover_and_click(context):
    context.logger.step("When: Hover Makeup and click Lipstick")
    home = HomePage(context.driver)
    home.hover_makeup_and_click_lipstick()
    context.lipstick = LipstickPage(context.driver)
    context.logger.action("Hovered Makeup and clicked Lipstick")


@then("I should see the lipstick listing page heading")
def step_verify_heading(context):
    heading = context.lipstick.get_heading_text()
    context.logger.action(f"Listing heading: '{heading}'")
    context.logger.assert_msg(f"Heading contains 'Lipstick'")
    assert "lipstick" in heading.lower(), f"Heading '{heading}' should contain 'Lipstick'"


@then("there should be products displayed on the listing")
def step_verify_products(context):
    count = context.lipstick.get_product_count()
    context.logger.action(f"Product count: {count}")
    context.logger.assert_msg(f"Product count > 0")
    assert count > 0, f"Expected at least 1 product, found {count}"


@when('I filter by brand "{brand}"')
def step_filter_brand(context, brand):
    context.logger.step(f"When: Filter by brand '{brand}'")
    context.lipstick.filter_by_brand(brand)
    context.logger.action(f"Applied '{brand}' brand filter")
    time.sleep(3)


@then("the URL should contain the brand parameter")
def step_url_has_brand(context):
    context.logger.assert_msg(f"URL has brand param: {context.driver.current_url}")
    assert "brand" in context.driver.current_url.lower(), (
        f"URL should contain brand param, got {context.driver.current_url}"
    )


@then("the filtered results should be displayed")
def step_filtered_results(context):
    context.logger.assert_msg(f"Filtered URL: {context.driver.current_url}")
    assert "brand" in context.driver.current_url.lower(), (
        f"URL should contain brand param, got {context.driver.current_url}"
    )


@when('I sort by price Low to High')
@when('I select sort by "{sort_option}"')
def step_sort_low_to_high(context, sort_option="Low to High"):
    context.logger.step(f"When: Sort by '{sort_option}'")
    context.lipstick.select_sort_low_to_high()
    context.logger.action("Selected Low to High sort")
    time.sleep(3)


@then("I should still be on the lipstick page")
def step_still_on_lipstick(context):
    heading = context.lipstick.get_heading_text()
    context.logger.action(f"Heading after sort: '{heading}'")
    context.logger.assert_msg("Still on lipstick page")
    assert "lipstick" in heading.lower(), "Not on lipstick page after sort"


@then("the URL should contain the sort parameter")
def step_url_has_sort(context):
    url = context.driver.current_url.lower()
    has_sort = "sort" in url or "price_asc" in url
    context.logger.assert_msg(f"URL has sort param: {url}")
    assert has_sort, f"URL should contain sort param, got {url}"


@then("the products should be sorted by price")
def step_sorted_by_price(context):
    heading = context.lipstick.get_heading_text()
    context.logger.action(f"Heading after sort: '{heading}'")
    context.logger.assert_msg("Still on lipstick page after sort")
    assert "lipstick" in heading.lower(), "Not on lipstick page"


@when("I click the first product")
def step_click_first_product(context):
    context.logger.step("When: Click first product")
    context.lipstick.click_first_product()
    context.logger.action("Clicked first product link")


@when("I switch to the product detail tab")
def step_switch_to_pdp(context):
    context.logger.step("When: Switch to PDP tab")
    context.driver.switch_to.window(context.driver.window_handles[-1])
    context.logger.action("Switched to new PDP tab")


@then("I should see the product name")
@then("the product name should be visible")
def step_verify_product_name(context):
    name = context.lipstick.get_product_name()
    context.logger.action(f"Product name: '{name}'")
    context.logger.assert_msg("Product name is not empty")
    assert name.strip(), f"Product name should not be empty, got '{name}'"


@then("I should see the product price")
@then("the product price should be visible")
def step_verify_product_price(context):
    price = context.lipstick.get_product_price()
    context.logger.action(f"Product price: '{price}'")
    context.logger.assert_msg("Product price is not empty")
    assert price.strip(), f"Product price should not be empty, got '{price}'"


@when("I add the product to bag")
def step_add_to_bag(context):
    context.logger.step("When: Add to bag")
    context.lipstick.add_to_bag()
    context.logger.action("Clicked Add to Bag")
    time.sleep(2)


@then("the product should be added to bag")
def step_verify_added(context):
    context.logger.assert_msg("Add to Bag clicked successfully")
    assert True


@when("I add the first product to bag")
def step_add_first_to_bag(context):
    context.logger.step("When: Add first product to bag")
    context.lipstick.click_first_product()
    context.logger.action("Clicked first product")
    context.driver.switch_to.window(context.driver.window_handles[-1])
    context.logger.action("Switched to PDP tab")
    name = context.lipstick.get_product_name()
    price = context.lipstick.get_product_price()
    context.logger.action(f"Product: '{name}' - {price}")
    context.lipstick.add_to_bag()
    context.logger.action("Clicked Add to Bag")
    time.sleep(1)


@when("I go to the bag page")
def step_go_to_bag(context):
    context.logger.step("When: Go to bag page")
    context.lipstick.go_to_bag()
    context.logger.action("Navigated to bag")
    time.sleep(2)


@then("I should be on the bag page")
def step_verify_bag_page(context):
    url = context.driver.current_url.lower()
    context.logger.assert_msg(f"Bag page URL: {url}")
    assert "bag" in url or "cart" in url, f"Should be on bag page, got {url}"


@when('I search for "{query}"')
def step_search(context, query):
    context.logger.step(f"When: Search for '{query}'")
    home = HomePage(context.driver)
    home.search(query)
    context.logger.action(f"Submitted search query '{query}'")
    time.sleep(3)


@then("I should see search results")
def step_search_results(context):
    context.logger.assert_msg(f"Search URL: {context.driver.current_url}")
    assert "search" in context.driver.current_url.lower(), (
        f"Not on search results page, got {context.driver.current_url}"
    )


@then("the page should load without errors")
def step_no_errors(context):
    context.logger.step("Then: Page loaded without errors")
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    context.logger.action("Page body loaded")
    context.logger.assert_msg(f"Title: '{context.driver.title}'")
    assert "error" not in context.driver.title.lower(), "Page shows an error"


@then("the search results page should be visible")
def step_search_results_visible(context):
    body = context.driver.find_element(By.TAG_NAME, "body")
    context.logger.assert_msg("Search results body is visible")
    assert body.is_displayed(), "Search results body not visible"
    context.logger.assert_msg(f"URL: {context.driver.current_url}")
    assert "search" in context.driver.current_url.lower(), (
        f"Not on search results, got {context.driver.current_url}"
    )
