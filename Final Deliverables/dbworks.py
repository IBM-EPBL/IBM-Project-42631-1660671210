import sqlite3 as sql

con = sql.connect('database.db')
def insertUser(Username, Password, Email):
    try:
        con = sql.connect('database.db')
        cur = con.cursor()
        cur.execute("INSERT INTO USER (USERNAME,PASSWORD,EMAIL,HISTORY) VALUES (?,?,?,?)", (Username, Password, Email,''))
        con.commit()
        con.close()
        return True
    except:
        return False
def retreiveUsers(User):
    try:
        con = sql.connect('database.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM USER WHERE USERNAME = '"+ User +"'");
        user = cur.fetchall()
        con.close()
        return user
    except:
        return False
def updateHistory(User):
    try:
        con =  sql.connect('database.db')
        cur = con.cursor()
        cur.execute("UPDATE USER SET HISTORY = '"+ User[4] +"' WHERE EMAIL = '"+ User[3] +"';")
        con.commit()
        con.close()
        return True
    except:
        return False
def deleteAccount(User):
        con =  sql.connect('database.db')
        cur = con.cursor()
        cur.execute("DELETE FROM USER WHERE USERNAME = '"+ User +"'")
        con.commit()
        con.close()
