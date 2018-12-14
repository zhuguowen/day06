"""
    目标：已PO模式实现 设置搜索练习 --》base
    重要：base内存放公共方法（不能有固定数据）
    分析：
        1. 点击搜索按钮 --》公共方法：点击方法
        2. 输入内容--》 公共方法：输入方法
"""
# 类名 模块名以大驼峰形式编写（如果有下划线去掉下划线）
from selenium.webdriver.support.wait import WebDriverWait


class Base():

    def __init__(self,driver):
        self.driver=driver

    # 查找元素 封装 目的：给点击和输入方法使用
    def base_find_element(self,loc,timeout=30,poll=0.5):
        # 使用显示等待 查找元素  # *loc：为元祖解包
        return WebDriverWait(self.driver,timeout,poll_frequency=poll).until(lambda x:x.find_element(*loc))

    # 点击方法 封装
    def base_click(self,loc):
        # 调用查找元素方法 并 进行点击操作
        self.base_find_element(loc).click()

    # 输入方法 封装
    def base_input(self,loc,value):
        # 调用查找元素方法，获取元素
        el=self.base_find_element(loc)
        # 清空操作
        el.clear()
        # 输入方法
        el.send_keys(value)