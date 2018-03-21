import FrontBlock

class Fruits:
    global collide
    global xpos
    global ypos

    def __init__(self, collide, ypos, xpos):
        self.collide = tempCollide
        self.xpos = tempXpos
        self.ypos = tempYpos

    def display(self):
        fill(255, 0, 0)
        rect(xpos, ypos, 20, 20)

    def impact(self):
        collide = False
        if(xpos == FrontBlock.xpos and ypos == FrontBlock.ypos + 20 or xpos=FrontBlock.xpos and ypos + 20 == FrontBlock.pos or xpos == FrontBlock.xpos + 20 and ypos == FrontBlock.ypos or xpos + 20 == FrontBlock.xpos and ypos == FrontBlock.ypos):
            collide = True

    def spawn(self):
        if(collide == True):
            xpos = random(20, displayWidth - 20)
            ypos = random(20, displayHeight - 20)
            collide = False
