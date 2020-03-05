""" String """
import pytest


def test_add():
    """ Function to check addition of two strings """

    s1 = 'atmo'
    s2 = 'sphere'
    assert s1 + s2 == 'atmosphere'


def test_extracting_slice():
    """ Function to check extracting of tge slice from the string """

    s = 'atmosphere'

    assert s[4:] == 'sphere'


def test_split():
    """ Function to check spliting the string on the elements. """

    s = '1 2 3'
    assert s.split() == ['1', '2', '3']


class TestString:

    @staticmethod
    def test_upper():
        """ Function to check converting a string to uppercase """

        s = 'string'
        assert s.upper() == 'STRING'

    @staticmethod
    @pytest.mark.parametrize('string', '123')
    def test_check_symbols(string):
        """ :param string: one string
Parametrized test that checks if string consist of digits.
"""
        assert string.isdigit()
