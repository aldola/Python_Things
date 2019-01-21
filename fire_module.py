from graphics import *
import  random

PBURN   = 100000
PGROWTH = 100
EMPTY   = "black"
TREE    = "green"
BURNING = "red"

class Cell:
    state = 'E'

    def isBurning(self):
        return self.state == 'B'

    def isEmpty(self):
        return self.state == 'E'
        
    def hasTree(self):
        return self.state == 'T'
    
    def step(self,  hasBurningNeighbour):
        if self.hasTree():
            if hasBurningNeighbour:
                self.state = 'B'
            elif random.randint(1,PBURN) <= 6:
                self.state = 'B'
        elif self.isEmpty():
            if random.randint(1,PGROWTH) == 1:
                self.state = 'T'
        elif self.isBurning():
            self.state = 'E'

    def getState(self):
        return self.state

class Coordinates:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y 

class Forest:
    width  = 0
    height = 0
    area   = []

    def __init__(self, width, height):
        self.width  = width
        self.height = height
        for x in range(self.width):
            column = []
            for y in range(self.height):
                column.append(Cell())
            self.area.append(column)

    def step(self):
        w = random.randint(0,self.width-1)
        h = random.randint(0,self.height-1)
        self.cellAt(w,h).step(self.hasBurningNeighbour(w,h))
        return Coordinates(w,h)

    def cellAt(self,x,y):
        if x != self.width and y != self.height:
            return self.area[x][y]
        else:
            return None

    def hasBurningNeighbour(self,x,y):
        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                if self.cellAt(i,j) is not None and not(i == x and j == y):
                    if self.cellAt(i,j).isBurning():
                        return True
        return False

    def countTrees():
        t = 0
        for i in range(0,self.width):
            for j in range(0,self.height):    
                if self.cellAt(i,j).hasTree():
                    t += 1
        return t     
    
    def countFires():
        f = 0
        for i in range(0,self.width):
            for j in range(0,self.height):    
                if self.cellAt(i,j).isBurning():
                    f += 1
        return f

class ForestSimulator: 
    
    def run(self, width, height, cell_size):
        window = []
        win = GraphWin('Forest', width  * cell_size, height * cell_size, autoflush=True)
        for x in range(width):
            column = []
            for y in range(height):
                b = Rectangle(Point(x*cell_size, y*cell_size),Point(x*cell_size+cell_size, y*cell_size+cell_size))
                b.setFill(EMPTY)
                b.setOutline(EMPTY)
                b.draw(win)
                column.append(b)
            window.append(column)
        forest = Forest(width,height)    
        while True:
            cordinates = forest.step()
            state = forest.cellAt(cordinates.getX(),cordinates.getY()).getState()
            if state == 'E':
                window[cordinates.getX()][cordinates.getY()].setFill(EMPTY)
                window[cordinates.getX()][cordinates.getY()].setOutline(EMPTY)
            elif state == 'T':
                window[cordinates.getX()][cordinates.getY()].setFill(TREE)
                window[cordinates.getX()][cordinates.getY()].setOutline(TREE)
            elif state == 'B':   
                window[cordinates.getX()][cordinates.getY()].setFill(BURNING)     
                window[cordinates.getX()][cordinates.getY()].setOutline(BURNING) 

if __name__ == "__main__":
    a = ForestSimulator()
    a.run(100,100,2)

