# This is the graphics tab
width = int(displayWidth/50) * 50
height = int(displayHeight/50) * 50    
def setup():
    size(this, that)
    
    
    


def draw():
    background(245, 240, 240)
    stroke(210, 180, 60, 80)
    strokeWeight(1)
    for w in range(0, width, 50):
            line(w, 100, w, height - 100)
    for h in range(100, height - 50, 50):
            line(0, h, width, h)
    fill(210, 180, 60)
    textSize(50)
    textAlign(LEFT, TOP)
    text("Score: ", 25, 0)
    textAlign(RIGHT, TOP)
    text("Time", width, 0)
    textAlign(CENTER, TOP)
    textSize(90)
    text("Snake Game", width/2,  0)
    strokeWeight(15)
    JumpSpace()
    
            
def JumpSpace():
        w1 = int(mouseX / 50) * 50
        h1 = int(mouseY / 50) * 50
        w2 = mouseX % 50
        h2 = mouseY % 50
        
        if(w2 < 25):
            w2 = 0
        elif(w2 >= 25):
            w2 = 50
        
        if(h2 < 25):
            h2 = 0
        elif(h2 >= 25):
            h2 = 50
        strokeWeight(25)
        point(w1 + w2, h1+h2)
        point(w1 + w2, h1+h2 - 50)
        point(w1 + w2 - 50, h1+h2 - 50)
        point(w1 + w2 - 50, h1+h2)
