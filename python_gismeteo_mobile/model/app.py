from selene import be
from selene.support.shared import browser
from appium.webdriver.common.appiumby import AppiumBy


def given_request_access():
    if browser.element((AppiumBy.ID, 'selector')).matching(be.visible):
        browser.element((AppiumBy.ID, 'selector')).click()