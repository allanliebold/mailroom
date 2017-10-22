import pytest

"""Test for getting the name of a donar"""
def test_get_name_true():
    from mailroom import check_name
    assert check_name("John Snow") == True


def test_get_name_false():
    from mailroom import check_name
    assert check_name("Khal Drogo") == False
