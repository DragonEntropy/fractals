import turtle
import math

def sierpinski(side, level):
    if level == 1:
        turtle.fd(side)
        turtle.left(135)
        turtle.fd(side * math.sqrt(2))
        turtle.left(135)
        turtle.fd(side)
        turtle.left(90)
    else:
        sierpinski(side/2, level-1)
        turtle.fd(side/2)
        sierpinski(side/2, level-1)
        turtle.bk(side/2)
        turtle.left(90)
        turtle.fd(side/2)
        turtle.right(90)
        sierpinski(side/2, level-1)
        turtle.left(90)
        turtle.bk(side/2)
        turtle.right(90)
def main():
    sierpinski(400, 8)

turtle.setworldcoordinates(-1, -1, 400, 350)
turtle.speed(0)
main()
turtle.hideturtle()
turtle.mainloop()