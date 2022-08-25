import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import wait
from selenium.webdriver.support.select import Select
from utilities.BaseClass import BaseClass

class detailsclass(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    name = (By.CSS_SELECTOR, "input[name*='name']")
    email = (By.CSS_SELECTOR, "input[name*='email']")
    pw = (By.CSS_SELECTOR, "input[type*='password']")
    chkbx = (By.XPATH, "//input[@type='checkbox']")
    empstatus = (By.XPATH, "//input[@value='option3']")
    dob = (By.XPATH, "//input[@type='date']")
    submit = (By.CSS_SELECTOR, "input[type*='submit']")
    alert = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

#we have globally declared getDataFromFixture but explicitly passing it as an argument since the fixture is returning values/data
    @pytest.mark.xfail
    def getData(self, getFixtureData):
        logger = self.getLogger()
        name = self.driver.find_element(*detailsclass.name)
        names = getFixtureData
        name.send_keys(names)
        self.driver.find_element(*detailsclass.email).send_keys("vilasanr@amazon.com")
        self.driver.find_element(*detailsclass.pw).send_keys("abc123")
        self.driver.find_element(*detailsclass.chkbx).click()
        selobj = Select(self.driver.find_element(By.TAG_NAME, "Select"))
        selobj.select_by_visible_text("Female")
        logger.debug("selecting emp status")
        empstatus = self.driver.find_element(*detailsclass.empstatus)
        empstatus.click()
        logger.info("Verifying using assert if employment status has been selected")
        logger.debug("assert statement evaluation")
        dob = self.driver.find_element(*detailsclass.dob)
        dob.send_keys("07-24-1995")
        self.driver.find_element(*detailsclass.submit).click()
        alertmsg = self.driver.find_element(*detailsclass.alert).text
        assert alertmsg == "Success! The Form has been submitted successfully!."
        assert empstatus.is_selected()








