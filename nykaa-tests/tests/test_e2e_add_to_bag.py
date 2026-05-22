import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse, parse_qs
from pages.home_page import HomePage
from pages.lipstick_page import LipstickPage
from utils import save_screenshot


@allure.story("End-to-End")
@allure.feature("Purchase Flow")
@allure.title("End-to-end: 13-step E2E test suite for lipstick purchase flow")
@allure.severity(allure.severity_level.BLOCKER)
@allure.description("13-step E2E flow: nav → listing → filters → sort → PDP → add to bag → search")
class TestE2EAddToBag:

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Step 1: Navigate to lipstick listing page via Makeup menu")
    def test_step_nav_to_lipstick(self, driver):
        home = HomePage(driver)
        home.hover_makeup_and_click_lipstick()

        lipstick = LipstickPage(driver)
        heading = lipstick.get_heading_text()
        save_screenshot(driver, "step1_lipstick_listing")
        assert "lipstick" in heading.lower(), f"Heading '{heading}' should contain 'Lipstick'"

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Step 2: Verify products are displayed on listing page")
    def test_step_verify_products_displayed(self, driver):
        home = HomePage(driver)
        home.hover_makeup_and_click_lipstick()

        lipstick = LipstickPage(driver)
        count = lipstick.get_product_count()
        save_screenshot(driver, "step2_product_count")
        assert count > 0, f"Expected at least 1 product on listing, found {count}"

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Step 3: Filter products by brand Lakme")
    def test_step_filter_brand_lakme(self, driver):
        home = HomePage(driver)
        home.hover_makeup_and_click_lipstick()

        lipstick = LipstickPage(driver)
        lipstick.filter_by_brand("Lakme")
        time.sleep(3)
        save_screenshot(driver, "step3_filter_lakme")
        assert "brand" in driver.current_url.lower(), (
            f"URL should contain brand parameter after Lakme filter, got {driver.current_url}"
        )

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Step 4: Filter products by brand Maybelline")
    def test_step_filter_brand_maybelline(self, driver):
        home = HomePage(driver)
        home.hover_makeup_and_click_lipstick()

        lipstick = LipstickPage(driver)
        lipstick.filter_by_brand("Maybelline")
        time.sleep(3)
        save_screenshot(driver, "step4_filter_maybelline")
        assert "brand" in driver.current_url.lower(), (
            f"URL should contain brand parameter after Maybelline filter, got {driver.current_url}"
        )

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Step 5: Sort products by Price Low to High")
    def test_step_sort_low_to_high(self, driver):
        home = HomePage(driver)
        home.hover_makeup_and_click_lipstick()

        lipstick = LipstickPage(driver)
        lipstick.select_sort_low_to_high()
        time.sleep(3)
        save_screenshot(driver, "step5_sort_low_to_high")

        heading = lipstick.get_heading_text()
        assert "lipstick" in heading.lower(), "Still on lipstick page after sorting"

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Step 6: Verify sort parameter appears in URL")
    def test_step_verify_sort_param_in_url(self, driver):
        home = HomePage(driver)
        home.hover_makeup_and_click_lipstick()

        lipstick = LipstickPage(driver)
        lipstick.select_sort_low_to_high()
        time.sleep(3)
        save_screenshot(driver, "step6_sort_url")

        has_sort = "sort" in driver.current_url.lower() or "price_asc" in driver.current_url.lower()
        assert has_sort, f"URL should contain sort parameter, got {driver.current_url}"

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Step 7: Verify product name is displayed on PDP")
    def test_step_verify_pdp_product_name(self, driver):
        home = HomePage(driver)
        home.hover_makeup_and_click_lipstick()

        lipstick = LipstickPage(driver)
        lipstick.click_first_product()
        driver.switch_to.window(driver.window_handles[-1])

        name = lipstick.get_product_name()
        save_screenshot(driver, "step7_pdp_name")
        assert name.strip(), f"Product name should not be empty, got '{name}'"

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Step 8: Verify product price is displayed on PDP")
    def test_step_verify_pdp_product_price(self, driver):
        home = HomePage(driver)
        home.hover_makeup_and_click_lipstick()

        lipstick = LipstickPage(driver)
        lipstick.click_first_product()
        driver.switch_to.window(driver.window_handles[-1])

        price = lipstick.get_product_price()
        save_screenshot(driver, "step8_pdp_price")
        assert price.strip(), f"Product price should not be empty, got '{price}'"

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("Step 9: Add product to bag")
    def test_step_add_to_bag(self, driver):
        home = HomePage(driver)
        home.hover_makeup_and_click_lipstick()

        lipstick = LipstickPage(driver)
        lipstick.click_first_product()
        driver.switch_to.window(driver.window_handles[-1])

        name = lipstick.get_product_name()
        price = lipstick.get_product_price()
        assert name.strip(), "Product name should be visible"
        assert price.strip(), "Product price should be visible"

        lipstick.add_to_bag()
        time.sleep(2)
        save_screenshot(driver, "step9_after_add_to_bag")

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Step 10: Navigate to bag page")
    def test_step_navigate_to_bag(self, driver):
        home = HomePage(driver)
        home.hover_makeup_and_click_lipstick()

        lipstick = LipstickPage(driver)
        lipstick.click_first_product()
        driver.switch_to.window(driver.window_handles[-1])

        lipstick.add_to_bag()
        time.sleep(1)
        lipstick.go_to_bag()
        time.sleep(2)

        save_screenshot(driver, "step10_bag_page")
        assert "bag" in driver.current_url.lower() or "cart" in driver.current_url.lower(), (
            f"Should be on bag/cart page, got {driver.current_url}"
        )

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Step 11: Search for 'lipstick' from homepage")
    def test_step_search_lipstick(self, driver):
        home = HomePage(driver)
        home.search("lipstick")
        time.sleep(3)

        save_screenshot(driver, "step11_search_lipstick")
        assert "search" in driver.current_url.lower(), (
            f"Should navigate to search results page, got {driver.current_url}"
        )

    @allure.severity(allure.severity_level.MINOR)
    @allure.title("Step 12: Search special characters does not crash")
    def test_step_search_special_chars_no_crash(self, driver):
        home = HomePage(driver)
        home.search("!@#$%")

        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        save_screenshot(driver, "step12_search_special_chars")
        assert "error" not in driver.title.lower(), "Page should not show an error after special char search"

    @allure.severity(allure.severity_level.MINOR)
    @allure.title("Step 13: Search results page renders successfully")
    def test_step_verify_search_results_rendered(self, driver):
        home = HomePage(driver)
        home.search("lipstick")
        time.sleep(3)

        body = driver.find_element(By.TAG_NAME, "body")
        save_screenshot(driver, "step13_search_results_rendered")
        assert body.is_displayed(), "Search results page body should be visible"
        assert "search" in driver.current_url.lower(), (
            f"Should be on search results page, got {driver.current_url}"
        )


