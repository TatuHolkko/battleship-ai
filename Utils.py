#constants for the integer grids:

#the values for misses, hits, ships and not ships are
#chosen so that if ships and shots matrices equal at
#any square, the configuration is invalid
MISS = 1
HIT = 0
NOT_SHOT = 2

SHIP = 1
NOT_SHIP = 0

'''
explanations of the grid arguments "shots" and "ships"

shots:  A board matrix where 1 indicates a miss,
        2 indicates a hit and 0 can be either

ships:  A board matrix where 1 indicates a ship and
        0 is no ship. This represents the current guess
        where the ships could be

'''

def place_ship(ships, x, y, length, orientation):
    """
    Place a ship into the ships array. This function does not
    check if the placement is legal or not.

    Args:
        ships: ship matrix
        x (int): x coordinate of top left end of the ship
        y (int): y coordinate of top left end of the ship
        length (int): length of the ship
        orientation (int): HORIZONTAL (1) or VERTICAL (2)
    """
    for i in range(length):
        x_ = x
        y_ = y
        if orientation == HORIZONTAL:
            x_ = x + i
        else:
            y_ = y + i

        ships[y_][x_] = SHIP

def can_place(ships, shots, x, y, length, orientation):
    """
    Return true if a ship to be placed does not collide with other
    ships or missed shot squares

    Args:
        ships: ship matrix
        shots: shot matrix
        x (int): x coordinate of top left end of the ship
        y (int): y coordinate of top left end of the ship
        length (int): length of the ship
        orientation (int): HORIZONTAL (1) or VERTICAL (2)
    """
    for i in range(length):
        x_ = x
        y_ = y
        if orientation == HORIZONTAL:
            x_ = x + i
        else:
            y_ = y + i
        if shots[y_][x_] == MISS:
            return False
        if ships[y_][x_] == SHIP:
            return False
    return True