import pymysql
# con=sqlite3.connect('../database/test.db')
# cur=con.cursor()
# data="1,'tom','123456'"
# # cur.execute("INSERT INTO user VALUES (%s) "%data)
# cur.execute("select * from user where id=1")
# con.commit()
# print(cur.fetchone())
# for i in cur:
#     print(i)
#
# cur.execute("select max(id) from user")
#
# def db_init():
#     cur.execute("CREATE TABLE IF NOT EXISTS user(id INTEGER PRIMARY KEY,name TEXT,password TEXT)")
#
# db_init()
# cur.close()
# con.close()

class Mapper:
    def __init__(self):
        self.con = pymysql.connect(host='qx6.h.filess.io'  # 连接名称，默认127.0.0.1
                               , user='JOIagent_wantantsme'  # 用户名
                               , passwd='1e6eaca6476f68fefe9a88f57cdac45513c42e62'  # 密码
                               , port=3307  # 端口，默认为3306
                               , db='JOIagent_wantantsme'  # 数据库名称
                               , charset='utf8'  # 字符编码
                               )
        self.cur=self.con.cursor()
        self.sql_init()

    def __del__(self):
        self.cur.close()
        self.con.close()

    def sql_init(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS user(id INTEGER PRIMARY KEY,name varchar(100),password varchar(100))")
        try:
            self.cur.execute("insert into user values (0,'system-uesr','123456')",)
        except:
            a=0
        self.con.commit()
    # get the complete info of one user, for login module
    def get_user(self,name,password):
        try:
            self.cur.execute("select * from user where name='%s' and password='%s'"%(name,password))
        except:
            return []
        return self.cur.fetchall()

    # check whether the new username exists in db, true for the legal username
    def check_username(self,name):
        try:
            self.cur.execute("select * from user where name='%s'"%name)
        except:
            return False
        if len(self.cur.fetchall()) !=0:
            return False
        else:
            return True

    # insert new user, for register module
    def insert_user(self,name,password):
        try:
            self.cur.execute("select max(id) from user")
            maxid=self.cur.fetchone()[0]
            self.cur.execute("insert into user values (%d,'%s','%s')"%(maxid+1,name,password))
        except:
            return None
        self.con.commit()
        return maxid+1



#
# con = pymysql.connect(host='qx6.h.filess.io'  # 连接名称，默认127.0.0.1
#                                , user='JOIagent_wantantsme'  # 用户名
#                                , passwd='1e6eaca6476f68fefe9a88f57cdac45513c42e62'  # 密码
#                                , port=3307  # 端口，默认为3306
#                                , db='JOIagent_wantantsme'  # 数据库名称
#                                , charset='utf8'  # 字符编码
#                                )
# cur=con.cursor()
# x="tom"
# b=0
# cur.execute("select * from user where name='%s' and id=%d"%(x,b))
# a=cur.fetchall()
# con.commit()


