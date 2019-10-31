import unittest
from api.login_api import LoginApi
import logging
from utils import assert_utils


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.login_api = LoginApi()
        pass

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    # 测试登陆成功
    def test01_login_success(self):
        # 发送登陆请求
        response = self.login_api.login("13800000002", "123456")
        logging.info("登陆成功的数据： {}".format(response.json()))

        # jsonData = response.json() # type:dict
        # # 断言
        # self.assertEqual(200, response.status_code)
        # self.assertEqual(True,jsonData.get("success"))
        # self.assertEqual(10000, jsonData.get("code"))
        # self.assertIn("操作成功", jsonData.get("message"))

        # 断言
        assert_utils(self, response, 200, True, 10000, "操作成功")

    # 测试用户名不存在
    def test02_mobile_is_not_exists(self):
        # 发送登陆请求
        response = self.login_api.login("13900000002", "123456")
        logging.info("用户名不存在： {}".format(response.json()))
        # 断言
        assert_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 密码错误
    def test03_password_is_error(self):
        # 发送登陆请求
        response = self.login_api.login("13800000002", "error")
        logging.info("密码错误： {}".format(response.json()))
        # 断言
        assert_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 请求参数为空
    def test04_requests_params_is_empyt(self):
        # 调用参数为空的登陆接口
        response = self.login_api.login_empty()
        logging.info("请求参数为空： {}".format(response.json()))
        # 断言
        assert_utils(self, response, 200, False, 99999, "抱歉，系统繁忙，请稍后重试")

    # 用户名为空
    def test05_mobile_is_empyt(self):
        # 发送登陆请求
        response = self.login_api.login("", "error")
        logging.info("用户名为空： {}".format(response.json()))
        # 断言
        assert_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 密码为空
    def test06_password_is_empty(self):
        # 发送登陆请求
        response = self.login_api.login("13800000002", "")
        logging.info("密码为空： {}".format(response.json()))
        # 断言
        assert_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 添加一个无效的参数
    def test07_add_invalid_params(self):
        # 发送添加无效参数的登陆请求
        response = self.login_api.login_invalid_params("13800000002", "123456", verfify="123456")
        logging.info("添加一个无效的参数： {}".format(response.json()))
        # 断言
        assert_utils(self, response, 200, True, 10000, "操作成功")


