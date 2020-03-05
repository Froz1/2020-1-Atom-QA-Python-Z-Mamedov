""" List """
import pytest


def test_append():
    """ Function to check appendig new element to the list """

    s = []
    s.append(1)
    assert len(s) == 1


def test_sum():
    """ Function to check sum of all elements of the list """

    assert sum([1, 3, 6]) == 10


def test_clear():
    """ Function to check clearing of the list """

    s = [1, 2, 3]
    s.clear()
    assert s == []


class TestList:

    @staticmethod
    def test_sort():
        """ Function to check sorting of the list """

        s = [5, 8, 18, 2]
        s.sort()
        assert s == [2, 5, 8, 18]

    @staticmethod
    @pytest.mark.parametrize('i', list(range(5)))
    def test_pop(i):
        """ :param i: index in list
Parametrized test that checks which element will be deleted.
"""
        s = [1, 8, 9, 2, 44]
        assert s[i] == s.pop(i)
