"""
    目标：
        1. 导包 yaml
        2. 打开yaml文件
        3. 调用 load()方法
"""

# 导包
import os
import yaml


# # 打开文件
# with open("../data/data_login.yaml", "r", encoding="utf-8") as f:
#     # 调用load方法
#     print(yaml.load(f))


class ReadYaml():
    def __init__(self,filename):
        self.filename=os.getcwd()+os.sep+"data"+os.sep+filename

    # 定义函数名
    def read_yaml(self):
        # 打开文件
        with open(self.filename, "r", encoding="utf-8") as f:
            # 调用load方法
            return yaml.load(f)


if __name__ == '__main__':
    print(ReadYaml().read_yaml())