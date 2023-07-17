import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import have, be
from selene.support.shared import browser
from allure_commons.types import Severity
from allure import step


@allure.tag("ui", "mobile")
@allure.label('owner', 'Aleksandr Zavialov')
@allure.feature('UI')
@allure.story('Search')
@allure.severity(Severity.BLOCKER)
@allure.title('Search for a city')
def test_search_city():
    with step("Search for a city"):
        browser.element((AppiumBy.ID, "ru.gismeteo.gismeteo:id/action_search")).click()
        browser.element((AppiumBy.ID, "ru.gismeteo.gismeteo:id/search_src_text")).type('Moscow')
        browser.element((AppiumBy.CSS_SELECTOR, '.android.widget.TextView:nth-child(1)')).should(have.text('Moscow')).click()  # move to method like search
    with step("Verify content of filtered city"):
        browser.element((AppiumBy.ID, 'ru.gismeteo.gismeteo:id/text_location_name')).element((AppiumBy.CSS_SELECTOR, '.android.widget.TextView')).should(have.text('Moscow'))
        browser.element((AppiumBy.ID, 'ru.gismeteo.gismeteo:id/tbLocationsDetailsAction')).should(be.visible)
        browser.element((AppiumBy.ID, 'ru.gismeteo.gismeteo:id/text_date')).should(be.visible)
        browser.element((AppiumBy.ID, 'ru.gismeteo.gismeteo:id/sunProgress')).should(be.visible)
        browser.element((AppiumBy.ID, 'ru.gismeteo.gismeteo:id/text_weather_and_wind_descr')).should(be.visible)
        browser.element((AppiumBy.ID, 'ru.gismeteo.gismeteo:id/weatherBitmapViewHourly')).should(be.visible)
        browser.element((AppiumBy.ID, 'ru.gismeteo.gismeteo:id/gistTemperatureHourly')).should(be.visible)


def test_manage_favorite():
    with step("Open favorite menu"):
        browser.element((AppiumBy.XPATH, '//*[contains(@text,"FAVORITES")]')).click()
        browser.element((AppiumBy.ID, "ru.gismeteo.gismeteo:id/fabAdd")).click()
        browser.element((AppiumBy.ID, "ru.gismeteo.gismeteo:id/search_src_text")).type('Paris') # move to method like search
        browser.element((AppiumBy.CSS_SELECTOR, '.android.widget.TextView')).should(have.text('Paris')).click() # move to method like searc
    with step("Verify added favorite"):
        browser.element((AppiumBy.ID, 'ru.gismeteo.gismeteo:id/text_header')).should(have.text('My locations'))
        browser.element((AppiumBy.ID, 'ru.gismeteo.gismeteo:id/text_location_name')).should(have.text('Paris'))
    with step('Delete favorite'):
        browser.element((AppiumBy.ID, 'ru.gismeteo.gismeteo:id/text_location_name')).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'More options')).click()
        browser.element((AppiumBy.XPATH, '//*[contains(@text,"Remove from favorites")]')).click()
    with step('Check that no favorites appear on the main page'):
        browser.element((AppiumBy.XPATH, '//*[contains(@text,"FAVORITES")]')).should(be.visible)
        browser.element((AppiumBy.ID, 'ru.gismeteo.gismeteo:id/text_header')).should(be.not_.visible)


def test_check_share_options():
    with step("Open share menu"):
        browser.element((AppiumBy.CSS_SELECTOR, '.android.widget.ImageView')).click()
        browser.element((AppiumBy.XPATH, '//android.widget.LinearLayout[1]')).click()
    with step("Check share options"):
        browser.element((AppiumBy.ID, 'android:id/title')).should(have.text('Share'))
        browser.all((AppiumBy.ID, 'android:id/text1')).should(have.size(3))


def test_change_language_settings():
    with step("Open language settings"):
        browser.element((AppiumBy.CSS_SELECTOR, '.android.widget.ImageView')).click()
        browser.element((AppiumBy.XPATH, '//android.widget.LinearLayout[3]')).click()
    with step("Change language to Russian"):
        browser.element((AppiumBy.XPATH, '//*[contains(@text,"Language")]')).click()
        browser.element((AppiumBy.XPATH, '//*[contains(@text,"Русский")]')).click()
    with step('Check changes on main page'):
        browser.driver.back()
        browser.element((AppiumBy.XPATH, '//*[contains(@text,"ПОБЛИЗОСТИ")]')).should(be.visible)


def test_deny_request_access():
    with step("Open permissions dialog"):
        browser.element((AppiumBy.XPATH, '//*[contains(@text,"NEARBY")]')).click()
        browser.element((AppiumBy.ID, 'ru.gismeteo.gismeteo:id/btnEnableLocationRequest')).click()
    with step("Check permission options"):
        browser.element((AppiumBy.ID, 'com.android.permissioncontroller:id/permission_message')).should(
            have.text('Allow Gismeteo to access this device’s location?'))
        browser.all((AppiumBy.CSS_SELECTOR, '.android.widget.Button')).should(have.texts('While using the app', 'Only this time', 'Deny'))

