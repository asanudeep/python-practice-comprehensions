from tutorial.excercise02 import flatten_2d

def test_basic_case():
    matrix = [[1, 2], [3, 4]]
    expected = [1, 2, 3, 4]
    assert flatten_2d(matrix) == expected

def test_single_row():
    matrix = [[1, 2, 3]]
    expected = [1, 2, 3]
    assert flatten_2d(matrix) == expected

def test_single_column():
    matrix = [[1], [2], [3]]
    expected = [1, 2, 3]
    assert flatten_2d(matrix) == expected

def test_empty_lists_inside():
    matrix = []
    expected = []
    assert flatten_2d(matrix) == expected

def test_large_matrix():
    matrix = [[i for i in range(10)] for _ in range(5)]
    expected = list(range(10)) * 5
    assert flatten_2d(matrix) == expected