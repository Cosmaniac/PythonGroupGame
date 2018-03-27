#MadebyHwS
import Mover
def scrollFeature():
    scroll = Mover.x >= 40 and Mover.x < (width - 39) and Mover.y >= 100 and Mover.y <= (height - 39)
    if (scroll):
        Mover.x = Mover.x
        Mover.y = Mover.y
    elif (Mover.x < 40):
        Mover.x = width - 40
        Mover.y = Mover.y
    elif (Mover.x > (width - 79)):
        Mover.x = 40
        Mover.y = Mover.y
    elif (Mover.y < 100):
        Mover.x = Mover.x
        Mover.y = height - 40
    elif (Mover.y > (height - 99)):
        Mover.x = Mover.x
        Mover.y = 100
