from fizzbuzz import fizz_buzz, fizz_buzz_2


arg_to_expected = [
    (1, "1"),
    (3, "fizz"),
    (4, "4"),
    (5, "buzz"),
    (6, "fizz"),
    (10, "buzz"),
    (15, "fizzbuzz"),
    (30, "fizzbuzz"),
]


def test_fizz_buzz():
    for arg, expected in arg_to_expected:
        assert fizz_buzz(arg) == expected


def test_fizz_buzz_2():
    for arg, expected in arg_to_expected:
        assert fizz_buzz_2(arg) == expected
