import sqlite3

# connect to db
with sqlite3.connect("hrd_system_project/database/hrd_system.sqlite") as conn:
    cursor = conn.cursor()

    # create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS payroll (
            payroll_id INTEGER NOT NULL,
            payroll_date TEXT NOT NULL,
            employee_id INTEGER NOT NULL,
            total_amount INTEGER NOT NULL,
            PRIMARY KEY (Payroll_id)
        );
    ''')

    # commit changes
    conn.commit()
    print("payroll table was created successfully")
    cursor.close()