import math

def is_prime(x:int)->bool:
    """Function that calculates if a number is a prime or not

    Args:
        x (_int): integer which will be tested

    Returns:
        bool: True if the integer is a prime number, False otherwise
    """

    # Prime numbers should be greater than 2
    if x <2:
        return False
    
    for n in range(2, math.floor(math.sqrt(x)+1)):
        if x%n == 0:
            return False

    return True

def sum_of_primes(nums):
    return sum([x for x in nums if is_prime(x)])