import pytest

from testFuel.fuel import convert, gauge


def test_check_half():
    assert convert("5/10") == 50


def test_check_three_quarter():
    assert convert("3/4") == 75


def test_check_empty():
    assert gauge(1) == "E"


def test_check_full():
    assert gauge(99) == "F"


def test_check_inbetween():
    assert gauge(60) == "60%"


def test_ve():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')


def test_value():
    with pytest.raises(ValueError):
        convert('dog/cat')