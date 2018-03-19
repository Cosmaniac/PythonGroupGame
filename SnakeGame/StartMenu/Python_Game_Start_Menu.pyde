import Buttons
b1 = Buttons.Buttons(210,160,170,100,5,'  START',True)
b2 = Buttons.Buttons(210,365,170,100,5,'OPTIONS',True)

def setup():
  size(600,600)
  background(0,100,0)
  
def draw():
  background(0,100,0)
  fill(0,200,0)
  rect(35,70,527,490,10)
  fill(200,240,0)
  textSize(30)
  text("[Python Snake Game]", 140,43)
  fill(0)
  b1.hover()
  b1.display()
  b2.hover()
  b2.display()
  

  