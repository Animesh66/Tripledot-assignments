import allure
import pytest
from allure_commons.types import AttachmentType
from appium import webdriver
from appium.webdriver.appium_service import AppiumService

APPIUM_PORT = 4723  # This is the default port where the appium will be started.
APPIUM_HOST = '127.0.0.1' # This is the default host where we want to run appium server.

"""
This confitest.py file is a globally accessible file by pytest framework. We are writing the setup and tear-down methods in this file and call 
this fixtures(pytest) in a test method to reduce code duplication.
"""

@pytest.fixture(scope='class')
def appium_driver(request):
    """
    Fixture to start appium and launch the app
    :param request: take the request as a parameters
    :return: returns the driver object 
    """
    appium_service = AppiumService()
    appium_service.start(args=['--address', APPIUM_HOST, '-p', str(APPIUM_PORT)], timeout_ms=20000) # Passing aorgument to start the appium server on default port and default host.
    print(appium_service.is_running)
    desired_caps = dict(
        platformName='Android',
        platformVersion='13',
        deviceName='Galaxy S23 Ultra',
        appPackage='com.secretescapes.mobile',
        appActivity='com.secretescapes.android.main.MainActivity',
        udid='R3CW1062Q3M'
    )
    driver = webdriver.Remote(f'http://{APPIUM_HOST}:{APPIUM_PORT}/wd/hub',
                              desired_capabilities=desired_caps)
    request.cls.driver = driver
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
    appium_service.stop()
    print(appium_service.is_running)


