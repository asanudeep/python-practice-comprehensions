from copy import deepcopy

from tutorial.excercise03 import add

def test_single_items():
    assert add([[5]], [[-2]]) == [[3]]

def test_two_by_two_matrices():
    m1 = [[6, 6], [3, 1]]
    m2 = [[1, 2], [3, 4]]
    m3 = [[7, 8], [6, 5]]
    assert add(m1, m2) == m3

def test_two_by_three_matrices():
    m1 = [[1, 2, 3], [4, 5, 6]]
    m2 = [[-1, -2, -3], [-4, -5, -6]]
    m3 = [[0, 0, 0], [0, 0, 0]]
    assert add(m1, m2) == m3


def test_input_unchanged():
    m1 = [[6, 6], [3, 1]]
    m2 = [[1, 2], [3, 4]]
    m1_original = deepcopy(m1)
    m2_original = deepcopy(m2)
    add(m1, m2)
    assert m1 == m1_original
    assert m2 == m2_original