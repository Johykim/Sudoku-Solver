import random


'''This is a basic application to solve a Sudoku board using backtracking'''

#current board being used
'''
b = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
'''
#main function that works recursively and validates using other functions
def solve(board):

    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(board, i, (row,col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False
#main validation function that essentially checks a possible value for a square against values within the same: column, row or 3x3 square

def valid(board,num, pos):
    #check row, col and which square you're in
    for i in range(9):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(9):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    #this is my method to ensure that each 3x3 square has a different numbering
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y *3 +3):
        for j in range(box_x * 3, box_x*3 +3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True





#printing a Sudoku board so it's easier to view
def print_board(board):
    TableTB = "|--------------------------------|"
    TableMD = "|----------+----------+----------|"
    print(TableTB)
    for x in range(9):
        for y in range(9):
            if ((x == 3 or x == 6) and y == 0):
                print(TableMD)
            if (y == 0 or y == 3 or y == 6):
                print("|", end=" ")
            print(" " + str(board[x][y]), end=" ")
            if (y == 8):
                print("|")
    print(TableTB)

#Tries to find a 0 within the Sudoku board so that we can try a new value into that square
def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i,j) # row,col
    return None





#With the current print function embedded into solve you can see the steps that are being taken to solve




def MakeSudoku():
    Grid = [[0 for x in range(9)] for y in range(9)]

    for i in range(9):
        for j in range(9):
            Grid[i][j] = 0

    #randomly give the board a certain number of values to work with
    given = random.randrange(8,13)
    for i in range(given):
        # choose random spots to put the values
        row = random.randrange(9)
        col = random.randrange(9)
        num = random.randrange(1, 10)
        while (not valid(Grid, num, (row,col)) or Grid[row][col] != 0):  # validate that the code doesn't put down an imporoper value
            row = random.randrange(9)
            col = random.randrange(9)
            num = random.randrange(1, 10)
        Grid[row][col] = num

    return(Grid)






b=MakeSudoku()
print_board(b)
solve(b)
print_board(b)
