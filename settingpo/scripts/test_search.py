"""
    目标： 以po模式编写设置搜索  --》scripts脚本
    步骤：
        1. 新建模块 test_xxx.py
        2. 新建类名 大驼峰编写模块名(去掉下划线)
        3. 不用动脑编写三个方法
            1). setup_class
                    实例化页面对象
            2). teardown_class
                    关闭driver
            3). test_xxx
                    根据测试步骤调用page类
"""
import os
import sys
# 将当前模块所在目录添加到系统path环境中 （我们使用pytest配置文件去执行，配置文件所在路径为根目录）
sys.path.append(os.getcwd())
import pytest
from base.get_driver import get_driver
from page.page_search import PageSearch


# 建类
class TestSearch():
    # setup_class
    def setup_class(self):
        # 实例化页面对象
        self.serach=PageSearch(get_driver())

    # teardown_class
    def teardown_class(self):
        # 调用base类关闭驱动对象方法
        self.serach.driver.quit()

    # test_xxx测试方法
    @pytest.mark.parametrize("text",["123"])
    def test_search(self,text):
        search=self.serach
        # 点击 搜索按钮
        search.page_click_search_btn()
        # 输入 输入文本(123)
        search.page_input_text(text)
        # 点击 返回按钮
        search.page_click_back_btn()