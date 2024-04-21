import turtle
import math

def draw_spike(depth, max_depth, forward_distance):
    # If the max depth has not been reached, smaller Koch curves are drawn in the place of lines
    if depth < max_depth:
        draw_spike(depth + 1, max_depth, forward_distance)
        turtle.left(60)
        draw_spike(depth + 1, max_depth, forward_distance)
        turtle.right(120)
        draw_spike(depth + 1, max_depth, forward_distance)
        turtle.left(60)
        draw_spike(depth + 1, max_depth, forward_distance)

    # If the max depth has been reached, lines are drawn
    else:
        turtle.forward(forward_distance)
        turtle.left(60)
        turtle.forward(forward_distance)
        turtle.right(120)
        turtle.forward(forward_distance)
        turtle.left(60)
        turtle.forward(forward_distance)

def main():
    # The depth for the curve generation
    max_depth = 5

    # The size of the curve
    size = 400

    # Setting the initial position
    forward_distance = size / math.pow(3, max_depth)
    turtle.penup()
    turtle.setpos(-size / 2, 0)
    turtle.pendown()
    turtle.hideturtle()
    turtle.speed(0)

    # Starting the iterative process
    draw_spike(1, max_depth, forward_distance)

    turtle.exitonclick()

if __name__ == "__main__":
    main()
