
def divisible_by(n):
    """
        Function that returns a lambda function that checks if a given number is divisible by n
    """
    return lambda x: x % n == 0
