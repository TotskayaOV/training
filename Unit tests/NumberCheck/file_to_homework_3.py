LOWER_BOUND = 25 + 1
UPPER_BOUND = 100


def even_odd_number(param):
    return param % 2 == 0


def number_in_interval(param):
    return param in range(LOWER_BOUND, UPPER_BOUND)
