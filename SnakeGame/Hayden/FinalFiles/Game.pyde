import Mover, Scroll

def setup():
    size(int(displayWidth / 20) * 20, (int(displayHeight / 20) * 20) - 40)
    frameRate(100)



def draw():
    background(255, 255, 255)
    stroke(210, 180, 60, 80)
    strokeWeight(1)
    for w in range(40, width - 39, 20):
        line(w, 100, w, height - 40)
    for h in range(100, height - 39, 20):
        line(40, h, width - 40, h)
    fill(210, 180, 60)
    textSize(50)
    textAlign(LEFT, TOP)
    text("Score: ", 25, 0)
    textAlign(RIGHT, TOP)
    text("Time", width, 0)
    textAlign(CENTER, TOP)
    textSize(90)
    text("Snake Game", width / 2, 0)
    strokeWeight(15)
    Mover.move()
    Scroll.scrollFeature()
