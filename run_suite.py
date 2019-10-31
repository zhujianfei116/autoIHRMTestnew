# 1 导包
import unittest
# from script.login_test import LoginTest
# from script.emp_test import EmpTest
from script.emp_parameterized import EmpTest
from script.login_parameterized import LoginTest
from tools.HTMLTestRunner import HTMLTestRunner
import app
import time

# 2 生成测试套件
suite = unittest.TestSuite()
# 3 将测试用例添加到测试套件
suite.addTest(unittest.makeSuite(LoginTest))
suite.addTest(unittest.makeSuite(EmpTest))

# 4 指定测试报告的地址
report_path = app.BASE_DIR + "/report/ihrm-{}.html".format(time.strftime('%Y%m%d %H%M%S'))
# 5 使用HTMLTestRunner运行测试套件
with open(report_path, 'wb') as f:
    # 定义HTMLTestRunner的实例
    runner = HTMLTestRunner(f, verbosity=1, title="IHRM人力资源管理系统", description="V1.1")
    # 使用runner实例运行测试套件
    runner.run(suite)
