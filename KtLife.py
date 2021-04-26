"""This program is a John Conway's Game of Life running with tkinter
to know more about it --> https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life"""



__author__ = "Jules Garreau"
__contact__ = "jules.garreau00@gmail.com"
__version__ = "1.0.0"
__copyright__ = "copyleft"
__date__ =  "15/02/2021"


import ktlife_functions as fct

import tkinter
import random


#Starting by creating a 50x50 "blueprint" that will be use
#to intialize the grid, barely 20% of the cells will be alive
#at the start with this law.
law = ["1","1","0","0","0","0","0","0","0","0"]
matrix = ""

for j in range(0,50):
    for i in range(0,50):
        matrix += random.choice(law)
    matrix += "."


#create the window, the canvas that will be use to display
#the cells, matrix_cell is the initial grid with the ~20%
#of living cells with a random repartition
Window = tkinter.Tk()
canvas = tkinter.Canvas(Window, width = 1000, height = 1000)
matrix_cell = fct.init_grid(matrix,canvas)

#since a simple Window.mainloop() was not "refresh" the grid,
#I had to use this code with a while loop and the 
#two method .update_idletask() and .update().
turn = True
while turn == True:
    
    fct.cycle_math(matrix_cell)
    fct.cycle_color(matrix_cell,canvas)
    
    canvas.grid()
    Window.update_idletasks()
    Window.update()
    
