"""
    目标：统一入口类实现
    操作：
        1. 新建page_in模块
        2. 新建PageIn类
        3. 需要管理几个页面对象，就创建几个获取页面对象的方法
        4. 解决driver问题
"""
from base.get_driver import get_driver
from page.page_address import PageAddress
from page.page_login import PageLogin
from page.page_search import PageSearch

# 定义driver
driver=get_driver()


# 建类
class PageIn():

    # 创建 获取PageSearch对象方法
    def page_get_pageserarch(self):
        return PageSearch(driver)

    # 创建 获取PageLogin对象方法
    def page_get_pagelogin(self):
        return PageLogin(driver)

    # 创建 获取PageAddress对象方法
    def page_get_pageaddress(self):
        return PageAddress(driver)