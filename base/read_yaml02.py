"""
    目标：yaml文件读取方法
    方法：load
    步骤：
        1. 导入yaml包
        2. 打开文件操作 获取文件流
        3. 调用load方法
    扩展：
        1. 新建函数名 def read_yaml():
        2. 函数内一定要return 结果
"""
# 导包
import yaml

# # 打开文件
# with open("../data/data01.yaml", "r", encoding = "utf-8") as f:
#     # 调用load方法
#     print(yaml.load(f))

# 扩展 封装函数
def read_yaml():
    with open("../data/data01.yaml", "r", encoding = "utf-8") as f:
        # 调用load方法
        return yaml.load(f)

if __name__ == '__main__':
    print(read_yaml())