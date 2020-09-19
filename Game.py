import numpy as np
from Utils import SHIP, NOT_SHOT, HIT, MISS



class Game():

    def __init__(player1, player2):
        ship_squares = sum(player1.get_board())
        side = len(player1.get_board())
        self.hp = [ship_squares, ship_squares]
        self.boards = [player1.get_board(), player2.get_board()]
        self.players = [player1, player2]
        self.shots = [
            np.full([side, side], NOT_SHOT),
            np.full([side, side], NOT_SHOT)
        ]
        self.player = 0
    
    def bomb(self, x, y):
        """
        Bomb a certain square on the board of the current opponent

        Args:
            x (int): x coordinate
            y (int): y coordinate

        Returns:
            bool: true, if the bomb was a hit
        """
        opponent = (self.player + 1) % 2

        if self.shots[self.player][y][x] != NOT_SHOT:
            raise "Can not bomb the same coordinate",x,y,"twice."
        
        hit = False
        if boards[opponent][y][x] == SHIP:
            self.hp[opponent] -= 1
            self.shots[self.player][y][x] = HIT
            hit = True
        else:
            self.shots[self.player][y][x] = MISS

        return hit
    
    def is_over(self):
        """
        Return true if either player has no unbombed ship squares left

        Returns:
            bool: true if either player has no unbombed ship squares left
        """
        return self.hp[0] * self.hp[1] == 0

    def winner(self):
        """
        Returns 0 if player 1 won, and 1 if player 2 won

        Returns:
            int: the winner
        """
        if self.hp[0] == 0:
            return 0
        elif self.hp[1] == 0:
            return 1
        else:
            raise "Game is not over"

    def next_turn(self):
        """
        Swap the currently bombing player
        """
        self.player = (self.player + 1) % 2
    
    def run(self):
        while not self.is_over():
            bomb = self.players[player].get_bomb_coords(self.shots[player])
            self.bomb(bomb[0], bomb[1])
            self.next_turn()
        print("Player", self.winner() + 1, ", you're winner!")
