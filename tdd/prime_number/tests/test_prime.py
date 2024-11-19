from prime_number.src import src

def test_prime():
    """Function that tests if 1 is a prime number
    """
    assert src.is_prime(1) is False

def test_29_prime():
    """Function which tests if 29 is a prime
    """
    assert src.is_prime(29)

def test_prime_composite_number():
    """Function which tests if 15 is a prime
    """
    assert src.is_prime(15) == False

def test_sum_of_primes_empty_list():
    assert src.sum_of_primes([]) == 0

def test_sum_of_primes_mixed_list():
    assert src.sum_of_primes([11,15,17,18,20,100]) == 28