
HIT = 2
MISS = 1
SHIP = 1

HORIZONTAL = 1
VERTICAL = 2

'''
explanations of the grid arguments "shots" and "ships"

shots:  A board matrix where 1 indicates a miss,
        2 indicates a hit and 0 can be either

ships:  A board matrix where 1 indicates a ship and
        0 is no ship

'''

def board_is_possible(ships, shots):
    """
    Return true if a configuration of ships and shots are possible

    Args:
        shots: shot matrix
        ships: ship matrix
    """
    for y in range(len(ships)):
        for x in range(len(ships[y])):
            if shots[y][x] == HIT and ships[y][x] != SHIP:
                return False
            if shots[y][x] == MISS and ships[y][x] == SHIP:
                return False
    return True

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

def place_ship(ships, x, y, length, orientation)
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

def add_configuration(distribution, ships):
    """
    Add one to each square in the distribution that
    is occupied by a ship

    Args:
        distribution (Array):
            Matrix of integers representing the number
            of times each square has been occupied by a ship

        ships (Array):
            ship matrix
    """
    #TODO: would be faster with numpy
    for y in range(len(distribution)):
        for x in range(len(distribution[y])):
            distribution[y][x] += ships[y][x]
