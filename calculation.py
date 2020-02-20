class ATI:
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def summation(self):
        return self.a+self.b
    def multiplication(self):
        return self.a*self.b;
    def divide(self):
        return self.a/self.b;

# import sqlite3
# class ATI:
#     def __init__(self):
#         self.con=sqlite3.connect('cskipl.db')
#         self.cursor=self.con.cursor()
#
#
#     def cskati(self, name, ID, price, city):
#         sa="CREATE TABLE IF NOT EXISTS cskteam (ID INT PRIMARY KEY NOT NULL, palyername VARCHAR(20) NOT NULL, price REAL, city CHAR(50))"
#         self.cursor.execute(sa)