"""Functions to solve a sudoku"""

import itertools
from pydoku.row import *

def check_valid(row, column, num):
    """Auxiliary function to check if the digit to be assigned is not repeated in the column and in the 3x3 submatrix"""
    global mat_s
    for i in range(0, 9):
        if mat_s[i][column] == num:
            return False
    square_row = (row // 3) * 3
    square_col = (column // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if mat_s[square_row + i][square_col + j] == num:
                return False
    return True

def solve_sudoku():
    global mat_s
    for row in range(9):
        row_permut = list(itertools.permutations(options_row(row)))
        for permut in row_permut:
            for column in range(9):
                if mat_s[row,column] == 0:
                    for num in permut:
                        if check_valid(row, column, num):
                            mat_s[row][column] = num
                            solve_sudoku()
                            mat_s[row][column] = 0
                    return
    print("Solution for the Sudoku Problem: ")
    print_matrix()
