from appium.webdriver.common.appiumby import AppiumBy


class ScrollUtil:

    @staticmethod
    def ScrolltoText(text, driver):
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                            "new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains(\""+text+"\").instance(0))").click()

    @staticmethod
    def ScrollUp(NumberofTimes, driver):
        for i in range(NumberofTimes):
            driver.swipe(800, 2000, 800, 700, 1000)

    @staticmethod
    def ScrollUDown(NumberofTimes, driver):
        for i in range(NumberofTimes):
            driver.swipe(800, 900, 800, 2000, 1000)

    @staticmethod
    def SwipeLeft(NumberofTimes, driver):
        for i in range(NumberofTimes):
            driver.swipe(900, 1400, 300, 1400, 500)

    @staticmethod
    def SwipeRight(NumberofTimes, driver):
        for i in range(NumberofTimes):
            driver.swipe(300, 1400, 900, 1400, 500)
