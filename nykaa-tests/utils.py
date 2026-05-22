import os
from pathlib import Path

import allure


def take_screenshot(driver, name):
    allure.attach(
        driver.get_screenshot_as_png(),
        name=name,
        attachment_type=allure.attachment_type.PNG,
    )


def save_screenshot(driver, name, subdir="end to end"):
    screenshot_dir = Path(__file__).parent / subdir
    screenshot_dir.mkdir(parents=True, exist_ok=True)
    filepath = screenshot_dir / f"{name}.png"
    driver.save_screenshot(str(filepath))

    allure.attach(
        driver.get_screenshot_as_png(),
        name=name,
        attachment_type=allure.attachment_type.PNG,
    )

    return filepath
