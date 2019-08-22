import unnecessary_math as math


def test_numbers_3_4():
    assert math.multiply(3, 4) == 12


def test_strings_a_3():
    assert math.multiply("a", 3) == "aaa"


def test_numbers_1_3():
    assert math.sum(1, 3) == 4

