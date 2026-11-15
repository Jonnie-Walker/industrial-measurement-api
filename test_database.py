from database import initialize_database, add_measurement, get_measurements
import pytest
import sqlite3

def test_add_measurement(tmp_path):
    
    db_path = tmp_path / "test.db"
    
    initialize_database(str(db_path))

    add_measurement(
            "temperature",
            27.5,
            "°C",
            str(db_path)
        )

    rows = get_measurements(str(db_path))

    assert len(rows) == 1
    assert rows[0][1:] == ("temperature", 27.5, "°C")

def test_empty_database(tmp_path):

    db_path = tmp_path / "test.db"
        
    initialize_database(str(db_path))

    rows = get_measurements(str(db_path))

    assert rows == []

def test_multiple_measurements(tmp_path):

    db_path = tmp_path / "test.db"
        
    initialize_database(str(db_path))

    add_measurement("temperature", 23.5, "°C", str(db_path))
    add_measurement("pressure", 6.2, "bar", str(db_path))
    add_measurement("humidity", 65.0, "%", str(db_path))

    rows = get_measurements(str(db_path))

    assert len(rows) == 3

    measurements = [row[1:] for row in rows]

    assert set(measurements) == {("temperature", 23.5, "°C"),
                         ("pressure", 6.2, "bar"),
                         ("humidity", 65.0, "%")
                         }

def test_add_measurement_without_table(tmp_path):
    db_path = tmp_path / "test.db"

    with pytest.raises(sqlite3.OperationalError, match="no such table: measurements"):
        add_measurement("temperature", 25.0, "°C", str(db_path))
