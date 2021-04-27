# coding=utf-8
import os,sys
from config.configHttp import r
Path = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(Path)[0]
sys.path.append(rootPath)

class management():

    def man(self,method,url,datas,headers):
        r.request_log(method=method, url=url, datas=datas, headers=headers)
        rep = r.run_main(method,url,datas,headers).json()
        return rep['error_msg']

m=management()
