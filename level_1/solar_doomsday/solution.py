def solution(area: int) -> list:
    """
    Given a total area of solar paneling, find the largest possible panels
    that can be created.
    """
    # This task is basically the same as the coin question
    # except we have to find the area of the panels each iteration.
    # Finding the square root of the reamining area and truncating the
    # decimals should do the trick.
    from math import sqrt
    panels = []
    while area:
        panel = int(sqrt(area)) ** 2
        panels.append(panel)
        area -= panel
    return panels
