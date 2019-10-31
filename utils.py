from unittest import TestCase
from requests import Response
import app
import json
import logging
import re

app.init_logging()


# 用于参数化输出中文
def to_safe_name(s):
    return str(re.sub("[^a-zA-Z0-9_\u4e00-\u9fa5]+", "_", s))


# parameteried模块中使用
def custom_name_func(testcase_func, param_num, param):
    print('匹配结果：', to_safe_name(param.args[0]))
    return "%s_%s_%s" % (
        testcase_func.__name__,
        to_safe_name(param.args[0]),
        param_num
    )


def assert_utils(self, response, status_code, success, code, message):
    """
    @type self:TestCase
    @type response: Response
    """
    jsonData = response.json()  # type: dict
    # 断言
    # HTTP相应状态吗
    self.assertEqual(status_code, response.status_code)
    self.assertEqual(success, jsonData.get("success"))
    self.assertEqual(code, jsonData.get("code"))
    self.assertIn(message, jsonData.get("message"))


def read_login_data():
    # 读取登陆数据
    data_path = app.BASE_DIR + "/data/login_data.json"
    with open(data_path, encoding='utf-8') as f:
        jsonData = json.load(f)
        login_data_list = []
        for login_data in jsonData:
            # logging.info("登陆数据为：{}".format(login_data))
            case_name = login_data.get("case_name")
            mobile = login_data.get("mobile")
            password = login_data.get("password")
            status_code = login_data.get("status_code")
            success = login_data.get("success")
            code = login_data.get("code")
            message = login_data.get("message")
            login_data_list.append((case_name, mobile, password, status_code, success, code, message))
        logging.info("读取后，返回的登陆数据列表为： {}".format(login_data_list))

    return login_data_list


def read_emp_add():
    # 读取添加员工的数据
    data_path = app.BASE_DIR + "/data/emp_data.json"
    with open(data_path, encoding='utf-8') as f:
        jsonData = json.load(f)
        logging.info("jsonData {}".format(jsonData))
        add_emp_data = jsonData.get("emp_add")
        add_emp_data_list = []
        username = add_emp_data.get("username")
        mobile = add_emp_data.get("mobile")
        status_code = add_emp_data.get("status_code")
        success = add_emp_data.get("success")
        code = add_emp_data.get("code")
        message = add_emp_data.get("message")
        add_emp_data_list.append((username, mobile, status_code, success, code, message))
    logging.info("读取到的添加员工的数据为：{}".format(add_emp_data_list))
    return add_emp_data_list


def query_emp():
    # 读取添加员工的数据
    data_path = app.BASE_DIR + "/data/emp_data.json"
    with open(data_path, encoding='utf-8') as f:
        jsonData = json.load(f)
        # logging.info("jsonData {}".format(jsonData))
        query_emp_data = jsonData.get("emp_query")
        query_emp_data_list = []
        status_code = query_emp_data.get("status_code")
        success = query_emp_data.get("success")
        code = query_emp_data.get("code")
        message = query_emp_data.get("message")
        query_emp_data_list.append((status_code, success, code, message))

    logging.info("读取员工数据时，返回的数据为：{}".format(query_emp_data_list))
    return query_emp_data_list


def update_emp_data():
    # 读取添加员工的数据
    data_path = app.BASE_DIR + "/data/emp_data.json"
    with open(data_path, encoding='utf-8') as f:
        jsonData = json.load(f)
        update_emp_data_list = []
        update_emp_data = jsonData.get("emp_update")
        username = update_emp_data.get("username")
        status_code = update_emp_data.get("status_code")
        success = update_emp_data.get("success")
        code = update_emp_data.get("code")
        message = update_emp_data.get("message")
        update_emp_data_list.append((username, status_code, success, code, message))
    logging.info("修改员工数据时，返回的数据为：{}".format(update_emp_data_list))
    return update_emp_data_list


def delete_emp_data():
    # 读取删除员工的数据
    data_path = app.BASE_DIR + "/data/emp_data.json"
    with open(data_path, encoding='utf-8') as f:
        jsonData = json.load(f)
        delete_emp_data_list = []
        delete_emp_data = jsonData.get("emp_delete")
        status_code = delete_emp_data.get("status_code")
        success = delete_emp_data.get("success")
        code = delete_emp_data.get("code")
        message = delete_emp_data.get("message")
        delete_emp_data_list.append((status_code, success, code, message))
    logging.info("删除员工用例的数据为：{}".format(delete_emp_data_list))
    return delete_emp_data_list


if __name__ == '__main__':
    # read_login_data()
    # read_emp_add()
    # read_emp_query()
    # update_emp_data()
    delete_emp_data()
