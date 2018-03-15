timesPressedD = 0
timesPressedS = 0
timesPressedA = 0
timesPressedW = 0


def setup():
    size(2000, 2000)


def draw():
    global timesPressedD
    global timesPressedA
    global timesPressedS
    global timesPressedW
    x = (timesPressedD * 50) + (timesPressedA * -50)
    y = (timesPressedS * 50) + (timesPressedW * -50)
    if keyPressed:
        if key == 'd' or key == 'D':
            rect(x + 50, y, 50, 50)
            timesPressedD += 1
    if keyPressed:
        if key == 's' or key == 'S':
            rect(x, y + 50, 50, 50)
            timesPressedS += 1
    if keyPressed:
        if key == 'a' or key == 'A':
            rect(x - 50, y, 50, 50)
            timesPressedD += 1
    if keyPressed:
        if key == 'w' or key == 'W':
            rect(x, y - 50, 50, 50)
            timesPressedD += 1
