import time

import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

from PageObjects.GroceriesPage import GroceriesPage
from TestCases.BaseTest import BaseTest
from Utilities.DataLoadUtil import DataLoadUtil


class Test_Groceries(BaseTest):

    def test_Groceries(self, get_data):
        groceries = GroceriesPage(self.driver)
        groceries.search_Groceries(get_data)

    @pytest.fixture(params= DataLoadUtil.data_load('Groceries'))
    def get_data(self, request):
        return request.param