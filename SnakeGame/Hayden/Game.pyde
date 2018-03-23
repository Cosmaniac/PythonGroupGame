xspeed = 0
yspeed = 0
x = (width / 2)
y = (height / 2)

def setup():
    size(int(displayWidth / 20) * 20, (int(displayHeight / 20) * 20) - 40)
    frameRate(500)

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
    move()
    # JumpSpace()


def JumpSpace():
    w1 = int(mouseX / 20) * 20
    h1 = int(mouseY / 20) * 20
    w2 = mouseX % 20
    h2 = mouseY % 20

    if(w2 < 10):
        w2 = 0
    elif(w2 >= 10):
        w2 = 20

    if(h2 < 10):
        h2 = 0
    elif(h2 >= 10):
        h2 = 20
    strokeWeight(25)
    rect(w1 + w2, h1 + h2, 20, 20)

def move():
    global xspeed, yspeed, x, y
    rectMode(CENTER)
    rect(x, y, 20, 20)
        x += xspeed
        y += yspeed
    if keyPressed:
        if key == 'd':
            xspeed = 20
            yspeed = 0
        if key == 's':
            xspeed = 0
            yspeed = 20
        if key == 'a':
            xspeed = -20
            yspeed = 0
        if key == 'w':
            xspeed = 0
            yspeed = -20
