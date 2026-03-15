from solution import square_growth_naive, square_growth

def test_normal_case_1():
        assert square_growth_naive([-2, -1, 4]) == [1, 4, 16]

def test_normal_case_2():
        assert square_growth_naive([3, 5, 9]) == [9, 25, 81]

def test_normal_case_3():
        assert square_growth_naive([-1, 0, 1, 2, 3, 19]) == [0, 1, 1, 4, 9, 361]

def test_edge_case_1():
#all negatives
        assert square_growth_naive([-8, -4, -3]) == [9, 16, 64]

def test_edge_case_2():
#empty list
        assert square_growth_naive([]) == []

def test_edge_case_3():
#zero only
        assert square_growth_naive([0]) == [0]

def test_normal_case_1_opt():
        assert square_growth([-2, -1, 4]) == [1, 4, 16]

def test_normal_case_2_opt():
        assert square_growth([3, 5, 9]) == [9, 25, 81]

def test_normal_case_3_opt():
        assert square_growth([-1, 0, 1, 2, 3, 19]) == [0, 1, 1, 4, 9, 361]

def test_edge_case_1_opt():
#all negatives
        assert square_growth([-8, -4, -3]) == [9, 16, 64]

def test_edge_case_2_opt():
#empty list
        assert square_growth([]) == []

def test_edge_case_3_opt():
#zero only
        assert square_growth([0]) == [0]