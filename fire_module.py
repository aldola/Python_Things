import  random

class Cell:

    state = 'E'
    PBURN   = 0.00006
    PGROWTH = 0.01

    def isBurning(self):
        return self.state == 'B'

    def isEmpty(self):
        return self.state == 'E'
        
    def hasTree(self):
        return self.state == 'T'
    
    def step(self,  hasBurningNeighbour):
        if self.hasTree() and hasBurningNeighbour:
            self.state = 'B'
        elif self.isBurning():
            self.state = 'E'
        else:
            self.state = 'T'

class Coordinates:

    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX():
        return self.x

     def getY():
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
        w = random.randint(0,width-1)
        h = random.randint(0,height-1)
        self.cellAt(w,h).step(self.hasBurningNeighbour(w,h))
        return Coordinates(w,h)

    def cellAt(self,x,y):
        if x != self.width and y != self.height:
            return self.area[x][y].Cell()
        else:
            return None

    def hasBurningNeighbour(x,y):
        #Left
        if w != 0:
            if self.area[w-1][h].isBurning():
                burningNeighbour = True
        #Right
        if w != width-1 and not burningNeighbour:
            if self.area[w+1][h].isBurning():
                burningNeighbour = True 
        #Up
        if h != 0 and not burningNeighbour:
            if self.area[w][h-1].isBurning():
                burningNeighbour = True
        #Down
        if h != height-1 and not burningNeighbour:
            if self.area[w][h+1].isBurning():
                burningNeighbour = True
        self.area[w][h].step(burningNeighbour)

if __name__ == "__main__":

    c = random.randint(0,5-1)
    print (c)

