# coding=utf-8
import requests
import json
from config import readconfig as readConfig
from config.log.mylog import log
logger=log
localReadConfig = readConfig.ReadConfig()
class ConfigHttp:
    def __init__(self):
        global host, port, timeout,headers
        host = localReadConfig.get_http("url")
        port = localReadConfig.get_http("port")
        headers=localReadConfig.get_http("headers")
        timeout = localReadConfig.get_http("timeout")
        self.log=log
        self.headers = None
        self.params = {}
        self.data = {}
        self.url = None
        self.files = {}

    def set_url(self, path):
        self.url =host + port + path
        return self.url

    def set_headers(self):
        keys = ["Content-Type", "X-UserID","Authorization"]
        values = ["application/json", "1004-com.droidhang.aod.google-839699602","eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkaEFjY291bnRJZCI6ODM5Njk5NjAyLCJleHBpcmUiOjE2MTc5NTg1MDR9.x4ZEC1u4XwDHkAQropyN6fL5CbRnavfI10C53_0s0vU"]
        dic = dict(zip(keys, values))
        return dic

    def set_params(self, param):
        self.params = param
        return self.params

    def set_data(self, data):
        self.data = data
        return self.data

    def set_files(self, file):
        self.files = file
        return self.files


class RunMain():

    def send_post(self, url, datas,headers):
        # 参数必须按照url、data,headers顺序传入
        result = requests.post(url=url, data=datas,headers=headers)# 封装post方法
        return result

    def send_get(self, url, datas,headers):
        result = requests.get(url=url, params=datas,headers=headers)
        return result

    def send_put(self, url, datas,headers):
        result = requests.get(url=url, params=datas,headers=headers)
        return result

    def send_delete(self, url, datas,headers):
        result = requests.get(url=url, params=datas,headers=headers)
        return result


    def send_request(self,testdata):

        result = None
        method=testdata.method
        url=testdata.url
        datas=testdata.datas

        if method == 'post':
            result = self.send_post(url, datas, headers)
        elif method == 'get':
            result = self.send_get(url, datas, headers)
        elif method == 'put':
            result = self.send_put(url, datas, headers)
        else:
            print("method值错误！！！")
        return result

    def run_main(self, method, url=None, datas=None, headers=None, **kwargs):  # 定义一个run_main函数，通过传过来的method来进行不同的get或post请求
        result = None
        if method == 'post':
            result = self.send_post(url, datas,headers)
        elif method == 'get':
            result = self.send_get(url, datas,headers)
        elif method =='put':
            result = self.send_put(url, datas, headers)
        else:
            print("method值错误！！！")

        return result

    def request_log(self, url, method, datas=None, title=None,params=None, headers=None, **kwargs):
        logger.info("接口请求地址 ==>> {}".format(url))
        logger.info("接口请求方式 ==>> {}".format(method))
        # Python3中，json在做dumps操作时，会将中文转换成unicode编码，因此设置 ensure_ascii=False
        logger.info("接口请求头 headers参数 ==>> {}".format(json.dumps(headers, indent=4, ensure_ascii=False)))
        logger.info("用例描述 ==>> {}".format(title))
        logger.info("接口请求 params 参数 ==>> {}".format(json.dumps(params, indent=4, ensure_ascii=False)))
        logger.info("接口请求体 data 参数 ==>> {}".format(datas))




r=RunMain()
