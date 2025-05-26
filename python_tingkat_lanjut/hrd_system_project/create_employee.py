import sqlite3

# connect to db
with sqlite3.connect("hrd_system_project/database/hrd_system.sqlite") as conn:
    cursor = conn.cursor()

    # create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            employee_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            job TEXT NOT NULL,
            salary INTEGER NOT NULL,
            commission INTEGER NOT NULL,
            PRIMARY KEY (employee_id)
    );
    ''')

    # commit changes
    conn.commit()
    print("employee table was created successfully")
    cursor.close()