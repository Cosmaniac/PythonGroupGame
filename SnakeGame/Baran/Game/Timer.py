import Scores, Fruit

T1 = Scores.Timer(1)

score = 0

def setup():
    size(displayWidth, displayHeight)

def draw():
    if(T1.finish):
        global score
        score = score + 0.1
        T1.Start()
    """if(Fruit.collide == true):
        score = score + 100
    print(score)"""
    