import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import have, be
from selene.support.shared import browser
from allure_commons.types import Severity


@allure.tag('UI', 'mobile')
@allure.label('owner', 'Aleksandr Zavialov')
@allure.feature('UI')
@allure.severity(Severity.BLOCKER)
@allure.title('Search for a city')
@allure.story('Search')
def test_search_city():
    with allure.step('Search for a city'):
        browser.element((AppiumBy.ID, 'ru.gismeteo.gismeteo:id/action_search')).click()
        browser.element((AppiumBy.ID, 'ru.gismeteo.gismeteo:id/search_src_text')).type('Moscow')
        browser.element((AppiumBy.ID, 'ru.gismeteo.gismeteo:id/text_location_name')).should(have.text('Moscow')).click()

    with allure.step('Verify content of filtered city'):
        browser.element((AppiumBy.ID, 'ru.gismeteo.gismeteo:id/text_location_name')).element((AppiumBy.XPATH, '//android.widget.TextView')).should(have.text('Moscow'))
        browser.element((AppiumBy.ID, 'ru.gismeteo.gismeteo:id/tbLocationsDetailsAction')).should(be.visible)
        browser.element((AppiumBy.ID, 'ru.gismeteo.gismeteo:id/text_date')).should(be.visible)
        browser.element((AppiumBy.ID, 'ru.gismeteo.gismeteo:id/sunProgress')).should(be.visible)
        browser.element((AppiumBy.ID, 'ru.gismeteo.gismeteo:id/text_weather_and_wind_descr')).should(be.visible)
        browser.element((AppiumBy.ID, 'ru.gismeteo.gismeteo:id/weatherBitmapViewHourly')).should(be.visible)
        browser.element((AppiumBy.ID, 'ru.gismeteo.gismeteo:id/gistTemperatureHourly')).should(be.visible)


@allure.tag('UI', 'mobile')
@allure.label('owner', 'Aleksandr Zavialov')
@allure.feature('UI')
@allure.severity(Severity.CRITICAL)
@allure.title('Set up application language')
@allure.story('Settings')
def test_change_language_settings():
    with allure.step('Open language settings'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'More options')).click()
        browser.element((AppiumBy.XPATH, '//android.widget.LinearLayout[3]')).click()

    with allure.step('Change language to Russian'):
        browser.element((AppiumBy.XPATH, '//*[contains(@text,"Language")]')).click()
        browser.element((AppiumBy.XPATH, '//*[contains(@text,"Русский")]')).click()

    with allure.step('Check changes on main page'):
        browser.driver.back()
        browser.element((AppiumBy.XPATH, '//*[contains(@text,"ПОБЛИЗОСТИ")]')).should(be.visible)


@allure.tag('UI', 'mobile')
@allure.label('owner', 'Aleksandr Zavialov')
@allure.feature('UI')
@allure.severity(Severity.CRITICAL)
@allure.title('Set up permissions')
@allure.story('Settings')
def test_deny_request_access():
    with allure.step('Open permissions dialog'):
        browser.element((AppiumBy.XPATH, '//*[contains(@text,"NEARBY")]')).click()
        browser.element((AppiumBy.ID, 'ru.gismeteo.gismeteo:id/btnEnableLocationRequest')).click()

    with allure.step('Check permission options'):
        browser.element((AppiumBy.ID, 'com.android.permissioncontroller:id/permission_message')).should(
            have.text('Allow Gismeteo to access this device’s location?'))
        browser.element((AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_foreground_only_button')).should(have.text('While using the app'))
        browser.element((AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_one_time_button')).should(have.text('Only this time'))
        browser.element((AppiumBy.ID, 'com.android.permissioncontroller:id/permission_deny_button')).should(have.text('Deny'))


@allure.tag('UI', 'mobile')
@allure.label('owner', 'Aleksandr Zavialov')
@allure.feature('UI')
@allure.severity(Severity.NORMAL)
@allure.title('Set and unset city as a favorite')
@allure.story('Favorite')
def test_manage_favorite():
    with allure.step('Open favorite menu'):
        browser.element((AppiumBy.XPATH, '//*[contains(@text,"FAVORITES")]')).click()
        browser.element((AppiumBy.ID, 'ru.gismeteo.gismeteo:id/fabAdd')).click()
        browser.element((AppiumBy.ID, 'ru.gismeteo.gismeteo:id/search_src_text')).type('Paris')
        browser.element((AppiumBy.XPATH, '//android.widget.LinearLayout[1]/android.widget.TextView[1]')).should(have.text('Paris')).click()

    with allure.step('Verify added favorite'):
        browser.element((AppiumBy.ID, 'ru.gismeteo.gismeteo:id/text_header')).should(have.text('My locations'))
        browser.element((AppiumBy.ID, 'ru.gismeteo.gismeteo:id/text_location_name')).should(have.text('Paris'))

    with allure.step('Delete favorite'):
        browser.element((AppiumBy.ID, 'ru.gismeteo.gismeteo:id/text_location_name')).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'More options')).click()
        browser.element((AppiumBy.XPATH, '//*[contains(@text,"Remove from favorites")]')).click()

    with allure.step('Check that no favorites appear on the main page'):
        browser.element((AppiumBy.XPATH, '//*[contains(@text,"FAVORITES")]')).should(be.visible)
        browser.element((AppiumBy.ID, 'ru.gismeteo.gismeteo:id/text_header')).should(be.not_.visible)


@allure.tag('UI', 'mobile')
@allure.label('owner', 'Aleksandr Zavialov')
@allure.feature('UI')
@allure.severity(Severity.MINOR)
@allure.title('Share application')
@allure.story('Share')
def test_check_share_options():
    with allure.step('Open share menu'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'More options')).click()
        browser.element((AppiumBy.XPATH, '//android.widget.LinearLayout[1]')).click()

    with allure.step('Check share options'):
        browser.element((AppiumBy.ID, 'android:id/title')).should(have.text('Share'))
        browser.all((AppiumBy.ID, 'android:id/text1')).should(have.size(3))
