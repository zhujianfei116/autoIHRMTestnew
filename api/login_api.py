import requests
import app
import logging


class LoginApi:

    def __init__(self):
        # 定义登陆的URL
        self.login_url = app.HOST + "/api/sys/login"
        # 　定义请求头
        self.headers = app.HEADERS

    def login(self, mobile, password):
        # 组合要发送的登陆数据
        data = {
            "mobile": mobile,
            "password": password
        }
        # 返回登陆响应结果
        return requests.post(url=self.login_url, json=data, headers=self.headers)

    # 封装请求参数为空的登陆请求
    def login_empty(self):
        return requests.post(url=self.login_url)

    # 封装增加无效参数的登陆请求
    def login_invalid_params(self, mobile, password, *args, **kwargs):
        data = {
            "mobile": mobile,
            "password": password
        }
        if kwargs:
            logging.info(kwargs)
            for k, v in kwargs.items():
                data[k] = v
        logging.info("无效参数的登陆数据 {}".format(data))
        return requests.post(self.login_url, json=data, headers=self.headers)
