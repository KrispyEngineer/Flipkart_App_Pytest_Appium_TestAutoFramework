from PageObjects.BasePage import BasePage
from Utilities.ScrollUtil import ScrollUtil


class GroceriesPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    def search_Groceries(self,items):
        self.click("groceries_btn_XPATH")
        self.click("search_grc_XPATH")
        self.type("type_grc_XPATH",items[0])
        self.click("click_prdct_XPATH")
        ScrollUtil.ScrolltoText(items[1],self.driver)
        ele_text = self.get_text("validate_XPATH")
        assert items[2] in ele_text