import sqlite3

def initialize_database(db_path: str = "measurements.db") -> None:
    connection = sqlite3.connect(db_path)

    try:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS measurements (
                id INTEGER PRIMARY KEY,
                sensor TEXT NOT NULL,
                value REAL NOT NULL,
                unit TEXT NOT NULL
            )
        """)
    finally:
        connection.close()

def add_measurement(
        sensor: str, 
        value: float, 
        unit: str,
        db_path: str = "measurements.db"
        ) -> None:
    
    connection = sqlite3.connect(db_path)
    try:
        connection.execute(
            "INSERT INTO measurements (sensor, value, unit) VALUES (?, ?, ?)",
            (sensor, value, unit)
        )
        connection.commit()
    except sqlite3.Error:
        connection.rollback()
        raise
    finally:
        connection.close()

def get_measurements(
        db_path: str = "measurements.db"
    ) -> list[tuple[int, str, float, str]]:

    connection = sqlite3.connect(db_path)
    try:
        cursor = connection.execute("SELECT * FROM measurements")
        rows = cursor.fetchall()
        return rows
    finally:
        connection.close()
        

if __name__ == "__main__":
    initialize_database("test_measurements.db")
    add_measurement(
        "temperature",
        25.0,
        "°C",
        "test_measurements.db"
    )

    print(get_measurements("test_measurements.db"))