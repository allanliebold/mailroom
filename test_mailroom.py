import pytest

"""Test for getting the name of a donar"""
def test_get_name():
    from mailroom import check_name
    assert check_name("John Smith") == False 