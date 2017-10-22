import pytest

"""Test for getting the name of a donar"""
def test_get_name_true():
    from mailroom import check_name
    assert check_name("John Snow") == True


def test_get_name_false():
    from mailroom import check_name
    assert check_name("Khal Drogo") == False

"""Test if donation amount is valid number """
def test_is_valid_donation_is_true():
    from mailroom import check_donation
    assert check_donation("500") == True

def test_is_valid_donation_is_false():
    from mailroom import check_donation
    assert check_donation("xxx") == False

