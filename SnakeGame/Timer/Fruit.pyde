class Fruits:
    def __init__(self, collide, ypos, xpos):
        self.collide = tempCollide
        self.xpos = tempXpos
        self.ypos = tempYpos
        
    def display(self):
        fill(255, 0, 0)
        rect(self.xpos, self.ypos, 20, 20)
        
    def impact(self):
        collide = False
        if(xpos == FrontBlock.xpos && ypos == FrontBlock.ypos + 20 || xpos = FrontBlock.xpos && ypos + 20 == FrontBlock.pos || xpos == FrontBlock.xpos + 20 && ypos == FrontBlock.ypos || xpos + 20 == FrontBlock.xpos && ypos == FrontBlock.ypos):
            collide = True
        