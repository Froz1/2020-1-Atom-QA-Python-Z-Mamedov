""" Set """
import pytest


def test_add():
    """ Function to check adding new element to the set """

    s = set()
    s.add(1)
    assert len(s) == 1


def test_different_items():
    """ Function to check that all items of the set are different """

    words = ['hello', 'daddy', 'hello', 'mum']
    assert set(words) == {'hello', 'daddy', 'mum'}


def test_clear():
    """ Function to check clearing of the set """

    s = {1, 2, 3}
    s.clear()
    assert s == set()


class TestSet:

    @staticmethod
    def test_copy():
        """ Function to check of copy of the set """

        s = {5, 8, 18, 2}
        v = s.copy()
        assert v == s

    @staticmethod
    @pytest.mark.parametrize('other_set', [{1, 2, 5, 1, 6, 2},
                                           {1, 1, 1, 5, 2, 6}])
    def test_equality(other_set):
        """ :param other_set: sets for comparing
Parametrized test which checks that these sets are equal.
"""
        s = {1, 2, 5, 6}
        assert s == other_set
