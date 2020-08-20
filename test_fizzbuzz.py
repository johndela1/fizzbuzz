from fizzbuzz import fizz_buzz


def test_fizz_buzz():
    assert fizz_buzz(1) == "1"
    assert fizz_buzz(3) == "fizz"
    assert fizz_buzz(5) == "buzz"
    assert fizz_buzz(6) == "fizz"
    assert fizz_buzz(10) == "buzz"
    assert fizz_buzz(15) == "fizzbuzz"
    assert fizz_buzz(30) == "fizzbuzz"
