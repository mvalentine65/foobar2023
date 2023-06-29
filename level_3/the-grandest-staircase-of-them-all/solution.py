def solution(bricks):
    """Calculates the number of possible stairs based on bricks.

    Accepts a number of bricks. Returns the number of staircases which can
    be made using all the provided bricks. Each staicase must have at least
    two steps. Each step must be taller than the previous step. No bricks can
    be left unused.

    Bricks will always be more than 1 and less than 200.
    """
    if bricks < 3:
        return 0
    array = [0]*(bricks + 1)
    array[0] = 1
    for i in xrange(1,bricks + 1):
        for j in xrange(bricks, i-1, -1):
            array[j] += array[j-i]
    return array[-1] - 1
    

print(solution(3))
print(solution(4))
print(solution(5))
print(solution(6))
print(solution(7))
