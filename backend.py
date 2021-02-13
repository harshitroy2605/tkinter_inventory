import json
import sqlite3
from tkinter import messagebox

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

def display_list(name=""):
    #print(name)
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    cur.execute("SELECT DISTINCT chategory FROM products WHERE name=?",(name,))
    row=cur.fetchall()
    chategory=str(row)
    #print(type(row))
    chategory=chategory.replace('[','')
    chategory=chategory.replace('(','')
    chategory=chategory.replace("'",'')
    chategory=chategory.replace(',','')
    chategory=chategory.replace(']','')
    chategory=chategory.replace(')','')

    print(chategory)
    #chategory=''.join(e for e in chategory if e.isalnum())
    cur.execute("SELECT DISTINCT quantity FROM products WHERE name=?",(name,))
    rows=cur.fetchall()
    quantity=str(rows)
    quantity=''.join(e for e in quantity if e.isalnum())


    conn.close()
    messagebox.showinfo("showinfo",'name : '+name+'\n'+'quantity : '+quantity+'\n'+'chategory : '+chategory)

def search(name="",chategory=""):
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    cur.execute("SELECT DISTINCT name , quantity , chategory FROM products WHERE name=? OR chategory=?",(name,chategory))
    row=cur.fetchall()
    conn.close()
    return row



def update(name,quantity,chategory,chategory_list):
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    cur.execute("UPDATE products SET name=? , quantity=? where name=?",(name,quantity,name))
    if chategory_list is not None:
        for i in chategory_list:
            cur.execute("INSERT INTO products VALUES (NULL, ?,?,?)",(name,quantity,i))
    conn.commit()
    conn.close()




def view():
    view_result=[]
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    cur.execute("SELECT name FROM products GROUP BY name ")
    row=cur.fetchall() 
    #print(row)
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