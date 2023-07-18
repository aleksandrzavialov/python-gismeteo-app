import allure
from allure_commons.types import AttachmentType
from python_gismeteo_mobile.utils.browserstack.get_attach import get_video_url


def attach_video(browser):
    video_url = f'{get_video_url(browser.driver.session_id)}'
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, 'Video_' + browser.driver.session_id, AttachmentType.HTML, '.html')


def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='Last screenshot', attachment_type=AttachmentType.PNG, extension='.png')

