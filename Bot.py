import numpy as np
import time
from Utils import HIT, MISS, NOT_SHOT, SHIP, NOT_SHIP
from Player import BattleShipPlayer

HORIZONTAL = 1
VERTICAL = 2

#global limit variable to be properly assigned later
LIMIT = 1

class Bot(BattleShipPlayer):

    def __init__(side):
        ships = np.full([side, side], NOT_SHIP)

    def get_distribution(self, ships, shots, ship_sizes):
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
