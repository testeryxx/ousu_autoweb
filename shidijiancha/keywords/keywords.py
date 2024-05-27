from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains




# 定义工具类（进行关键字驱动）
class WebKeys:
    # 构造方法，用来接收driver对象
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    # 打开浏览器
    def open(self, url):
        self.driver.get(url)

    # 元素定位
    def locator(self, name, value):
        el = self.driver.find_element(name, value)
        # 将定位的元素标记出来
        self.locator_station(el)
        return el

    def locator_with_wait(self, name, value):
        '''
        元素定位+等待
        :param name:定位方式
        :param value: 元素定位的值
        :return:
        '''
        locator = (name, value)
        self.wait.until(ec.visibility_of_element_located(locator))
        el = self.driver.find_element(name, value)
        self.locator_station(el)
        return el

    # 显示定位的地方，方便确认定位位置
    def locator_station(self, ele):
        self.driver.execute_script(
            "arguments[0].setAttribute('style',arguments[1]);",
            ele,
            "border: 2px solid red"  # 边框，red红色
        )

    def change_window(self, n):
        '''
        窗口切换功能
        :param n:
         # 切换到原始页面 n=0
        # 切换到第二页面 n=1
        # 切换到最新页面 n=-1
        :return:
        '''
        # 获取句柄
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[n])
        print('当前成功跳转的页面：', self.driver.title)

    def text_wait(self, name, value, text):
        '''元素文本获取 + 显示等待'''
        el = (name, value)
        res = self.wait.until(ec.text_to_be_present_in_element(el, text))
        return res

    def mouse_hold(self):
        '''鼠标事件'''
        action = ActionChains(self.driver)
        action.click() #鼠标点击
        # action.click_and_hold()
        # action.scroll_to_element()
        action.perform()


