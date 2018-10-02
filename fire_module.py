from graphics import *
import  random

PBURN   = 1000
PGROWTH = 10

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

        for i in range(x-1,x+1):
            for j in range(y-1,y+1):
                if self.cellAt(i,j) is not None and (i != x and j != y):
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
    WIDTH  = 50
    HEIGHT = 50
    CELL_SIZE = 5
    APLLICATION_WIDTH  = WIDTH  * CELL_SIZE 
    APLLICATION_HEIGHT = HEIGHT * CELL_SIZE
    EMPTY   = "black"
    TREE    = "green"
    BURNING = "red"
    def run(self):
        window = []
        win = GraphWin('Forest', self.APLLICATION_WIDTH, self.APLLICATION_HEIGHT, autoflush=True)
        for x in range(self.WIDTH):
            column = []
            for y in range(self.HEIGHT):
                b = Rectangle(Point(x*self.CELL_SIZE, y*self.CELL_SIZE),Point(x*self.CELL_SIZE+self.CELL_SIZE, y*self.CELL_SIZE+self.CELL_SIZE))
                b.setFill(self.EMPTY)
                b.setOutline(self.EMPTY)
                b.draw(win)
                column.append(b)
            window.append(column)
        forest = Forest(self.WIDTH,self.HEIGHT)    
        while True:
            cordinates = forest.step()
            state = forest.cellAt(cordinates.getX(),cordinates.getY()).getState()
            if state == 'E':
                window[cordinates.getX()][cordinates.getY()].setFill(self.EMPTY)
                window[cordinates.getX()][cordinates.getY()].setOutline(self.EMPTY)
            elif state == 'T':
                window[cordinates.getX()][cordinates.getY()].setFill(self.TREE)
                window[cordinates.getX()][cordinates.getY()].setOutline(self.TREE)
            elif state == 'B':   
                window[cordinates.getX()][cordinates.getY()].setFill(self.BURNING)     
                window[cordinates.getX()][cordinates.getY()].setOutline(self.BURNING)
        win.close()

if __name__ == "__main__":
    a = ForestSimulator()
    a.run()
    '''win = GraphWin('Forest', 100, 100)
    b = Rectangle(Point(4, 4), Point(4, 4))
    c = Rectangle(Point(1,3), Point(4,7))
    b.setFill("red")
    b.draw(win)  
    win.getMouse() 
    c.setFill("brown")
    c.draw(win)   
    win.getMouse() 
    win.close()'''
