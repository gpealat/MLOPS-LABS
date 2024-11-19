from prime_number.src import src

def test_prime():
    """Function that tests if 1 is a prime number
    """
    assert src.is_prime(1) is False

def test_29_prime():
    """Function which tests if 29 is a prime
    """
    assert src.is_prime(29)