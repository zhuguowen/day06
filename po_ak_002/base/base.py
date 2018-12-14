"""
    目标：base基类工具封装
    步骤：
        1. 新建类
        2. 封装哪些工具(公共)方法？
            0. 查找元素
            1. 输入方法
            2. 点击方法
"""
from selenium.webdriver.support.wait import WebDriverWait


# 建类
class Base():
    def __init__(self, driver):
        self.driver = driver

    # 查找元素方法
    def base_find_element(self, loc, timeout=30, poll=0.5):
        # 显示等待+find_element(By.xxx,xxx)
        return WebDriverWait(self.driver, timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 输入方法
    def base_input(self, loc, value):
        # 调用 查找元素方法
        el = self.base_find_element(loc)
        # 清空操作
        el.clear()
        # 输入操作
        el.send_keys(value)

    # 点击方法
    def base_click(self, loc):
        # 调用查找元素 并 点击操作
        self.base_find_element(loc).click()
