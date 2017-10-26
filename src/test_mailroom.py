"""Mailroom Madness Tests."""
import pytest

"""Test for getting the name of a donar"""


def test_get_name_true():
    """Test of the check_name function.

    Should return True if a passed name is in the donor_list dictionary.
    """
    from mailroom import check_name
    assert check_name("John Snow") is True


def test_get_name_false():
    """Test a name that is not in the donor_list dictionary."""
    from mailroom import check_name
    assert check_name("Khal Drogo") is False


def test_is_valid_donation_is_true():
    """Test if donation amount is valid number."""
    from mailroom import check_donation
    assert check_donation("500") is True


def test_is_valid_donation_is_false():
    """Test if donation amount entered cannot be made into an int."""
    from mailroom import check_donation
    with pytest.raises(ValueError):
        check_donation("xxxx")


def test_create_email():
    """Test if create e-mail function returns correct string."""
    from mailroom import create_email
    assert create_email("John Snow", 500) == "Thank you John Snow for your donation of $500"


def test_get_average_donation():
    """Test get donor's average donation."""
    from mailroom import get_average_donation
    assert get_average_donation([20, 500, 10]) == '176.67'
