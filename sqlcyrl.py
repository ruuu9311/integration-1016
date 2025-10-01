import sqlite3

conn = sqlite3.connect('product_init.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM product_init')

sqlins="""
INSERT INTO "main"."product_init"
("name","version","remark")
VALUES('Laptop','ASUS','U R ASUS')
"""
cursor.execute(sqlins)

records = cursor.fetchall()
conn.commit()
print(records)
# execute sqlcryl.py 
#1:in terminal: python sqlcryl.py
#2:in terminal: python3 sqlcryl.py
#3:in VSCode: click 'Run Python File' 