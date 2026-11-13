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

def test_calculate_std_dev():
    assert result["std_dev"] == 10.0

def test_std_dev_single_value():
    assert calculate_statistics([20.0])["std_dev"] == 0.0
