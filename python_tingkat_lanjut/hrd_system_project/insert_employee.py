import os
import sqlite3

my_db = 'hrd_system_project/database/hrd_system.sqlite'
db_exist = os.path.exists(my_db)
conn = sqlite3.connect(my_db)

emp_data = [
    (1, "Budi", "Manager", 5000000, 100),
    (2, "Joko", "Supervisor", 4000000, 200),
    (3, "Tono", "Staff", 3000000, 150),
    (4, "Lina", "Supervisor", 4000000, 450),
    (5, "Budi", "Manager", 5000000, 120)
]

if db_exist:
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO employees VALUES(?, ?, ?, ?, ?)", emp_data)
    conn.commit()
    print("Employee data inserted successfully")
    
else:
    print("Database not found")

conn.close()