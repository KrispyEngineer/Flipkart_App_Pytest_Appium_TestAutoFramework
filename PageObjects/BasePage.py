from appium.webdriver.common.appiumby import AppiumBy

from Utilities.ConfigReaderUtil import ConfReader
from Utilities.LogUtil import Logger

log = Logger.get_Logger()
class BasePage:


    def __init__(self,driver):
        self.driver = driver

    def click(self,locator):
        if str(locator).endswith('_ID'):
            self.driver.find_element(AppiumBy.ID, ConfReader.get_config('locator', locator)).click()
        elif str(locator).endswith('_XPATH'):
            self.driver.find_element(AppiumBy.XPATH, ConfReader.get_config('locator', locator)).click()
        elif str(locator).endswith('_ACCESSIBILITY_ID'):
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, ConfReader.get_config('locator', locator)).click()
        log.info("Clicking on locator" + str(locator))

    def type(self,locator,value):
        if str(locator).endswith('_ID'):
            self.driver.find_element(AppiumBy.ID, ConfReader.get_config('locator', locator)).send_keys(value)
        elif str(locator).endswith('_XPATH'):
            self.driver.find_element(AppiumBy.XPATH, ConfReader.get_config('locator', locator)).send_keys(value)
        elif str(locator).endswith('_ACCESSIBILITY_ID'):
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, ConfReader.get_config('locator', locator)).send_keys(value)
        log.info("Sending inpuut keys to element" + str(locator) + "Entered the value as, " + str(value))

    def get_text(self,locator):
        if str(locator).endswith('_ID'):
            text = self.driver.find_element(AppiumBy.ID, ConfReader.get_config('locator', locator)).text
        elif str(locator).endswith('_XPATH'):
            text = self.driver.find_element(AppiumBy.XPATH, ConfReader.get_config('locator', locator)).text
        elif str(locator).endswith('_ACCESSIBILITY_ID'):
            text = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, ConfReader.get_config('locator', locator)).text
        log.info("Getting text from selected locator" + str(locator))
        return text