    """
    An abstract base class for an object that can be used as a player in a battleship
    """
    import abc

    class BattleShipPlayer(abc.ABC):
        
        @abc.abstractclassmethod
        def get_bomb_coords(self, shots):
            """
            This function returns coordinates at which this player
            wants to bomb, by looking at the given shot matrix

            Args:
                shots: shot matrix

            Returns:
                [int, int]: coordinates in the form of [x, y]
            """
            pass

        def get_board(self):
            """
            Returns the ship matrix that the player wants to start playing with

            Returns:
                the ship matrix that the player wants to start playing with
            """
            pass
