from graphics import *
import  random

class Cell:

    state = 'E'
    PBURN   = 0.00006
    #6/100000
    PGROWTH = 0.01
    #1/100

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
            elif random.randint(1,1000) <= 6:
                self.state = 'B'
        elif self.isEmpty():
            if random.randint(1,10) == 1:
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
        for x in range(height):
            column = []
            for y in range(width):
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
    WIDTH  = 20
    HEIGHT = 20
    CELL_SIZE = 4
    APLLICATION_WIDTH  = WIDTH  * CELL_SIZE
    APLLICATION_HEIGHT = HEIGHT * CELL_SIZE
    EMPTY   = "black"
    TREE    = "green"
    BURNING = "red"

    def run(self):
        window = []
        win = GraphWin('Forest', self.APLLICATION_WIDTH, self.APLLICATION_HEIGHT)
        for x in range(self.WIDTH):
            column = []
            for y in range(self.HEIGHT):
                b = Rectangle(Point(x*self.CELL_SIZE, y*self.CELL_SIZE),Point(4, 4))
                b.setFill(self.EMPTY)
                b.draw(win)
                column.append(b)
            window.append(column)
        while True:
            forest = Forest(self.WIDTH,self.HEIGHT)
            cordinates = forest.step()
            state = forest.cellAt(cordinates.getX(),cordinates.getY()).getState()
            print (state)
            print (window[cordinates.getX()][cordinates.getY()])
            if state == 'E':
                window[cordinates.getX()][cordinates.getY()].setFill(self.EMPTY)
            elif state == 'T':
                window[cordinates.getX()][cordinates.getY()].setFill(self.TREE)
            elif state == 'B':        
                window[cordinates.getX()][cordinates.getY()].setFill(self.BURNING)
            time.sleep(.01)
            #win.getMouse()

if __name__ == "__main__":
    a = ForestSimulator()
    a.run()
    """     win = GraphWin('Forest', 100, 100)
    b = Rectangle(Point(4, 4), Point(4, 4))
    c = Rectangle(Point(20, 20), Point(30, 30))
    b.setFill("red")
    b.draw(win)  
    c.setFill("brown")
    c.draw(win)   
    win.getMouse() 
    win.close() """
