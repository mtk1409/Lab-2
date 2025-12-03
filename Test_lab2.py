import Lab2 as LAB2


def test_FindMinMax():
    expected = [1, 5]
    test_arr = [2, 4, 3, 5, 1]
    result = LAB2.find_min_max(test_arr)
    assert(result == expected)


def test_CalcAverage():
    expected = 4.86
    test_arr = [2, 9, 3, 7, 1, 8, 4]  # Avg = 4.857142857
    result = LAB2.calc_average(test_arr)
    assert(result == expected)


def test_Median_Odd():
    expected = 4
    test_arr = [2, 9, 3, 7, 1, 8, 4]
    result = LAB2.calc_median_temperature(test_arr)
    assert(result == expected)


def test_Median_Even():
    expected = 3.5
    test_arr = [2, 3, 7, 1, 8, 4]
    result = LAB2.calc_median_temperature(test_arr)
    assert(result == expected)