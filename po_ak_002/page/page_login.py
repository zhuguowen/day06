"""
    目标：page对象编写
    操作：
        0. 核心:继承 Base
        1. 新建模块 page_页面名称.py
        2. 新建类 大驼峰将模块搬进来(去掉下划线)
        3. 内容(不过脑)
            1. 将每个操作步骤单独封装一个函数

"""
from base.base import Base
import page


# 建类
class PageLogin(Base):
    # 输入用户名
    def page_input_username(self,username):
        # 调用 封装的输入方法 来实现输入用户名
        self.base_input(page.loc_username,username)

    # 输入密码
    def page_input_pwd(self,password):
        self.base_input(page.loc_pwd,password)

    # 点击登录
    def page_click_login_btn(self):
        # 调用base内点击元素的方法 进行点击按钮操作
        self.base_click(page.loc_btn)
