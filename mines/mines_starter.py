# NO IMPORTS ALLOWED!

def new_game(num_rows, num_cols, bombs):
    """Start a new game. Should return a dictionary with the following keys:
       * `dimensions`
       * `state`
       * `board`
       * `visible`

    Each of these should be as described in the handout.
    Parameters:
       num_rows (int): Number of rows
       num_cols (int): Number of columns
       bombs (list/tuple): List of bombs, given in (row, column) pairs (tuples)
    """

    # initialize the game board
    board = []
    for i in range(num_rows):
        one_row = []
        for j in range(num_cols):
            one_row.append(0)
        board.append(one_row)

    # initialize the game visiblity board
    visible = []
    for i in range(num_rows):
        one_row = []
        for j in range(num_cols):
            one_row.append(False)
        visible.append(one_row)

    # insert bombs to the board
    for row in range(num_rows):
        for col in range(num_cols):
            if (row,col) in bombs or [row,col] in bombs:
                board[row][col] = '.'
                
    # for each non-bomb cell, count the number of bombs around this cell
    # and make the corresponding cell be that number
    for row in range(num_rows):
        for col in range(num_cols):
            if board[row][col] != '.':
                
                num_bombs = 0

                # find neighboring locations

                neighbors = []
                coord1 = [row - 1, col - 1]

                if coord1[0]>=0 and coord1[0]<num_rows:
                    if coord1[1]>=0 and coord1[1]<num_cols:
                        neighbors.append(coord1)

                coord2 = [row - 1, col]

                if coord2[0]>=0 and coord2[0]<num_rows:
                    if coord2[1]>=0 and coord2[1]<num_cols:
                        neighbors.append(coord2)

                coord3 = [row - 1, col + 1]

                if coord3[0]>=0 and coord3[0]<num_rows:
                    if coord3[1]>=0 and coord3[1]<num_cols:
                        neighbors.append(coord3)

                coord4 = [row, col - 1]

                if coord4[0]>=0 and coord4[0]<num_rows:
                    if coord4[1]>=0 and coord4[1]<num_cols:
                        neighbors.append(coord4)

                coord5 = [row, col + 1]

                if coord5[0]>=0 and coord5[0]<num_rows:
                    if coord5[1]>=0 and coord5[1]<num_cols:
                        neighbors.append(coord5)

                coord6 = [row + 1, col - 1]

                if coord6[0]>=0 and coord6[0]<num_rows:
                    if coord6[1]>=0 and coord6[1]<num_cols:
                        neighbors.append(coord6)

                coord7 = [row + 1, col]

                if coord7[0]>=0 and coord7[0]<num_rows:
                    if coord7[1]>=0 and coord7[1]<num_cols:
                        neighbors.append(coord7)

                coord8 = [row + 1, col + 1]  

                if coord8[0]>=0 and coord8[0]<num_rows:
                    if coord8[1]>=0 and coord8[1]<num_cols:
                        neighbors.append(coord8)

                
                # count bombs in neighboring locations

                for i in range(len(neighbors)):
                    r, c = neighbors[i]
                    if board[r][c] == '.':
                        num_bombs += 1                       
                
                board[row][col] = num_bombs
         
    game = {
                "dimensions": (num_rows, num_cols),
                "state": "ongoing",
                "board": board,
                "visible": visible
            }

    return game



def dump(game):
    """
    Print a human-readable representation of this game. You can use this to check your code
    if it's helpful!
    """

    lines = ["dimensions: {}".format(game['dimensions']),
             "board: {}".format("\n       ".join(map(str, game["board"]))),
             "visible:  {}".format("\n       ".join(map(str, game["visible"]))),
             "state: {}".format(game['state']),
             ]
    print("\n".join(lines))


def dig(game, row, col):
    """
    Recursively dig up (row, col) and neighboring squares.
    Update game["visible"] to reveal (row, col); then recursively reveal (dig up)
    its neighbors, as long as (row, col) does not contain and is not adjacent
    to a bomb.  Return an integer indicating how many new squares were
    revealed.
    Parameters:
       game (dict): game represented as a dictionary, same format as new_game
       row (int): Where to start digging (row)
       col (int): Where to start digging (col)
    Returns:
       int: the number of new squares revealed
    """
    raise NotImplementedError     
    
def check_game_over(game):
    """
    Two things need to happen: game["state"] should change and the function
    should return if the game is over or not.

    The state of the game should be changed to "defeat" if at least one bomb
    is visible on the board, "victory" when all safe squares (squares that 
    do not contain a bomb) and no bombs are visible, and "ongoing" otherwise.

    Function should return True if the game is over (i.e. victory or defeat has happened), 
    and False otherwise (i.e. if the game is still ongoing)
    """
    raise NotImplementedError

if __name__ == "__main__":

    # feel free to use the main method to test your methods!

    pass

