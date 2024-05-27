import pytest, logging, allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def browser():
    # 01 用例的前置操作
    global driver
    driver = webdriver.Chrome()
    '''无头模式
    chrome_options= Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    '''



    # 02 用例执行的时候返回driver
    yield driver

    # 03 用例的后置操作，关闭浏览器
    driver.quit()

# 钩子函数，生成报告截图
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport():
    # 获取测试用例的执行结果对象
    out = yield

    """
        从result对象out获取调用结果的测试报告，返回一个report对象

        report对象的属性：
        包含三个属性：
        when: setup、call、teardown三个值
        nodeid: 测试用例的名称
        outcome: 测试用例的执行结果 passed、failed
    """
    report = out.get_result()  # 返回一个report对象

    # 根据判断条件来进行截图取证
    if report.when == 'call':  # 仅仅只获取用例call阶段的执行结果
        # 获取用例call执行结果为失败的情况：
        xfail = hasattr(report, 'wasxfail')  # hasattr方法会：返回对象是否具有给定的名称的属性

        # 如果测试用例被跳过并且标记为预期失败，或者测试用例执行失败并且不是预期失败
        if (report.skipped and xfail) or (report.failed and not xfail):
            # 添加allure报告截图
            with allure.step("添加失败截图... ..."):
                # 使用allure自带的添加附件的方法
                allure.attach(driver.get_screenshot_as_png(), '失败截图', allure.attachment_type.PNG)

        # 成功用例的截图操作
        elif report.passed:
            # 如果测试用例执行通过，添加allure报告截图
            with allure.step("添加成功截图... ..."):
                # 使用allure自带的添加附件的方法
                allure.attach(driver.get_screenshot_as_png(), '成功截图', allure.attachment_type.PNG)


# 当执行一个case的时候会自动的调用这个方法：把对应的数据传过来给到call
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # 通过 out = yield 定义了一个生成器。在生成器中，res = out.get_result() 获取了测试结果对象。
    out = yield
    report = out.get_result()
    #  res.when == "call"：表示正在运行调用测试函数的阶段。
    if report.when == "call":
        allure.attach
        allure.attach(f"用例ID：{report.nodeid}", name="用例ID")
        allure.attach(f"测试结果：{report.outcome}", name="测试结果")
        allure.attach(f"故障表示：{report.longrepr}", name="故障表示")
        allure.attach(f"异常：{call.excinfo}", name="异常")
        allure.attach(f"用例耗时：{report.duration}", name="用例耗时")
        allure.attach("**************************************")
        xfail = hasattr(report, 'wasxfail')  # hasattr方法会：返回对象是否具有给定的名称的属性

        # 如果测试用例被跳过并且标记为预期失败，或者测试用例执行失败并且不是预期失败
        if (report.skipped and xfail) or (report.failed and not xfail):
            # 添加allure报告截图
            with allure.step("添加失败截图... ..."):
                # 使用allure自带的添加附件的方法
                allure.attach(driver.get_screenshot_as_png(), '失败截图', allure.attachment_type.PNG)

        # 成功用例的截图操作
        # elif report.passed:
        else:
            # 如果测试用例执行通过，添加allure报告截图
            with allure.step("添加成功截图... ..."):
                # 使用allure自带的添加附件的方法
                allure.attach(driver.get_screenshot_as_png(), '成功截图', allure.attachment_type.PNG)

