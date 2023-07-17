import pydantic
from appium.options.android import UiAutomator2Options
from typing import Optional

from python_gismeteo_mobile import utils
from python_gismeteo_mobile.utils import file


class Settings(pydantic.BaseSettings):
    context = 'emulation'

    # --- Appium Capabilities ---
    platformName: str = None
    platformVersion: str = None
    deviceName: str = None
    app: Optional[str] = None
    appName: Optional[str] = None
    appWaitActivity: Optional[str] = None
    newCommandTimeout: Optional[int] = 60
    udid: Optional[str] = None

    # --- > BrowserStack Capabilities ---
    projectName: Optional[str] = None
    buildName: Optional[str] = None
    sessionName: Optional[str] = None
    # --- > > BrowserStack credentials---
    userName: Optional[str] = pydantic.Field(None, env='browserstack.userName')
    accessKey: Optional[str] = pydantic.Field(None, env='browserstack.accessKey')

    # --- Remote Driver ---
    remote_url: str = 'http://127.0.0.1:4723/wd/hub'  # it's a default appium server url

    # --- Selene ---
    timeout: float = 6.0


    @property
    def driver_options(self):
        options = UiAutomator2Options()
        if self.deviceName:
            options.device_name = self.deviceName
        if self.platformName:
            options.platform_name = self.platformName
        options.app = (
            utils.file.abs_path_from_project(self.app)
            if self.app and (self.app.startswith('./') or self.app.startswith('../'))
            else self.app
        )
        options.new_command_timeout = self.newCommandTimeout
        if self.udid:
            options.udid = self.udid
        if self.appWaitActivity:
            options.app_wait_activity = self.appWaitActivity

        return options

    @classmethod
    def in_context(cls) -> 'Settings':
        """
        factory method to init Settings with values from corresponding .env file
        """
        #asked_or_current = env or cls().context
        return cls(
            _env_file=utils.file.abs_path_from_project(
                #f'config.{asked_or_current}.env'
                'config.env'
            )
        )


settings = Settings.in_context()

