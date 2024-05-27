from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


from keywords.keywords import WebKeys
from locate.loginPage import *
import time


class LoginPage(WebKeys):
    def login(self, url, username, password):
        self.open(url)
        # 实例化wait
        wait = WebDriverWait(self.driver, 20)

        # 等待登录按钮可见
        but_login =(By.XPATH, '//uni-button[text()="登录"]')
        wait.until(ec.text_to_be_present_in_element(but_login,"登录"))

        # 进行用户登录操作
        self.locator(*name).send_keys(username)
        self.locator(*pwd).send_keys(password)
        time.sleep(2)
        self.locator(*but_login).click()
        # 根据*** 的出现作为等待条件，确保首页正常出现
        seach = (By.XPATH, '//*[text()="确认"]')
        wait.until(ec.text_to_be_present_in_element(seach,"确认"))

