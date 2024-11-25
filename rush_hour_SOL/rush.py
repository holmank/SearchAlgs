import matplotlib.pyplot as plt

from helper import *
from util import *

def makeCars(board):
    '''
    board to cars dictionary.
    '''
    cars = {}
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] in cars:
                cars[board[r][c]].append((r,c))
            elif board[r][c]!=-1:
                cars[board[r][c]] = [(r,c)]
    return cars

def makeBoard(cars):
    '''
    cars dictionary to board.
    '''
    board = [[-1]*6 for i in range(6)]
    for car in cars:
        for coord in cars[car]:
            board[coord[0]][coord[1]]=car
    return board

def getSuccessors(board):
    '''
    How can you get the next states? 
    Make sure you use the helper method copyCars
    to create a copy for each successor.
    '''
    cars = makeCars(board)
    successors = []
    for car in cars:
        locations = cars[car]
        firstRow, firstCol = locations[0]
        lastRow, lastCol = locations[-1]
        # horizontal car
        if firstRow == lastRow: 
            # check move left
            if firstCol !=0 and board[firstRow][firstCol-1]==-1:
                newCars = copyCars(cars)
                newCars[car] = [(firstRow,firstCol-1)] + newCars[car]
                newCars[car].pop()
                successors.append(makeBoard(newCars))
            if lastCol !=5 and board[lastRow][lastCol+1]==-1:
                newCars = copyCars(cars)
                newCars[car] =  newCars[car] + [(lastRow,lastCol+1)]
                newCars[car].pop(0)
                successors.append(makeBoard(newCars))
        else:
            if firstRow != 0 and board[firstRow-1][firstCol]==-1:
                newCars = copyCars(cars)
                newCars[car] = [(firstRow-1,firstCol)] + newCars[car]
                newCars[car].pop()
                successors.append(makeBoard(newCars))
            if lastRow != 5 and board[lastRow+1][lastCol]==-1:
                newCars = copyCars(cars)
                newCars[car] =  newCars[car] + [(lastRow+1,lastCol)]
                newCars[car].pop(0)
                successors.append(makeBoard(newCars))
    return successors


def goalTest(board):
    '''
    The red car (car idNum 0) must take up locations 
    (2,4) and (2,5)
    '''
    return board[2][4]==0 and board[2][5]==0

def BFS(start):
    q = [(start, [start])]
    expanded = set()
    while q:
        board, path = q.pop(0)
        stringBoard = getStringBoard(board)
        if goalTest(board):
            return path, len(expanded)
        if stringBoard not in expanded:
            expanded.add(stringBoard)
            successors = getSuccessors(board)
            for nextBoard in successors:
                stringNext = getStringBoard(nextBoard)
                if stringNext not in expanded:
                    q.append((nextBoard, path + [nextBoard]))

def astarDistToExit(start):
    '''
    A* using distToExitHeuristic.
    '''
    q = PriorityQueue()
    q.push((start, [start], 0), 0) # now need to store cost
    expanded = set()
    while not q.isEmpty():
        board, path, cost = q.pop()
        stringBoard = getStringBoard(board)
        if goalTest(board):
            return path, len(expanded)
        if stringBoard not in expanded:
            expanded.add(stringBoard)
            successors = getSuccessors(board)
            for nextBoard in successors:
                stringNext = getStringBoard(nextBoard)
                if stringNext not in expanded:
                    c = cost + 1
                    h = distToExitHeuristic(nextBoard)
                    q.update((nextBoard, path + [nextBoard], c), c+h)

def distToExitHeuristic(board):
    '''
    How far is the car from the exit location?
    '''
    dist = 0
    col = 5
    while board[2][col]!=0:
        col-=1
        dist+=1
    return dist

def astarCarsBlocking(start):
    '''
    A* using carsBlockingHeuristic.
    '''
    q = PriorityQueue()
    q.push((start, [start], 0), 0) # now need to store cost
    expanded = set()
    while not q.isEmpty():
        board, path, cost = q.pop()
        stringBoard = getStringBoard(board)
        if goalTest(board):
            return path, len(expanded)
        if stringBoard not in expanded:
            expanded.add(stringBoard)
            successors = getSuccessors(board)
            for nextBoard in successors:
                stringNext = getStringBoard(nextBoard)
                if stringNext not in expanded:
                    c = cost + 1
                    h = carsBlockingHeuristic(nextBoard)
                    q.update((nextBoard, path + [nextBoard], c), c+h)

def carsBlockingHeuristic(board):
    """
    Blocking heuristic
    h(B) = 0 if the red car is at the goal when the board is in state S
    h(B) = 1 if the red car is not at the goal but there's nothing in the way when the board is in state S
    h(B) = 2 if the red car is not at the goal and there is at least one car in between it and the goal when the board is in state S
    """
    if goalTest(board):
        return 0
    col = 5
    while col >=0:
        if board[2][col]!=-1 and board[2][col]!=0:
            return 2
        col-=1
    return 3

def astarYourHeuristic(start):
    '''
    A* using myHeuristic.
    '''
    pass

def myHeuristic(board):
    '''
    Choose your own heuristic function.

    You should write an admissible heuristic! How can you improve on the 
    blocking heuristic? How can you improve on the distance to exit heuristic?
    Time to be creative :)
    '''
    pass


if __name__=="__main__":
    cars = loadPuzzle("jams/1.txt")
    board = makeBoard(cars)
    # plot(board)
    print(len(BFS(board)))

    # # uncomment for successors!
    # successors = getSuccessors(board)
    # print(len(successors))
    # plotSuccessors(board, successors)
    plt.show()