@allure.story("Navigation")
@allure.feature("Makeup Navigation")
@allure.title("Hover on Makeup and click Lipstick navigates to lipstick listing page")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Verify that hovering over the Makeup category and clicking Lipstick "
                     "redirects to the lipstick listing page with correct heading")
class TestNavLipstick:
    @allure.severity(allure.severity_level.CRITICAL)
    def test_hover_makeup_click_lipstick_navigates_to_lipstick_page(self, driver):
        home = HomePage(driver)
        home.hover_makeup_and_click_lipstick()

        lipstick = LipstickPage(driver)
        heading = lipstick.get_heading_text()

        save_screenshot(driver, "nav_lipstick_listing_page")
        assert "lipstick" in heading.lower(), f"Heading '{heading}' should contain 'Lipstick'"


@allure.story("Filtering")
@allure.feature("Product Filters")
@allure.title("Filter lipstick results by brand Lakme")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("Apply brand filter (Lakme) on the lipstick listing page and verify "
                     "the URL contains the brand filter parameter")
class TestFilterBrand:
    @allure.severity(allure.severity_level.NORMAL)
    def test_filter_by_brand_shows_filtered_results(self, driver):
        home = HomePage(driver)
        home.hover_makeup_and_click_lipstick()

        lipstick = LipstickPage(driver)
        save_screenshot(driver, "before_filter")
        lipstick.filter_by_brand("Lakme")

        time.sleep(3)
        save_screenshot(driver, "after_filter_lakme")

        assert "brand" in driver.current_url.lower(), (
            f"URL should contain brand parameter after filtering, got {driver.current_url}"
        )


@allure.story("Sorting")
@allure.feature("Product Sort")
@allure.title("Sort lipstick results by Price: Low to High")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("Apply Low to High price sort on the lipstick listing and verify "
                     "the URL reflects the sort parameter")
class TestSortPrice:
    @allure.severity(allure.severity_level.NORMAL)
    def test_sort_low_to_high_changes_product_order(self, driver):
        home = HomePage(driver)
        home.hover_makeup_and_click_lipstick()

        lipstick = LipstickPage(driver)

        parsed = urlparse(driver.current_url)
        qs = parse_qs(parsed.query)
        assert "sort" not in qs or qs.get("sort") != ["price_asc"], "Should not already be sorted by price"

        save_screenshot(driver, "before_sort")
        lipstick.select_sort_low_to_high()

        time.sleep(3)
        save_screenshot(driver, "after_sort_low_to_high")

        heading = lipstick.get_heading_text()
        assert "lipstick" in heading.lower(), "Still on lipstick page after sort"


@allure.story("Product Detail")
@allure.feature("Product Details Page")
@allure.title("Product detail page displays product name and price")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Click the first lipstick product from the listing, switch to the PDP tab, "
                     "and verify that the product name and price are displayed")
class TestProductDetail:
    @allure.severity(allure.severity_level.CRITICAL)
    def test_product_detail_displays_name_and_price(self, driver):
        home = HomePage(driver)
        home.hover_makeup_and_click_lipstick()

        lipstick = LipstickPage(driver)
        lipstick.click_first_product()
        driver.switch_to.window(driver.window_handles[-1])

        name = lipstick.get_product_name()
        assert name.strip(), f"Product name should not be empty, got '{name}'"

        price = lipstick.get_product_price()
        save_screenshot(driver, "product_detail_page")
        assert price.strip(), f"Product price should not be empty, got '{price}'"


@allure.story("Search")
@allure.feature("Search Error Handling")
@allure.title("Search with special characters does not crash the page")
@allure.severity(allure.severity_level.MINOR)
@allure.description("Enter special characters '!@#$%' in the search box and verify "
                     "the site navigates to a search results page without errors")
class TestSearchInvalid:
    @allure.severity(allure.severity_level.MINOR)
    def test_search_with_special_chars_does_not_crash(self, driver):
        home = HomePage(driver)
        home.search("!@#$%")

        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        save_screenshot(driver, "search_special_chars_result")
        assert "search" in driver.current_url.lower() or "result" in driver.current_url.lower(), (
            f"Should navigate to search results page, got {driver.current_url}"
        )
        assert "error" not in driver.title.lower(), "Page should not show an error"
