def max_of_two(x: int,y: int) -> int:
    """Given x and y, that are 2 numbers, return the biggest number."""
    biggest: int = x
    if x >= y:
        return biggest
    else:
        biggest = y
        return biggest

def max_of_three(x: int, y: int, z: int) -> int:
    """Given x, y and z, that are 3 numbers, return the biggest number of the three."""
    biggest: int = x
    if x >=y and x>=z:
        return biggest
    elif y >= z and y>=x:
        biggest = y
        return biggest
    else:
        biggest = z
        return biggest
