import numpy as np
import time

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

#global limit variable to be properly assigned later
LIMIT = 1

'''
explanations of the grid arguments "shots" and "ships"

shots:  A board matrix where 1 indicates a miss,
        2 indicates a hit and 0 can be either

ships:  A board matrix where 1 indicates a ship and
        0 is no ship. This represents the current guess
        where the ships could be

'''

def board_is_possible(ships, shots):
    """
    Return true if a configuration of ships and shots are possible

    Args:
        shots: shot matrix
        ships: ship matrix
    """
    return not np.any(ships == shots)

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

def get_distribution(ships, shots, ship_sizes):
    """
    Returns a numpy array that contains in each square the number of times
    the square was occupied by a ship out of all possible configurations

    Args:
        ships: ship matrix
        shots: shot matrix
        ship_sizes (Array): list of ship sizes that should be placed

    Returns:
        np.array: 
            a numpy array that contains in each square the number of times
            the square was occupied by a ship out of all possible 
            configurations
    """
    board_width = len(ships)
    board_height = len(ships[0])
    distr = np.zeros([board_height, board_width])
    ship_size = ship_sizes[-1]
    for orientation in [HORIZONTAL, VERTICAL]:
        
        #in the direction parallel to the ship the amount
        #of possible locations is restricted by the ships length
        y_max = board_height
        x_max = board_width
        if orientation == HORIZONTAL:
            x_max = board_width - ship_size + 1
        else:
            y_max = board_height - ship_size + 1

        for y in range(y_max):
            for x in range(x_max):
                
                if not can_place(ships, shots, x, y, ship_size, orientation):
                    continue
                
                new_ships = np.copy(ships)
                place_ship(new_ships, x, y, ship_size, orientation)
                new_ship_sizes = ship_sizes[:-1]

                if len(new_ship_sizes) == 0:
                    #all ships placed
                    if board_is_possible(new_ships, shots):
                        #the board is possible
                        #add one to each square occupied by a ship
                        distr = distr + new_ships
                else:
                    distr += get_distribution(new_ships, shots, new_ship_sizes)
        
    return distr

def info(config_finished=True):
    pass


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


ships = np.full([7,7],NOT_SHIP)
shots = np.full([7,7],NOT_SHOT)
ship_sizes = [2,3,4,5]

start = time.time()
print("Limit of configurations with collisions:", config_limit(7,7, ship_sizes))
print(get_distribution(ships, shots, ship_sizes))
print(time.time() - start)
