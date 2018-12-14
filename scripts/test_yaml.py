import os
import sys
sys.path.append(os.getcwd())

import pytest
from base.read_data import ReadYaml

# 获取yaml数据方法

"""
    需求数据格式：[("",""),("","")]
"""

def get_data():
    # 定义空列表
    arrs = []
    for data in ReadYaml("data_login.yaml").read_yaml().values():
        # 组装数据格式 [("username","password"),("username","password")]
        arrs.append((data.get("username"),data.get("password")))
    return arrs


class TestYaml():
    def setup_class(self):
        pass

    def teardown_class(self):
        pass

    @pytest.mark.parametrize("username,password", get_data())
    def test_yaml(self,username,password):
        print("正在登录用户名为：", username)
        print("正在登录密码为：", password)