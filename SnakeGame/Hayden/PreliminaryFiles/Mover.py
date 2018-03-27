xspeed = 0
yspeed = 0
x = (displayWidth / 2)
y = (displayHeight / 2)
c = 0


def move():
    global xspeed, yspeed, x, y, c
    rect(x, y, 20, 20)
    x += xspeed
    y += yspeed
    if keyPressed:
        if key == 'd' and c != 3:
            if y % 20 is 0:
                xspeed = 5
                yspeed = 0
                c = 1
            else:
                if y % 20 < 10:
                    y -= (y % 20)

                elif y % 20 >= 10:
                    y += (20 - (y % 20))

                xspeed = 5
                yspeed = 0
                c = 1

        if key == 's' and c != 4:
            if x % 20 is 0:
                xspeed = 0
                yspeed = 5
                c = 2

        if key == 'a' and c != 1:
            if y % 20 is 0:
                xspeed = -5
                yspeed = 0
                c = 3
            else:
                if y % 20 < 10:
                    y -= (y % 20)

                elif y % 20 >= 10:
                    y += (20 - (y % 20))

                xspeed = -5
                yspeed = 0
                c = 3

        if key == 'w' and c != 2:
            if x % 20 is 0:
                xspeed = 0
                yspeed = -5
                c = 4
