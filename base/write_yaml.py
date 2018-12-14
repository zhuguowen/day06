"""
    目标：yaml写入方法
    步骤：
        1. data：要写入的内容
        2. stream: 文件流-写到哪个目录叫什么文件名(文件流需要打开操作)
        3. 调用 dump()方法

"""
import yaml
# 写入数据

data = {'Search_Data': {
    'search_test_002': {'expect': {'value': '你好'}, 'value': '你好'},
    'search_test_001': {'expect': [4, 5, 6], 'value': 456}}}
# 写入文件流
with open("../data/data03_write.yaml", "w", encoding="utf-8")as f:
    # 调用 dump方法
    yaml.dump(data,f,encoding='utf-8',allow_unicode=True)