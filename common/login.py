# coding=utf-8
import requests,json,os,sys
from config.log.mylog import log

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
'''客户端登陆'''
class Login:
    def login(self):
        s = requests.session()
        headers= {"Content-Type": "application/json",
                  "X-UserID": "1004-com.droidhang.aod.google-839699602",
                  "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkaEFjY291bnRJZCI6ODM5Njk5NjAyLCJleHBpcmUiOjE2MTc5NTg1MDR9.x4ZEC1u4XwDHkAQropyN6fL5CbRnavfI10C53_0s0vU"
                  }

        url="http://182.150.22.61:37777/v2/user/login"
        data={"from":2,"language":0,"nickname":"player10723682","avatar":"hero_edward1001","level":1,"zone":"1","game_id":1004,"device_id":"202006112220584ffcfdd29e8e753eb9084d11faa390d1012c5ae159e3aac6","user_id":"1004-com.droidhang.aod.google-839699602"}
        r=s.post(url=url,data=json.dumps(data),headers=headers)
        print(r.json())
        try:
            if r.json()['error_msg']=="success":
                log.info("登陆成功")
        except Exception:
            log.info('数据异常，登陆失败')


Login=Login()
