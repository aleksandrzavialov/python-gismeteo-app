import time

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
        browser.element((AppiumBy.CSS_SELECTOR, '.android.widget.TextView:nth-child(1)')).click()

    with step("Verify content found"):
        browser.element((AppiumBy.ID, 'ru.gismeteo.gismeteo:id/text_location_name')).element((AppiumBy.CSS_SELECTOR, '.android.widget.TextView')).should(have.text('Moscow'))
        browser.element((AppiumBy.ID, 'ru.gismeteo.gismeteo:id/tbLocationsDetailsAction')).should(be.visible)
        browser.element((AppiumBy.ID, 'ru.gismeteo.gismeteo:id/text_date')).should(be.visible)
        browser.element((AppiumBy.ID, 'ru.gismeteo.gismeteo:id/sunProgress')).should(be.visible)
        browser.element((AppiumBy.ID, 'ru.gismeteo.gismeteo:id/text_weather_and_wind_descr')).should(be.visible)
        browser.element((AppiumBy.ID, 'ru.gismeteo.gismeteo:id/weatherBitmapViewHourly')).should(be.visible)
        browser.element((AppiumBy.ID, 'ru.gismeteo.gismeteo:id/gistTemperatureHourly')).should(be.visible)