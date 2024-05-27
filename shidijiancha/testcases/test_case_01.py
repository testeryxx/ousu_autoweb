import time
import pytest

from VAR.var import *
from keywords.keywords import WebKeys
from logic.login import LoginPage


@pytest.mark.skip
def test_addspotcheck(browser):
    # 初始化工具类
    wk = WebKeys(browser)

    # 登录
    wk.open(PRO_URL)
    wk.locator(name='xpath', value='//input[@class="uni-input-input"]').send_keys(UESRNAME)
    time.sleep(10)
    wk.locator(name='xpath', value='//input[@type="password"]').send_keys(PWD)
    time.sleep(10)
    wk.locator(name='xpath', value='//uni-button[text()="登录"]').click()


def test_addcheck(browser):
    login = LoginPage(browser)
    login.login(PRO_URL, UESRNAME, PWD)
