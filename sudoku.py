# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 21:38:12 2022

@author: VAGUE
"""

# printing the board for displaying the numbers
def print_board(puzzle):
    for r in range(len(puzzle)):
        if r%3 == 0 and r != 0:
            print("- - - - - - - - - - - -")
        
        for c in range(len(puzzle[0])):
            if c%3 == 0 and c != 0:
                print(" | ", end="")
                
            if c == 8:
                print(puzzle[r][c])
            else:
                print(str(puzzle[r][c]) + " ", end="")
                
def find_empty(puzzle):
    for r in range(len(puzzle)):
        for c in range(len(puzzle[0])):
            if puzzle[r][c] == 0:
                return r, c
    
    return None, None