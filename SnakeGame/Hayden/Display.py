# This is the graphics class
class Graphics:
    
    def setup():
        size(2250, 1250)
        
    def draw():
        background(245, 240, 240)
        for i in range(30, 80, 5):
            for j in range(0, 80, 5):
                point(i, j)
        
'''    def grid:
        for(x = 0: x <= width; x += 50):
            
    