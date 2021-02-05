import json
import sqlite3

def connect():
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTs products (id INTEGER PRIMARY KEY , name TEXT , quantity INTEGER, chategory TEXT )")
    conn.commit()
    conn.close()

def insert(name,quantity,chategories):
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    for i in chategories:
        cur.execute("INSERT INTO products VALUES (NULL, ?,?,?)",(name,quantity,i))
    conn.commit()
    conn.close()
    view()

def view():
    view_result=[]
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    cur.execute("SELECT name , quantity FROM products GROUP BY name ")
    row=cur.fetchall() 
    print(row)
    #print(type(row))
    '''for i in row:
        cur.execute("SELECT chategory FROM products WHERE name==?",(i))
        rows=cur.fetchall()
        cur.execute("SELECT DISTINCT quantity FROM products WHERE name==?",(i))
        rows1=cur.fetchall()
        #print(rows)
        #print(rows1)
        #print(type(i))
        view_result=list(i)+rows+rows1
        print(type(view_result))
        #print(view_result)'''


    conn.close()
    return row
    #print(row)


connect()