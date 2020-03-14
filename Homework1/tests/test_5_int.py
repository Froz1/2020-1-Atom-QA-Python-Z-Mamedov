""" Int """
import pytest


def test_sum():
    """ Function to check addition of two numbers """

    a1 = 4
    a2 = 5
    assert a1 + a2 == 9


def test_pow():
    """ Function to check pow """

    assert pow(2, 3) == 8


def test_div():
    """ Function to check getting the whole part from division """

    assert 5 // 2 == 2


class TestList:

    @staticmethod
    def test_abs():
        """ Function to check getting of number module """

        assert abs(-5) == 5

    @staticmethod
    @pytest.mark.parametrize('i', list(range(5)))
    def test_not_equal_6(i):
        """ :param i: integer
Parametrized test which checks that numbers aren't equal 6.
"""
        assert i != 6
