from calculator import find_max

def test_find_max():
    assert find_max(1, 2, 3) == 3
    assert find_max(10, 5, 7) == 10
    assert find_max(-1, -2, -3) == -1
    assert find_max(0, 0, 0) == 0
