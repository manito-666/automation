# coding=utf-8
import pymysql
import config.readconfig as readconfig
from config.log.mylog import log
localReadConfig = readconfig.ReadConfig()

class MyDB():
    def __init__(self):
        host=localReadConfig.get_db("host")
        username = localReadConfig.get_db("username")
        password = localReadConfig.get_db("password")
        port = localReadConfig.get_db("port")
        database=localReadConfig.get_db("database")
        self.config = {
            'host': str(host),
            'user': username,
            'passwd': password,
            'port': int(port),
            'db':str(database)
        }
        self.log=log()

    def connectDB(self):

        try:
            # connect to DB
            self.db = pymysql.connect(**self.config)
            # create cursor
            self.cursor = self.db.cursor()
            self.log.info("Connect DB successfully!")
        except ConnectionError as ex:
            self.log.debug("连接数据库失败")

    def executeSQL(self, sql):

        self.connectDB()

        try:
            self.cursor.execute(sql)
        except:
            self.log.debug("sql错误")
        # executing by committing to DB
        self.db.commit()
        return self.cursor

    def get_all(self, cursor):

        value = cursor.fetchall()
        return value

    def get_one(self, cursor):

        value = cursor.fetchone()
        return value
    def closeDB(self):

        self.cursor.close()
        self.db.close()
        self.log.info("Database closed!")

if __name__ == '__main__':
    db=MyDB()
    # db.connectDB()
    cursor=db.executeSQL(sql="select * from  im_system.t_sys_user  ")
    s=db.get_one(cursor)
    print(s)

    db.closeDB()

