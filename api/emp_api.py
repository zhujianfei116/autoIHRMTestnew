import app
import requests
import logging


class EmpApi:

    def __init__(self):
        # http://182.92.81.159/api/sys/user
        self.add_emp_url = app.HOST + "/api/sys/user"
        self.query_emp_url = app.HOST + "/api/sys/user"
        self.update_emp_url = app.HOST + "/api/sys/user"
        self.delete_emp_url = app.HOST + "/api/sys/user"
        self.headers = app.HEADERS
        pass

    def add_emp(self, username, mobile):
        data = {
            "username": username,
            "mobile": mobile,
            "timeOfEntry": "2019-10-01",
            "formOfEmployment": 1,
            "workNumber": "9833221",
            "departmentName": "财务部",
            "departmentId": "1066238836272664576",
            "correctionTime": "2019-12-31T16:00:00.000Z"
        }
        logging.info("添加员工接口中，请求头为：self.headers = {}".format(self.headers))
        return requests.post(self.add_emp_url, json=data, headers=self.headers)

    def query_emp(self, emp_id):
        logging.info("传入的查询员工API接口中的emp_id的值为:{}".format(emp_id))
        # 拼接员工ID，组成查询员工的URL
        self.query_emp_url = self.query_emp_url + '/' + emp_id
        logging.info("查询员工接口的URL为　{}".format(self.query_emp_url))
        return requests.get(self.query_emp_url, headers=self.headers)
        pass

    def update_emp(self, username, emp_id):
        self.update_emp_url = self.update_emp_url + "/" + emp_id
        return requests.put(self.update_emp_url, json={"username": username}, headers=self.headers)

    def delete_emp(self, emp_id):
        self.delete_emp_url = self.delete_emp_url + "/" + emp_id
        return requests.delete(self.delete_emp_url, headers=self.headers)
