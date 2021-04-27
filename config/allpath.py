import os

proDir = os.path.split(os.path.realpath(__file__))[0]

configPath = os.path.join(proDir, "config")
prj_path=os.path.abspath(os.path.join(os.path.dirname("__file__"),os.path.pardir))

# 日志路径
log_path = os.path.join('/Users/wangzhipeng/PycharmProjects/automation/config/log')

# 测试报告路径
result_path=os.path.join(prj_path,'util','report')

#测试数据路径

data_start=os.path.join(prj_path,'util','data','test.xlsx')
data_debug=os.path.join(prj_path,'util','data','result.xlsx')
