"""
    目标：爱客登录 业务成实现
    步骤：
        1. setup_class()
            1. 实例化 统一入口类
        2. teardown_class()
            1. 关闭driver
        3. test_login()
            1. 测试步骤实现
                1). 输入用户名
                2). 输入密码
                3). 点击登录
"""
import os
import sys
sys.path.append(os.getcwd())
import pytest
from page.page_in import PageIn


# 新建类
class TestLogin():
    # setup_class
    def setup_class(self):
        # 实例化统一入口 并 获取登录页面对象
        self.login=PageIn().page_get_pagelogin()
    # teardown_class
    def teardown_class(self):
        # 关闭driver
        self.login.driver.quit()
    # test_login
    @pytest.mark.parametrize("username,password",[("18610453007","123123")])
    def test_login(self,username,password):
        # 输入用户名
        self.login.page_input_username(username)
        # 输入密码
        self.login.page_input_pwd(password)
        # 点击登录
        self.login.page_click_login_btn()