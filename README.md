# battleship-ai
## Goal
The goal of this project is to build an artifical intelligence that plays battleship by calculating the probabilities of ships being in each square, assuming the opponent's ship placements are completely random.
## The basis for choosing the best coordinate
The probability of a certain squre being occupied by a ship is calculated with a recursive function that takes the following as parameters

1. Matrix that describes squares that are blocked and squares that are confirmed hits
    * Blocked squares are the ones that dont have a missed hit or a ship in them
    * Confirmed hit squares are confirmed to have a ship occupying them

2. The list of ships to be placed on the board

and returns a matrix that contains the number of times each square was occupied through out all possible configurations of ships.


## The algorithm
1. Pick the largest unplaced ship and initialize a distribution matrix to zero
2. Pick a position that has not been tested for the ship that is inside the board, if there are no new positions, go to step 6
3. Place the ship in the board
    * If the board is illegal continue to the next position
4. If there are still unplaced ships
    * Make a recursive call to step 1 with the new board and the rest of the ships
    * Add the return value to the current distribution matrix
    * Go to the next position
5. If all ships have been placed
    * Add one to each square occupied by a ship in the distribution matrix
    * Go to the next position
6. Return the distribution

### The same algorithm in pseudo code:
```
get_distribution(board, ships){
    distribution = (board full of zeros)
    ship = ships.get_largest()
    for vertical and horizontal orientation {
        for each position in board {
            if not board.can_place(position, ship){
                continue
            }
            new_board = board.place(position, ship)
            new_ships = ships.remove(ship)
            if ships.size() == 0 {
                #all ships have been placed
                if configuration is new {
                    distribution.add(board)
                }
            } else {
                distribution.add(get_distribution(new_board, new_ships))
            }
        }
    }
}
``` 