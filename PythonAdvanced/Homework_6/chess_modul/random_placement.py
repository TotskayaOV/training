from random import randint as rnd
from .checking_placement import start_pr

def generic_placement(num):
    result = []
    while True:
        position_list =[(rnd(1, num), rnd(1, num)) for _ in range(num)]
        if len(set(position_list)) == num:
            check = start_pr(num, position_list)
            if check:
                result.append(position_list)
            if len(result) == 4:
                return result
