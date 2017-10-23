"""Mailroom Madness Tests."""
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


"""Test if create e-mail function returns correct string."""
def test_create_email():
    from mailroom import create_email
    assert create_email("John Snow", 500) == "Thank you John Snow for your donation of $500"


"""Test get donar's average donation"""
def test_get_average_donation():
    from mailroom import get_average_donation
    assert get_average_donation([20,500,10]) == '176.67'