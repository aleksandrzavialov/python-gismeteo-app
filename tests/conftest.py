import allure
import allure_commons
import pytest
from _pytest.nodes import Item
from _pytest.runner import CallInfo
from selene.support.shared import browser
from selene import support
from appium import webdriver

import config
from python_wikipedia_mobile import utils


@pytest.fixture(scope='function', autouse=True)
def driver_management(request):
    browser.config.timeout = config.settings.timeout

    with allure.step('set up app session'):
        browser.config.driver = webdriver.Remote(
            config.settings.remote_url, options=config.settings.driver_options
        )

    yield

    if config.settings.run_on_browserstack:
        utils.allure.attach.screenshot(name='Last screenshot')
        utils.allure.attach.screen_xml_dump()

    session_id = browser.driver.session_id

    allure.step('close app session')(browser.quit)()

    if config.settings.run_on_browserstack:
        utils.allure.attach.video_from_browserstack(session_id)

