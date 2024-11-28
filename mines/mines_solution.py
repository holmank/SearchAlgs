# NO IMPORTS ALLOWED!

def make_board(num_rows, num_cols, default_value):
    """
    Creates and returns a new 2D array of size num_rows x num_cols where each element 
    is default_value
    """
    board = []
    for r in range(num_rows):
        row = []
        for c in range(num_cols):
            row.append(default_value)
        board.append(row)
    return board

def is_in_bounds(row, col, num_rows, num_cols):
    """ 
    Returns True if the board location at (row, col) lies within the bounds
    of (num_rows, num_cols), False otherwise
    """
    return col < num_cols and row < num_rows and col>=0 and row>=0  

def get_neighbors(dims, row, col):
    '''
    Given the dimensions of the board, and a row and column, returns the (up to) 8 surrounding 
    neighbors of location (row, col) that are within the bounds of the board
    '''
    neighbors = []
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if is_in_bounds(i, j, dims[0], dims[1]):
                neighbors.append((i,j))
    return neighbors


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
       bombs (set/tuple): Set of bombs, given in (row, column) pairs (tuples)
    """

    board = make_board(num_rows, num_cols, 0)
    visibility = make_board(num_rows, num_cols, False)

    for r, c in bombs:
        board[r][c] = '.'
        for n in get_neighbors((num_rows, num_cols), r, c):
            if board[n[0]][n[1]]!='.':
                board[n[0]][n[1]] += 1
         
    return {
            "dimensions": (num_rows, num_cols),
            "state": "ongoing",
            "board": board,
            "visible": visibility
            }

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
    if game['visible'][row][col]:
        return 0
    elif game['board'][row][col]!=0:
        game['visible'][row][col] = True
        return 1
    else:
        dug = 1
        game['visible'][row][col] = True
        for n in get_neighbors(game['dimensions'], row, col):
            dug += dig(game, n[0], n[1])
        return dug        
    
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
    victory_state = True
    for r in range(len(game['board'])):
        for c in range(len(game['board'][0])):
            if game['visible'][r][c] and game['board'][r][c]=='.':
                game['state']='defeat'
                return True
            if not game['visible'][r][c] and game['board'][r][c]!='.':
                victory_state = False
    
    if victory_state:
        game['state']='victory'
        return True

    game['state']='ongoing'
    return False

if __name__ == "__main__":

    # feel free to use the main method to test your methods!

    pass

