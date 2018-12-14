"""
    目标：以po模式编写搜索 --》page
    提示：
        1. 新建模块模块  page_xxx.py
        2. 类名 大驼峰编写模块名(去掉下划线)
        3. page与base关系(核心：page对象都继承Base类)
        4. page类的内容如何编写？(一个步骤，封装一个单独方法)
"""
import page
from base.base import Base


# 类名
class PageSearch(Base):
    # 点击搜索按钮 封装
    def page_click_search_btn(self):
        self.base_click(page.search_btn)

    # 输入搜索内容
    def page_input_text(self,text):
        self.base_input(page.search_input_search,text)

    # 点击返回按钮
    def page_click_back_btn(self):
        self.base_click(page.search_back_btn)