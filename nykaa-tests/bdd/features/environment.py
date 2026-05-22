import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from utils import save_screenshot, take_screenshot, TestLogger


def before_all(context):
    context.logger = TestLogger("bdd_nykaa")


def before_scenario(context, scenario):
    context.logger.info(f"=== Scenario: {scenario.name} ===")

    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service, options=options)
    context.driver.set_page_load_timeout(5)
    try:
        context.driver.get("https://www.nykaa.com")
    except Exception:
        context.driver.execute_script("window.stop();")
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.logo"))
    ).click()
    context.logger.action("Browser started and Nykaa homepage loaded")


def after_scenario(context, scenario):
    scenario_name = scenario.name.replace(" ", "_").lower()
    save_screenshot(context.driver, f"bdd_{scenario_name}")

    if scenario.status == "failed":
        take_screenshot(context.driver, f"{scenario_name}_failed")
        context.logger.info(f"=== Scenario FAILED: {scenario.name} ===")
    else:
        context.logger.info(f"=== Scenario PASSED: {scenario.name} ===")

    context.driver.quit()
    context.logger.action("Browser closed")


def after_all(context):
    context.logger.attach_to_allure("bdd_test_log")
    context.logger.info("All BDD scenarios completed")
