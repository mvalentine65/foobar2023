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
            return ceil(exponent), 1
        else:
            return floor(exponent), -1


    power = log(n, 2)
    power, _ = _round_power_and_get_sign(power)
    steps = power
    n = abs(n - 2**power)
    # remaining distance means we got close, but n is still off
    # we can account for this by adding or subtracting earlier in the process
    # simulate the changes by adjusting the end result
    while n:
        steps += 1
        power, sign = _round_power_and_get_sign(log(n, 2))
        n = abs(n + sign * 2**power) 
        
        
    return int(steps)

#2  4  8 16 15 14 13 12 11 10
#2  4  8  9 10
#2  3  6  5 10
print(solution(10))
print(solution(4))
print(solution(15))
