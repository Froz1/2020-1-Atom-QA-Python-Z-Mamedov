""" Dictionary """
import pytest


def test_empty_dict():
    """ Function to check creating of the empty dict """

    d = dict()
    assert d == {}


def test_update():
    """ Function to check updating of the dict after adding subdict to it """

    d = {1: 2, 2: 4, 3: 9}
    d.update({4: 16})
    assert d == {1: 2, 2: 4, 3: 9, 4: 16}


def test_clear():
    """ Function to check clearing of the dict """

    d = {1: 2, 2: 4, 3: 9}
    d.clear()
    assert d == {}


class TestDict:

    @staticmethod
    def test_copy():
        """ Function to check creating the copy of the dict """

        d = {1: 2, 2: 4, 3: 9}
        v = d.copy()
        assert v == d

    @staticmethod
    @pytest.mark.parametrize('i', list(range(1, 4)))
    def test_pop(i):
        """ :param i: key in dict
Parametrized test that checks which element will be deleted.
"""
        d = {1: 2, 2: 4, 3: 9}
        assert d[i] == d.pop(i)
