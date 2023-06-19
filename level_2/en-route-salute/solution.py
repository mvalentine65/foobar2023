def solution(s):
    """Returns the number of salutes done in a hallway.

    Accepts a string "s" which represents a hallway full of bunny guards.
    Each string will be some combination of three different characters:
        "-": an empty space in the hallway
        ">": a right facing guard
        "<": a left facing guard
    Guards move in the direction they face and stop to salute any time they
    run into a guard moving in the opposite direction. Since each guard salutes,
    the event makes two salutes.
    """

    salutes_done = 0
    possible_salutes = 0
    
    for char in s:
        if char == ">":
            possible_salutes += 2
        elif char == "<":
            salutes_done += possible_salutes 
    return salutes_done

print(solution("<<>><"))
print(solution(">----<"))
