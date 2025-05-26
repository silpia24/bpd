import os
import sqlite3
import datetime

my_db = 'hrd_system_project/database/hrd_system.sqlite'
db_exist = os.path.exists(my_db)
conn = sqlite3.connect(my_db)

x = datetime.datetime.now()
payroll_date = x.strftime('%Y-%m-%d')

emp_data = [
    (101, payroll_date, 1, 5000000),
    (102, payroll_date, 2, 4000000),
    (103, payroll_date, 3, 3000000),
    (104, payroll_date, 4, 4000000),
    (105, payroll_date, 5, 5000000)
]

if db_exist:
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO payroll VALUES(?, ?, ?, ?)", emp_data)
    conn.commit()
    print("Payroll data inserted successfully")
    
else:
    print("Database not found")

conn.close()