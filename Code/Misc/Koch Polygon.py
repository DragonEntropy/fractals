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

def koch_polygon(depth, max_depth, sides, forward_distance):
    # The angle at which each Koch curve is rotated
    rotation_angle = 180 - 180 * (sides - 2) / sides
    
    # Draws a Koch curve for each side of the polygon
    for side in range(sides):
        draw_spike(depth, max_depth, forward_distance)
        turtle.right(rotation_angle)


def main():
    # Initial parameters
    max_depth = 5
    sides = 3
    size = 500

    # Calculating the line length, initial x_shift and initial y_shift
    length_factor = size * math.sin(math.pi / sides)
    forward_distance = length_factor / math.pow(3, max_depth)
    x_shift = length_factor / 2
    y_shift = size / 2

    # Setting the initial position
    turtle.hideturtle()
    turtle.penup()
    turtle.setpos(-x_shift, y_shift)
    turtle.pendown()
    turtle.speed(0)

    # Drawing the Koch polygon
    koch_polygon(1, max_depth, sides, forward_distance)

    turtle.exitonclick()

if __name__ == "__main__":
    main()