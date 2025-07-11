from tutorial.excercise01 import square_evens

def test_basic_case():
    input_list = [1, 2, 3, 4]
    expected = [4, 16]
    assert square_evens(input_list) == expected

def test_empty_list():
    input_list = []
    expected = []
    assert square_evens(input_list) == expected

def test_odds_only():
    input_list = [1, 3, 5]
    expected = []
    assert square_evens(input_list) == expected