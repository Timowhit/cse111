"""
from receipt import read_dictionary
import pytest


def test_read_dictionary():
    products_dict = read_dictionary("products.csv", 0)

    assert len(products_dict) == 16

    assert products_dict["D150"] == ["D150", "1 gallon milk", "2.85"]
    assert products_dict["D083"] == ["D083", "1 cup yogurt", "0.75"]
    assert products_dict["W112"] == ["W112", "wheat bread", "2.55"]


pytest.main(["-v", "--tb=line", "-rN", __file__])
