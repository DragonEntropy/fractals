import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def plot_rectangles(lower_bound, upper_bound, height, depth, max_depth):
    # The width of the rectangle being drawn
    width = (upper_bound - lower_bound) / 3

    # Creates a rectangle with position, width and height and plots it
    rect = patches.Rectangle((lower_bound + width, 0), width, height, edgecolor="black", facecolor="black")
    plt.gca().add_patch(rect)

    # Goes one step deeper
    depth += 1

    # If the staircase still needs to go deeper, it will run again on the bottom third and top third of the previous area
    # The new heights are given by the expression: height +- 2^-(depth + 1)
    if depth < max_depth:
        plot_rectangles(lower_bound, lower_bound + width, height - 1 / math.pow(2, depth + 1), depth, max_depth)
        plot_rectangles(upper_bound - width, upper_bound, height + 1 / math.pow(2, depth + 1), depth, max_depth)

def main():
    # The max iterations of the staircase
    max_depth = 2

    # Begins plotting the staircase
    plot_rectangles(0, 1, 0.5, 0, max_depth)

    # Sets up and plots the graph
    plt.xlim = [0, 1]
    plt.ylim = [0, 1]
    plt.gca().set_aspect("equal", adjustable="box")
    plt.show()

if __name__ == "__main__":
    main()