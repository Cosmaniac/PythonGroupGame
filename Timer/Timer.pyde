import Scores
T1 = Scores.Timer(1)

score = 0

def setup():
    size(100, 100)

def draw():
    if(T1.finish):
        global score
        score = score + 100
        T1.Start()
    print(score)
