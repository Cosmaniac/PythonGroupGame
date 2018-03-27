import Fruit


    
class Follow:
    def __init__(self, x, y):
        self.x
        self.y

    X = [x]
    Y = [y]        
    
    def update(tempX, tempY, snakeLength): 
        X.insert(0, tempX)
        if(snakeLength <= len(X)):
            X.remove(len(X)-1)
            Y.remove(len(Y)-1)
    
    