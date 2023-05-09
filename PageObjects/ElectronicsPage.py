from PageObjects.BasePage import BasePage
from Utilities.ScrollUtil import ScrollUtil


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def search_electronics(self, device):
        self.click("search_btn_XPATH")
        self.type("type_search_XPATH", device[0])
        self.click("select_product_XPATH")
        ScrollUtil.ScrolltoText(device[1],self.driver)
