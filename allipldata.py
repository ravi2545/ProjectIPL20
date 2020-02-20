import sqlite3
from mainfile import *
class ATI:
    def __init__(self):
        self.con=sqlite3.connect('cskipl.db')
        self.cursor=self.con.cursor()
        self.msg = "SUCCESSFULLY ADDED"


    def cskati(self, name, ID, price, city):
        sa="CREATE TABLE IF NOT EXISTS cskteam (ID INT PRIMARY KEY NOT NULL, palyername VARCHAR(20) NOT NULL, price REAL, city CHAR(50))"
        self.cursor.execute(sa)
        self.cursor.execute("INSERT into cskteam (ID, palyername, price, city) values (?,?,?,?)", (ID,name,price,city))
        self.con.commit()
        return upd()

    def cskdel(self, ID):
        sa="DELETE FROM cskteam WHERE ID = {}".format(ID)
        self.cursor.execute(sa)
        self.con.commit()
        return delt()