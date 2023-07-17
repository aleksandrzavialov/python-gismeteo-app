import allure
import pytest
from selene.support.shared import browser
from selene import be
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

import config


@pytest.fixture(scope='function', autouse=True)
def driver_management(request):

    browser.config.timeout = config.settings.timeout
    with allure.step('set up app session'):
        browser.config.driver = webdriver.Remote(
            config.settings.remote_url, options=config.settings.driver_options
        )

    yield
    return_to_main()
    return_english_from_russian()


def return_to_main():
    while browser.element((AppiumBy.ID, 'ru.gismeteo.gismeteo:id/action_search')).matching(be.not_.visible):
        browser.driver.back()


def return_english_from_russian():
    if browser.element((AppiumBy.XPATH, '//*[contains(@text,"ПОБЛИЗОСТИ")]')).matching(be.visible):
        browser.element((AppiumBy.CSS_SELECTOR, '.android.widget.ImageView')).click()
        browser.element((AppiumBy.XPATH, '//android.widget.LinearLayout[3]')).click()
        browser.element((AppiumBy.XPATH, '//*[contains(@text,"Язык")]')).click()
        browser.element((AppiumBy.XPATH, '//*[contains(@text,"English")]')).click()
        return_to_main()

