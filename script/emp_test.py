import unittest
from api.emp_api import EmpApi
from api.login_api import LoginApi
from utils import assert_utils
import app
import logging
import pymysql


class EmpTest(unittest.TestCase):

    def setUp(self) -> None:
        pass

    @classmethod
    def setUpClass(cls) -> None:
        cls.login_api = LoginApi()
        cls.emp_api = EmpApi()

    def tearDown(self) -> None:
        pass

    def test01_login_success(self):
        # 调用登陆接口
        response = self.login_api.login("13800000002", "123456")
        # 提取登陆接口返回的json数据
        jsonData = response.json()
        logging.info("员工管理模块登陆接口的调用结果为： {}".format(jsonData))

        # token的格式"Bearer 14d94aec-94c1-4fd3-94a1-ffbcfb8c32ed"
        token = "Bearer " + jsonData.get("data")
        # 保存员工管理模块所需要的token到app.HEADERS
        app.HEADERS['Authorization'] = token
        logging.info("员工管理模块登陆接口中访问app.Headers的值为： {}".format(app.HEADERS))

        # 断言
        assert_utils(self, response, 200, True, 10000, "操作成功")

    def test02_add_emp(self):
        # 调用添加员工接口
        response = self.emp_api.add_emp("女娲008", "13700452329")

        jsonData = response.json()
        # 打印结果
        logging.info("添加员工接口的返回值为： {}".format(jsonData))

        # 获取员工id
        emp_id = jsonData.get("data").get("id")
        app.EMP_ID = emp_id
        logging.info("添加员工接口后，保存在app.EMP_ID的值为{}".format(app.EMP_ID))

        # 建立连接
        conn = pymysql.connect('182.92.81.159',
                               user='readuser',
                               password="iHRM_user_2019",
                               database="ihrm",
                               charset='utf8',
                               autocommit=False)
        # 获取游标
        cursor = conn.cursor()
        # 执行SQL
        sql = "select username from bs_user where id = {}".format(emp_id)
        cursor.execute(sql)
        # 使用cursor.fetchone来接收结果
        result = cursor.fetchone()
        logging.info("从数据库查询的到的username是{}".format(result))
        # 关闭cursor
        cursor.close()
        # 关闭连接
        conn.close()

        # 对从数据库总取出的username进行断言
        self.assertEqual("女娲008", result[0])

        # 断言
        assert_utils(self, response, 200, True, 10000, "操作成功")

    def test03_query_emp(self):
        # 调用添加员共接口
        response = self.emp_api.query_emp(app.EMP_ID)
        logging.info("查询员工接口返回的数据为：{}".format(response.json()))

        # 断言
        assert_utils(self, response, 200, True, 10000, "操作成功")

    def test04_update_emp(self):
        # 更新员工接口
        response = self.emp_api.update_emp("John Smith", app.EMP_ID)
        logging.info("修改员工的结果为：{}".format(response.json()))

        # 断言
        assert_utils(self, response, 200, True, 10000, "操作成功")

    def test05_delete_emp(self):
        # 删除员工接口
        response = self.emp_api.delete_emp(app.EMP_ID)
        logging.info("删除员工的结果为：{}".format(response.json()))

        # 断言
        assert_utils(self, response, 200, True, 10000, "操作成功")
