def solution(n):
    from math import ceil
    from math import floor
    from math import log
    HALFWAY = log(1.5, 2)
    # any log with a decimal value higher than this constant
    # is closer to the higher multiple of 2, so round the
    # exponent up
    def _round_power_and_get_sign(exponent):
        if exponent % 1 >= HALFWAY:
            return ceil(exponent), -1
        else:
            return floor(exponent), 1


    power = log(n, 2)
    # if we go over n, we need to subtract, so sign is negative -1
    # if we stay under n, we need to add, so sign is 1
    power, sign = _round_power_and_get_sign(power)
    current = 2**power
    steps = power
    # the distance from current to n has to be less than n at this point
    # we can account for this by adding or subtracting earlier in the process
    # simulate the changes by adding the end result
    while current != n:
        delta = abs(n - current)
        current += sign * delta
        power, sign = _round_power_and_get_sign(log(delta, 2))
        steps += 1
    return steps

#2  4  8 16 15 14 13 12 11 10
#2  4  8  9 10
#2  3  6  5 10

