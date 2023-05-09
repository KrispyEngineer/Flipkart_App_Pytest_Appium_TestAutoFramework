import time

import pytest

from PageObjects.ElectronicsPage import HomePage
from TestCases.BaseTest import BaseTest
from Utilities.DataLoadUtil import DataLoadUtil


class Test_search_electronics(BaseTest):

    def test_flipkart(self, get_data):
        elec = HomePage(self.driver)
        elec.search_electronics(get_data)

    @pytest.fixture(params=DataLoadUtil.data_load('Electronics'))
    def get_data(self, request):
        return request.param
