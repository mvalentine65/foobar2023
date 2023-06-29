def solution(n):
    # using log2 isnt working
    # if we're basing this on powers of two,
    # just mess with the binary itself
    # I'll never admit this in public,
    # but sometimes the EE is right
    steps = 0
    n = long(n)
    while n != 1:
        # no trailing 1, n is even
        if n & 1 == 0:
            n = n >> 1
        
        # all these cases are odd numbers
        # trailing 1 assumed to exist

        # normally we add in case of 11, but this breaks on 3
        # so decrement it to two
        elif n == 3:
            n -= 1

        elif (n >> 1) & 1 == 0:
            n -= 1

        # multiple 1 bits at the end
        # add 1 to overflow and make them all zero
        else:
            n += 1

        steps += 1
    return steps
