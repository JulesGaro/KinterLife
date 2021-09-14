class Cell:
    """Define a cell of the grid that can be dead or alive (black or green) 
    
    the method are use to change the color of the cells
    and will be called depending of the paremeters state or change_state
    during the cycles of the game

    
    """

    def __init__(self,x,y,state, canvas):
        """a cell is init with it coords and state (0 for "dead,1 for "alive")

        A tkinter rectangle with the coords of the cell and the color depending 
        of it state is also create in the canvas
        """
        self.x = x
        self.y = y
        self.state = state
        self.change_state = 0
        self.cell = canvas.create_rectangle((self.x, self.y),(self.x + 20, self.y + 20) , fill ="white")
    
    
    def dead_cell(self, canvas):
        """method use to set the color to black for a dead cell"""

        canvas.itemconfig(self.cell, fill ="black")

        

    def living_cell(self, canvas):
        """method use to set the color to green for a living cell"""
        
        canvas.itemconfig(self.cell, fill ="green")



def init_grid(matrice,canvas):
    """initialize the grid using the binary blueprint randomly generated"""

    cell_matrix = []

    #"line" of the matrix were seperated by dot when created
    matrice = matrice.split(".")
    
    for i in range(0,len(matrice)):
        for j in range(0,len(matrice[i])):
            if matrice[i][j] == "0": #initialize a dead cell
                
                cell_matrix.append(Cell(j*20,i*20,0,canvas))
            
            elif matrice[i][j] == "1": #initialize a living cell

                cell_matrix.append(Cell(j*20,i*20,1,canvas))

    return cell_matrix

def cycle_math(cell_matrix):
    """function that make a turn and change the cells states

    the function will check for all the cell how
    many cells or alive around it (notice that the 
    edge of the grid are consider as dead cell) and
    change their state (or not).

    to be brief on the Game of Life rules :
    --> A dead cell become alive if it surrounded by
        exactly 3 living cell become alive
    --> when surrounded by less than 2 or more than
        3 living cell a cell die (from 2 to 3 it stay
        alive).

    """
    for i in range(0, len(cell_matrix)):

        score = 0
        
        if cell_matrix[i].y != 0 and cell_matrix[i].x != 0 and cell_matrix[i-51].state == 1:
            score += 1

        if cell_matrix[i].y != 0 and cell_matrix[i-50].state == 1:
            score += 1

        if cell_matrix[i].y != 0 and cell_matrix[i].x != 980 and cell_matrix[i-49].state == 1:
            score += 1

        if  cell_matrix[i].x != 0 and cell_matrix[i-1].state == 1:
            score += 1

        if cell_matrix[i].x != 980 and cell_matrix[i+1].state == 1:
            score += 1

        if cell_matrix[i].y != 980 and cell_matrix[i].x != 980 and cell_matrix[i+51].state == 1:
            score += 1

        if cell_matrix[i].y != 980 and cell_matrix[i+50].state == 1:
            score += 1

        if cell_matrix[i].y != 980 and cell_matrix[i].x != 0 and cell_matrix[i+49].state == 1:
            score += 1


        
        if cell_matrix[i].state == 1:

            if score < 2 or score > 3:

                cell_matrix[i].change_state = 0
            
            else:

                cell_matrix[i].change_state = 1

        if cell_matrix[i].state == 0:

            if score == 3:

                cell_matrix[i].change_state = 1

            else:

                cell_matrix[i].change_state = 0

        

def cycle_color(cell_matrix, canvas):
    """change the color of the cell 

    if it is needed the function will change
    the color of the cells : green for 
    alive and black for dead.


    """
    for i in range(0,len(cell_matrix)):

        if cell_matrix[i].change_state == 0:

            cell_matrix[i].state = 0
            cell_matrix[i].dead_cell(canvas)

        if cell_matrix[i].change_state == 1:

            cell_matrix[i].state = 1
            cell_matrix[i].living_cell(canvas)





