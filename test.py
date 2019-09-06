from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import sys

import unittest, time, re

class Sel(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver-win.exe')
        self.driver.implicitly_wait(30)
        self.base_url = "https://marketplace.fourhands.com/login"
        self.verificationErrors = []
        self.accept_next_alert = True
    def test_sel(self):
        driver = self.driver
        delay = 3
        driver.get(self.base_url)
        username = driver.find_element_by_id("p_lt_zoneContent_Marketplace_LogonForm_logonFormInner_LogonForm_loginElem_UserName")
        password = driver.find_element_by_id("p_lt_zoneContent_Marketplace_LogonForm_logonFormInner_LogonForm_loginElem_Password")
        username.send_keys("75839")
        password.send_keys("Success7")
        driver.find_element_by_id("p_lt_zoneContent_Marketplace_LogonForm_logonFormInner_LogonForm_loginElem_btnLogon").click()
        time.sleep(4)
        driver.get("https://marketplace.fourhands.com/new")
        # Selenium script to scroll to the bottom, wait 3 seconds for the next batch of data to load, then continue scrolling.  It will continue to do this until the page stops loading new data.
        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        match=False
        while(match==False):
            lastCount = lenOfPage
            time.sleep(4)
            lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
            if lastCount==lenOfPage:
                match=True
        html_source = driver.page_source
        data = html_source.encode('utf-8')
        print(data)

if __name__ == "__main__":
    unittest.main()
