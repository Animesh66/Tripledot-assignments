import logging
from Utilities.logging_utility import Logger
from Utilities.config_reader import config_reader
import time
from appium.webdriver.common.appiumby import AppiumBy

log = Logger(__name__, logging.INFO)


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        if str(locator).endswith("_xpath"):
            self.driver.find_elemen(by=AppiumBy.XPATH, value=config_reader("locators", locator)).clear()
            self.driver.find_elemen(by=AppiumBy.XPATH, value=config_reader("locators", locator)).click()

        elif str(locator).endswith("_id"):
            self.driver.find_element(by=AppiumBy.ID, value=config_reader("locators", locator)).clear()
            self.driver.find_element(by=AppiumBy.ID, value=config_reader("locators", locator)).click()

        elif str(locator).endswith("_class"):
            self.driver.find_element(by=AppiumBy.CLASS_NAME, value=config_reader("locators", locator)).clear()
            self.driver.find_element(by=AppiumBy.CLASS_NAME, value=config_reader("locators", locator)).click()

        elif str(locator).endswith("_uiautomator"):
            self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=config_reader("locators", f"{locator}")).clear()
            self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=config_reader("locators", f"{locator}")).click()

        log.logger.info("Clicking on the element: " + str(locator))

    def click_index(self, locator, index):
        if str(locator).endswith("_xpath"):
            self.driver.find_elements(by=AppiumBy.XPATH, value=config_reader("locators", locator))[index].click()

        elif str(locator).endswith("_id"):
            self.driver.find_elements(by=AppiumBy.ID, value=config_reader("locators", locator))[index].click()

        elif str(locator).endswith("_class"):
            self.driver.find_elements(by=AppiumBy.CLASS_NAME, value=config_reader("locators", locator))[index].click()

        elif str(locator).endswith("_uiautomator"):
            self.driver.find_elements(by=AppiumBy.ANDROID_UIAUTOMATOR, value=config_reader("locators", f"{locator}"))[index].click()

        log.logger.info("Clicking on the element: " + str(locator) + " with index " + str(index))

    def type(self, locator, data):
        if str(locator).endswith("_xpath"):
            self.driver.find_element(by=AppiumBy.XPATH, value=config_reader("locators", locator)).send_keys(data)

        elif str(locator).endswith("_id"):
            self.driver.find_element(by=AppiumBy.ID, value=config_reader("locators", locator)).send_keys(data)

        elif str(locator).endswith("_class"):
            self.driver.find_element(by=AppiumBy.CLASS_NAME, value=config_reader("locators", locator)).send_keys(data)

        elif str(locator).endswith("_uiautomator"):
            self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=config_reader("locators", f"{locator}")).send_keys(data)

        log.logger.info("Typing on the element: " + str(locator) + " entered the value as: " + str(data))

    def get_text(self, locator):
        if str(locator).endswith("_xpath"):
            text = self.driver.find_element(by=AppiumBy.XPATH, value=config_reader("locators", locator)).text

        elif str(locator).endswith("_id"):
            text = self.driver.find_element(by=AppiumBy.ID, value=config_reader("locators", locator)).text

        elif str(locator).endswith("_class"):
            text = self.driver.find_element(by=AppiumBy.CLASS_NAME, value=config_reader("locators", locator)).text

        elif str(locator).endswith("_uiautomator"):
            text = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=config_reader("locators", f"{locator}")).text

        log.logger.info("Getting text from an element: " + str(locator))
        return text

    def hide_keyboard(self):
        self.driver.hide_keyboard()

    def static_wait(self, no_of_sec):
        time.sleep(no_of_sec)
