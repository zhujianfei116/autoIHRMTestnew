import unittest
from api.login_api import LoginApi
import logging
from utils import assert_utils, read_login_data, custom_name_func
from parameterized.parameterized import parameterized


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.login_api = LoginApi()
        pass

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    # 测试登陆
    @parameterized.expand(read_login_data, name_func=custom_name_func)
    def test01_login(self, case_name, mobile, password, status_code, success, code, message):
        # 发送登陆请求
        response = self.login_api.login(mobile, password)
        logging.info("登陆成功的数据： {}".format(response.json()))

        # jsonData = response.json() # type:dict
        # # 断言
        # self.assertEqual(200, response.status_code)
        # self.assertEqual(True,jsonData.get("success"))
        # self.assertEqual(10000, jsonData.get("code"))
        # self.assertIn("操作成功", jsonData.get("message"))

        # 断言
        assert_utils(self, response, status_code, success, code, message)

    # 请求参数为空
    def test04_requests_params_is_empyt(self):
        # 调用参数为空的登陆接口
        response = self.login_api.login_empty()
        logging.info("请求参数为空： {}".format(response.json()))
        # 断言
        assert_utils(self, response, 200, False, 99999, "抱歉，系统繁忙，请稍后重试")

    # 添加一个无效的参数
    def test07_add_invalid_params(self):
        # 发送添加无效参数的登陆请求
        response = self.login_api.login_invalid_params("13800000002", "123456", verfify="123456")
        logging.info("添加一个无效的参数： {}".format(response.json()))
        # 断言
        assert_utils(self, response, 200, True, 10000, "操作成功")
