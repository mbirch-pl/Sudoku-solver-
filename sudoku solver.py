import numpy as np

grid = []
grid.append([1, 0, 2, 0, 0, 4, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 9, 0, 2, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 6, 0, 0])
grid.append([0, 0, 8, 0, 0, 5, 0, 0, 0])
grid.append([0, 7, 0, 0, 6, 0, 0, 0, 0])
grid.append([0, 0, 0, 1, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 3, 0, 0, 0, 0, 9, 0])

def print_board(grid):
    for i in range(len(grid)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(grid[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(grid[i][j])
            else:
                print(str(grid[i][j]) + " ", end="")

def find_empty(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                return (i, j)
    return (None)

def valid(gird,position,number):

    #Check row
    if number in grid[position[0]]:
        return False

    #Check column
    for x in range(len(grid)):
        if number == grid[x][position[1]]:
            return False

    #Check box
    square_x = position[0]//3
    square_y = position[1]//3

    for i in range(square_x*3, square_x*3 + 3):
        for j in range(square_y * 3, square_y * 3 + 3):
            if grid[i][j] == number and (i, j) != position:
                return False
    return True

def solver(grid):
    find = find_empty(grid)
    if find == None:
        return True
    else:
        row, column = find

    for i in range(1,10):
        if valid(grid,(row,column), i):
            grid[row][column] = i

            if solver(grid):
                return True

            grid[row][column] = 0
    return False

solver(grid)
print_board(grid)










