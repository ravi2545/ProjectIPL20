from flask import *
import sqlite3
from allipldata import *
import onetimepad
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/savedetails", methods=["POST", "GET"])
def saveDetails():
    msg = "msg"
    if request.method == "POST":
        try:
            name = request.form["name"]
            passw = request.form["psd"]
            repassw = request.form["repass"]
            cipher = onetimepad.encrypt(passw, 'random')
            if passw==repassw:
                with sqlite3.connect("iplteams.db") as con:
                    cur = con.cursor()
                    cur.execute("CREATE TABLE IF NOT EXISTS iplravi (name VARCHAR(50), password VARCHAR(50), cry VARCHAR(50))")
                    cur.execute("INSERT into iplravi (name,password, cry) values (?,?,?)", (name, passw, cipher))
                    con.commit()
            else:
                msg = "Password is not matching"
        except:
            con.rollback()
            msg = "We can not add the employee to the list"
        finally:
            return render_template("success.html", msg=msg)
            con.close()

# @app.route('/login', methods=["POST"])
# def login():
#     if request.method=="POST":
#         try:
#             name=request.form["name"]
#             ps=request.form["ps"]
#             with sqlite3.connect("iplteams.db") as conn:
#                 cur = conn.cursor()
#                 cur.execute("SELECT * FROM allteams")
#                 rows = cur.fetchall()
#                 import pdb
#                 pdb.set_trace()
#                 conn.commit()
#                 msg = "Employee successfully Added"
#         except:
#             conn.rollback()
#             msg = "We can not add the employee to the list"
#
#         finally:
#             return render_template("success.html", msg=msg)
#             conn.close()


@app.route("/view", methods=["POST"])
def view():
    if request.method == "POST":
        try:
            name=request.form["name"]
            ps=request.form["ps"]
            with sqlite3.connect("iplteams.db") as conn:
                cur = conn.cursor()
                cur.execute("SELECT * FROM allteams")
                rows = cur.fetchall()
                tp=name, ps,
                for i in range(0, len(rows)):
                    if rows[i]==tp:
                        if name=="CSK":
                            return render_template("csk.html")
                        elif name=="DD":
                            return render_template("dd.html")
                        elif name=="RCB":
                            return render_template("rcb.html")
                        elif name=="MI":
                            return render_template("mi.html")
                        elif name=="RR":
                            return render_template("rr.html")
                        elif name=="KKR":
                            return render_template("kkr.html")
                        elif name=="KIXP":
                            return render_template("kixp.html")
                        elif name=="SRH":
                            return render_template("srh.html")
                        else:
                            return render_template("worng.html")
        except:
            conn.rollback()
    # con = sqlite3.connect("employee.db")
    # con.row_factory = sqlite3.Row
    # cur = con.cursor()
    # cur.execute("select * from Employees")
    # rows = cur.fetchall()
    # return render_template("view.html", rows=rows)

@app.route('/RegisterPlayers')
def RegisterPlayers():
    return render_template("cskreg.html")

@app.route("/saveCSK", methods=["POST"])
def saveCSK():
    if request.method=='POST':
        # import pdb
        # pdb.set_trace()
        name=request.form['name']
        ID=request.form['id']
        price=request.form['price']
        city=request.form['city']
        # con = sqlite3.connect('cskipl.db')
        # cur=con.cursor()
        # sa = "CREATE TABLE IF NOT EXISTS cskteam (ID INT PRIMARY KEY NOT NULL, palyername VARCHAR(20) NOT NULL, price REAL, city CHAR(50))"
        # cur.execute(sa)
        # cur.execute("INSERT into cskteam (ID, palyername, price, city) values (?,?,?,?)", (name,ID,price,city))
        # con.commit()
        sav=ATI()
        return  sav.cskati(name, ID, price, city)

@app.route("/delCSK")
def delCSK():
    return render_template("cskdel.html")

@app.route("/delCSKP", methods=["POST"])
def delCSKP():
    if request.method=='POST':
        name = request.form['name']
        ID = request.form['id']
        sav=ATI()
        return sav.cskdel(ID)

@app.route("/suc")
def upd():
    return render_template("csk.html")

@app.route("/deleted")
def delt():
    return render_template("deletes.html")

@app.route("/deleterecord", methods=["POST"])
def deleterecord():
    id = request.form["id"]
    with sqlite3.connect("employee.db") as con:
        try:
            cur = con.cursor()
            cur.execute("delete from Employees where id = ?", id)
            msg = "record successfully deleted"
        except:
            msg = "can't be deleted"
        finally:
            return render_template("delete_record.html", msg=msg)


if __name__ == "__main__":
    app.run(debug=True)


