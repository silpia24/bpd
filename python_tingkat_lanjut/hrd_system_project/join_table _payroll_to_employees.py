import sqlite3

try:
    # Menggunakan 'with' statement untuk manajemen koneksi dan transaksi otomatis.
    # conn.commit() akan dipanggil jika blok ini selesai tanpa error.
    # conn.rollback() akan dipanggil jika terjadi error di dalam blok ini.
    with sqlite3.connect("hrd_system_project/database/hrd_system.sqlite") as conn:
        cursor = conn.cursor()

        cursor.execute("PRAGMA foreign_keys = ON;")

        # Check if tabel 'payroll' already exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='payroll'")
        tabel_payroll_exist = cursor.fetchone() is not None

        if tabel_payroll_exist:
            print("Table 'payroll' already exist. Trying to modify and migrate data...")

            # 1. Create temporary table with new scheme (employee_id as foreign key)
            cursor.execute('''
                CREATE TABLE payroll_temp (
                    payroll_id INTEGER NOT NULL PRIMARY KEY,
                    payroll_date TEXT NOT NULL,
                    employee_id INTEGER NOT NULL,
                    total_amount INTEGER NOT NULL,
                    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
                );
            ''')

            # 2. Migrate data from old table to new table
            cursor.execute('''
                INSERT INTO payroll_temp (payroll_id, payroll_date, employee_id, total_amount)
                SELECT payroll_id, payroll_date, employee_id, total_amount FROM payroll;
            ''')

            # 3. Delete old table
            cursor.execute("DROP TABLE payroll")

            # 4. Change temporary table name to 'payroll'
            cursor.execute("ALTER TABLE payroll_temp RENAME TO payroll")
            
            print("Table 'payroll' successfully modified and data migrated.")

        else:
            print("Tabel 'payroll' tidak ditemukan. Membuat tabel baru...")
            # If table 'payroll' doesn't exist, create it
            cursor.execute('''
                CREATE TABLE payroll (
                    payroll_id INTEGER NOT NULL PRIMARY KEY,
                    payroll_date TEXT NOT NULL,
                    employee_id INTEGER NOT NULL,
                    total_amount INTEGER NOT NULL,
                    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
                );
            ''')
            print("Tabel 'payroll' berhasil dibuat.")
        
        if cursor:
            cursor.close()

except sqlite3.Error as e:
    print(f"Error occurred: {e}")
finally:
    print("Database operations completed.")