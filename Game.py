import numpy as np
from Utils import SHIP, NOT_SHIP, NOT_SHOT, HIT, MISS


SHIP_GRAPHICS = {
    SHIP: 'O',
    NOT_SHIP: ' '
}

SHOT_GRAPHICS = {
    NOT_SHOT: ' ',
    HIT: 'H',
    MISS: '-'
}


BOMB = 'X'

class Game():

    def __init__(self, player1, player2):
        ship_squares = np.sum(player1.get_board())
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
            raise "Can not bomb the same coordinate " + str(x) + ', ' +  str(y) + " twice."
        
        hit = False
        if self.boards[opponent][y][x] == SHIP:
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
        return (self.hp[0] * self.hp[1]) == 0

    def winner(self):
        """
        Returns 1 if player 1 won, and 2 if player 2 won

        Returns:
            int: the winner
        """
        if self.hp[0] == 0:
            return 2
        elif self.hp[1] == 0:
            return 1
        else:
            raise "Game is not over"

    def next_turn(self):
        """
        Swap the currently bombing player
        """
        self.player = (self.player + 1) % 2
    
    def print_pre_bomb(self):
        print('-------------------------------')
        pl =  str(self.player + 1)
        opponent = (self.player + 1) % 2
        opp = str(opponent + 1)
        print("Player " + pl + " is playing...")
        print("Shot history of player " + pl + ":")
        self.print_matrix(self.shots[self.player], SHOT_GRAPHICS)
        print("Ships of the opponent (player " + opp + "):")
        self.print_matrix(self.boards[opponent], SHIP_GRAPHICS)
        print("Player " + pl + " is thinking...")

    def print_bomb(self, bomb):
        pl =  str(self.player + 1)
        opponent = (self.player + 1) % 2
        opp = str(opponent + 1)
        print("Player " + pl + " bombed the coordinates:", bomb[0], bomb[1])
        self.print_matrix(self.boards[opponent], SHIP_GRAPHICS, bomb)

    def print_matrix(self, data, dictionary, bomb=None):
        side = len(data)
        print(' ', end='')
        for n in range(side):
            print('   ' + str(n), end='')
        print()
        print('  +' + '---+'*side)
        for y in range(side):
            print(y,'|', end='')
            for x in range(side):
                if bomb is not None and bomb[0] == x and bomb[1] == y:
                    print(' ' + BOMB + ' |', end='')
                else:
                    print(' ' + dictionary[data[y][x]] + ' |', end='')
            
            print()
            print('  +' + '---+'*side)
            
            

    
    def run(self, graphics=True):
        while not self.is_over():
            if graphics:
                self.print_pre_bomb()
            bomb = self.players[self.player].get_bomb_coords(self.shots[self.player])
            self.print_bomb(bomb)
            if graphics:
                self.bomb(bomb[0], bomb[1])
            self.next_turn()
            input("Press any key to move to the next turn")
        print("Player", self.winner(), "you're winner!")
        
