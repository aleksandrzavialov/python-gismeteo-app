import allure
import pytest
from selene.support.shared import browser
from appium import webdriver
from python_gismeteo_mobile.utils.allure.attach import attach_video, add_screenshot
import config


@pytest.fixture(scope='function', autouse=True)
def driver_management():
    browser.config.timeout = config.settings.timeout
    with allure.step('Set up app session'):
        browser.config.driver = webdriver.Remote(
            config.settings.remote_url, options=config.settings.driver_options
        )

    yield
    with allure.step('Closing session'):
        if config.settings.run_on_browserstack:
            attach_video(browser)
            add_screenshot(browser)

        browser.quit()
