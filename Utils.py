import numpy as np

#constants for the integer grids:

#the values for misses, hits, ships and not ships are
#chosen so that if ships and shots matrices equal at
#any square, the configuration is invalid
MISS = 1
HIT = 0
NOT_SHOT = 2

SHIP = 1
NOT_SHIP = 0

HORIZONTAL = 1
VERTICAL = 2

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

def can_place(ships, x, y, length, orientation, shots=None):
    """
    Return true if a ship to be placed does not collide with other
    ships or missed shot squares

    Args:
        ships: ship matrix
        x (int): x coordinate of top left end of the ship
        y (int): y coordinate of top left end of the ship
        length (int): length of the ship
        orientation (int): HORIZONTAL (1) or VERTICAL (2)
        shots (optional): 
            shot matrix, if omitted, only collisions will be checked
    """
    for i in range(length):
        x_ = x
        y_ = y
        if orientation == HORIZONTAL:
            x_ = x + i
        else:
            y_ = y + i
        if shots is not None and shots[y_][x_] == MISS:
            return False
        if ships[y_][x_] == SHIP:
            return False
    return True

def config_limit(width, height, ship_sizes):
        """
        Return the amount of different configurations
        if the ships are allowed to overlap

        Args:
            width (int): board width
            height (int): board height
            ship_sizes (Array): List of ship sizes to place
        """
        total = 1
        for size in ship_sizes:
            total *= (width - size + 1) * height + (height - size + 1) * width
        return total

def board_is_possible(self, ships, shots):
        """
        Return true if a configuration of ships and shots are possible

        Args:
            shots: shot matrix
            ships: ship matrix
        """
        return not np.any(ships == shots)
