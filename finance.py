import os
import json
from urllib.parse import urlencode
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class yahooFinance(object):
    def get_login(self):
        login_url = 'https://login.yahoo.com/'
        try:
            params = {'username': 'Eric.D.Grey@Outlook.com', 'acrumb':'PdKl6txY', 'sessionIndex': 'RA--',
                      'persistent': 'y', 'password': 'QCwbigGc7YjdqVE'}
            headers = {
                'content-type': 'application/x-www-form-urlencoded',
                'X-Requested-With': 'XMLHttpRequest',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/80.0.3987.87 Safari/537.36',
                
            }
            resp = requests.post(login_url, params=urlencode(params), headers=headers)
            resp
        except Exception as e:
            print(e)
        return
    
    def selenium_login(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        self.driver = webdriver.Chrome(executable_path='D:\Source\chromedriver\chromedriver.exe',
                                       chrome_options=options)
        self.driver.get('https://login.yahoo.com')
        emailElem = self.driver.find_element_by_id('login-username')
        emailElem.send_keys('Eric.D.Grey@Outlook.com')
        loginbtn = self.driver.find_element_by_id("login-signin")
        loginbtn.click()
    
        passwordElem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "login-passwd"))
        )
        passwordElem.send_keys('QCwbigGc7YjdqVE')
        submitBtn = self.driver.find_element_by_id("login-signin")
        submitBtn.click()
        self.driver
def main(event, context):
    y = yahooFinance()
    # y.get_login()
    y.selenium_login()

if __name__ == "__main__":
    main(0, 0)