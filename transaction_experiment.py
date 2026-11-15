import sqlite3

connection = sqlite3.connect("transaction_test_2.db")

connection.execute("""
            CREATE TABLE IF NOT EXISTS test_values (
                id INTEGER PRIMARY KEY,
                value REAL NOT NULL
            )
        """)
try:
    connection.execute("INSERT INTO test_values (value) VALUES (?)",(42.0,))
    connection.execute("INSERT INTO test_values (value) VALUES (?)",(None,))
    connection.commit()
except sqlite3.IntegrityError:
    connection.rollback()
    print("Transaction zurueckgerollt")

cursor = connection.execute("SELECT * FROM test_values")
rows = cursor.fetchall()

print(rows)

connection.close()