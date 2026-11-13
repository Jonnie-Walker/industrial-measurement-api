import pytest

from measurement_statistics import calculate_statistics

measurements = [10.0, 20.0, 30.0]

result = calculate_statistics(measurements)

def test_calculate_mean():
    assert result["mean"] == 20.0

def test_calculate_count():
    assert result["count"] == 3

def test_calculate_minimum():
    assert result["minimum"] == 10.0

def test_calculate_maximum():
    assert result["maximum"] == 30.0

def test_empty_list():
    with pytest.raises(ValueError):
        calculate_statistics([])