import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import wait

from tests.conftest import getDataFromFixture
from utilities.BaseClass import BaseClass
from PageObjects.DetailsPage import detailsclass

@pytest.mark.usefixtures("getDataFromFixture")
class TestForm(BaseClass):

    def test_addDetails(self, getDataFromFixture):
        log = self.getLogger()
        details = detailsclass(self.driver)
        log.debug("calling getData()")
        details.getData(getDataFromFixture)


