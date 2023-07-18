from selene import be
from selene.support.shared import browser
from appium.webdriver.common.appiumby import AppiumBy


def given_request_access():
    if browser.element((AppiumBy.ID, 'selector')).matching(be.visible):
        browser.element((AppiumBy.ID, 'selector')).click()


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

