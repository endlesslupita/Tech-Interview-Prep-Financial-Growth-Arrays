from solution.py import square_growth_naive, square_growth

def test_normal_case_1():
        assert square_growth_naive() == [-2, 4, 16]

def test_normal_case_2():
        assert square_growth_naive() == [3, 5, 9]

def test_normal_case_3():
        assert square_growth_naive() == [-1, 0, 1, 2, 3, 19]

def test_edge_case_1():
        assert square_growth_naive() == [-8, -4, -3]

def test_edge_case_2():
        assert square_growth_naive() == []

def test_edge_case_3():
        assert square_growth_naive() == [0]