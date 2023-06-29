# must return the numerator and denominator of the first radius in a list
#   -each part must be an int

# the minimum radius of a gear is 1, the upper bound is unlimited
# the first gear must be exactly twice the size as the last gear
#   -this implies the first gear has a minimum radius of 2

# r_1 + r_2 = peg_2 - peg_2
# 2r_n = r_0
# these are linear combinations, and the 
# first and last gear have a linear relationship
# so we can model it y = mx + b
# where x is the first gear and y is the final gear
# to satisfy conditons, y = 0.5x = mx + b
# 0.5x - mx = b
# (0.5 - m)x = b
# x = b/(0.5 -m)

# m = (y_2 - y_1) / (x_2 - x_1)
# x_1, x_2 = 2, peg_1 - peg_0 - 1
# b = y_1 - 2m
# x = b / (0.5 - m)

# the proof holds
# TODO: calculate intermediate pegs
# TODO: convert decimal to fraction
# TODO: verify solution
def solution(pegs):
    from fractions import Fraction
    from fractions import gcd
    if len(pegs) < 2:  # guard: never has two gears, no 2x ratio
        return [-1, -1]
    
    def find_last_radius(radius_1):
        for i in xrange(1,len(pegs)):
            radius_2 = pegs[i] - pegs[i-1] - radius_1
            radius_1 = radius_2
        return radius_2
    # find two points
    x_1, x_2 = 2, pegs[1] - pegs[0] - 1
    y_1, y_2 = find_last_radius(x_1), find_last_radius(x_2)
    # find slope
    m = (y_2 - y_1) / (x_2 - x_1)
    # find constant
    b = y_1 - m * x_1
    # find first gear satisfying x = 2y
    x = b / (0.5 - m)
    # check for valid dimensions:
    
    if not (x_1 <= x <= x_2):
        return [-1, -1]
    # final diff check:
    def final_radius_check(radius_1):
        for i in range(1,len(pegs)):
            radius_2 = pegs[i] - pegs[i-1] - radius_1
            if radius_2 < 1:
                return False
            radius_1 = radius_2
        return True

    if not final_radius_check(x):
        return [-1, -1]
    ratio = Fraction(x).limit_denominator()
    factor = gcd(ratio.numerator, ratio.denominator)
    return [ratio.numerator / factor, ratio.denominator / factor]


if __name__ == "__main__":
    print(solution([4, 17, 50]))
    print(solution([4, 30, 50]))



