import numpy as np
import time
from random import randint, choice
from Utils import HIT, MISS, NOT_SHOT, SHIP, NOT_SHIP, can_place, \
    HORIZONTAL, VERTICAL, place_ship
from Player import BattleShipPlayer

#global limit variable to be properly assigned later
LIMIT = 1

class Bot(BattleShipPlayer):

    def __init__(self, side, ships_sizes):
        self.ships = np.full([side, side], NOT_SHIP)
        self.ship_sizes = ships_sizes
        self.generate_board(side)

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
    
    def generate_board(self, side):
        for ship_length in self.ship_sizes:
            while True:
                x = randint(0, side - 1)
                y = randint(0, side - 1)
                orientation = choice([HORIZONTAL, VERTICAL])
                if can_place(self.ships, x, y, ship_length, orientation):
                    place_ship(self.ships, x, y, ship_length, orientation)
                    break
    
    def get_board(self):
        return self.ships

    def get_bomb_coords(self, shots):
        empty = np.full([len(self.ships), len(self.ships)], NOT_SHIP)
        dist = self.get_distribution(empty, shots)
        max_x = 0
        max_y = 0
        current_max = 0
        for y in range(len(dist)):
            for x in range(len(dist)):
                if dist[y][x] > current_max:
                    max_x = x
                    max_y = y
                    current_max = dist[y][x]
                elif dist[y][x] == current_max:
                    if randint(0,2) == 1:
                        max_x = x
                        max_y = y
                        current_max = dist[y][x]
        return [max_x, max_y]
