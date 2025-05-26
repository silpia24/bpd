import os
import sqlite3

my_db = 'hrd_system_project/database/hrd_system.sqlite'
db_exist = os.path.exists(my_db)
conn = sqlite3.connect(my_db)

if db_exist:
    cursor = conn.cursor()
    sql = """UPDATE employees 
                SET job = ?, salary = ?, commission = ? 
                WHERE employee_id = ? """

    # data for the udpdate
    new_job = "Engineering Manager"
    new_salary = 8000000
    new_commission = 150
    employee_id = 1

    cursor.execute(sql, (new_job, new_salary, new_commission, employee_id))
    conn.commit()
    
    cursor.execute("select * from employees")
    records = cursor.fetchall()

    # print("Fetching all record from employees table after update")
    # print("\n", records)

    print("Employee data has been updated successfully")
    
else:
    print("Database not found")

conn.close()