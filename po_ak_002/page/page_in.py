from base.get_driver import get_driver
from page.page_login import PageLogin


class PageIn():
    # 获取PageLogin()对象
    def page_get_pagelogin(self):
        return PageLogin(get_driver())