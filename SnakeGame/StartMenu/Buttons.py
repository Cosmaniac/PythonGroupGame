class Buttons(object):
    def __init__(self,x,y,w,h,v,n,hov):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.v = v
        self.n = n
        self.hov = False
  
    def display(self):
        if self.hov:
            fill(200,240,0)
            rect(self.x+5,self.y+5,self.w,self.h,self.v)
            fill(0)
            text(self.n,self.x+45,self.y+65)
        else:
            fill(80,80,80)
            rect(self.x+5,self.y+5,self.w,self.h,self.v)
            fill(200,240,0)
            rect(self.x,self.y,self.w,self.h,self.v)
            fill(0)
            text(self.n,self.x+20,self.y+60)
          
            
    def hover(self):
        hov = mouseX>self.x and mouseX<self.x+self.w and mouseY>self.y and mouseY<self.y+self.h
        
  