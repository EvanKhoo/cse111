import pytest
from triangle import compute_area
from triangle import convert_fahrenheit
def test_compute_area():
    assert(compute_area(5,6) == 30)

def test_convert_fahrenheit():
    assert(convert_fahrenheit(0) == 32)
    assert(convert_fahrenheit(500) == 932)
    assert(convert_fahrenheit(-151) == -239.8)

