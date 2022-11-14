import sqlite3

def connect():
    conn=sqlite3.connect("restaurant.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS FoodItem (id INTEGER PRIMARY KEY, name text, price real, inventory integer, taxable boolean, status CHARACTER(2))")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn):
    conn=sqlite3.connect("restaurant.db")
    # cur=conn.cursor()
    # cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
    # conn.commit()
    conn.close()
    view()

def view():
    conn=sqlite3.connect("restaurant.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM FoodItem")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title="",author="",year="",isbn=""):
    conn=sqlite3.connect("restaurant.db")
    # cur=conn.cursor()
    # cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
    # rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("restaurant.db")
    # cur=conn.cursor()
    # cur.execute("DELETE FROM book WHERE id=?",(id,))
    # conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn=sqlite3.connect("restaurant.db")
    # cur=conn.cursor()
    # cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
    # conn.commit()
    conn.close()

connect()
#insert("The Sun","John Smith",1918,913123132)
#delete(3)
#update(4,"The moon","John Smooth",1917,99999)
print(view())
# print(search(author="John Smooth"))
