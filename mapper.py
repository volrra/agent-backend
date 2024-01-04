import sqlite3

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
        self.con=sqlite3.connect(':memory:')
        self.cur=self.con.cursor()
        self.sql_init()

    def __del__(self):
        self.cur.close()
        self.con.close()

    def sql_init(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS user(id INTEGER PRIMARY KEY,name TEXT,password TEXT)")
        try:
            self.cur.execute("insert into user values (?,?,?)",(0,"system-uesr","123456"))
        except:
            a=0
    # get the complete info of one user, for login module
    def get_user(self,name,password):
        try:
            self.cur.execute("select * from user where name=? and password=?",(name,password))
        except:
            return []
        return self.cur.fetchall()

    # check whether the new username exists in db, true for the legal username
    def check_username(self,name):
        try:
            self.cur.execute("select * from user where name=?",(name,))
        except:
            return False
        if self.cur.fetchall() != []:
            return False
        else:
            return True

    # insert new user, for register module
    def insert_user(self,name,password):
        try:
            self.cur.execute("select max(id) from user")
            maxid=self.cur.fetchone()[0]
            self.cur.execute("insert into user values (?,?,?)",(maxid+1,name,password))
        except:
            return None
        self.con.commit()
        return maxid+1
