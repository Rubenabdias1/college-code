import sqlite3

def connect():
    conn=sqlite3.connect("restaurant.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS FoodItem (id INTEGER PRIMARY KEY, name text, price real, inventory integer, taxable boolean, status CHARACTER(2))")
    conn.commit()
    conn.close()

def insert(name,price,inventory,taxable):
    conn=sqlite3.connect("restaurant.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO FoodItem VALUES (NULL,?,?,?,?,?)",(name,price,inventory,taxable, "A"))
    conn.commit()
    conn.close()
    view()

def view():
    conn=sqlite3.connect("restaurant.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM FoodItem")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(name="",price="",inventory="",taxable=""):
    conn=sqlite3.connect("restaurant.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM FoodItem WHERE name=? OR price=? OR inventory=? OR taxable=?", (name,price,inventory,taxable))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("restaurant.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM FoodItem WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,name,price,inventory,taxable):
    conn=sqlite3.connect("restaurant.db")
    cur=conn.cursor()
    cur.execute("UPDATE FoodItem SET name=?, price=?, inventory=?, taxable=? WHERE id=?",(name,price,inventory,taxable,id))
    conn.commit()
    conn.close()

connect()
#insert("The Sun","John Smith",1918,913123132)
#delete(3)
#update(4,"The moon","John Smooth",1917,99999)
print(view())
# print(search(price="John Smooth"))
