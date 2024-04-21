import matplotlib.pyplot as plt
import numpy as np

# The logistic map equation
def logistic_equation(x, a):
    return a * x * (1 - x)

def main():
    # Initialparameters
    a = 4
    iterations = 1000
    starting_value = 0.1

    # The starting value and point
    current_value = starting_value
    current_point = [current_value, 0]

    # Looping for each iteration
    for i in range(1, iterations + 1):
        # Finding the next value
        current_value = logistic_equation(current_value, a)

        # Plotting the vertical line
        # To plot a line: plt.plot([x1, x2], [y1, y2])
        plt.plot([current_point[0], current_point[0]], [current_point[1], current_value], color="black")

        # Plotting the horizontal line 
        plt.plot([current_point[0], current_value], [current_value, current_value], color="black")

        # Updating the current point to perform the iteration again
        current_point = [current_value, current_value]

    # Creating the parabola
    x_parabola = np.linspace(0, 1, 1000)
    y_parabola = a * x_parabola * (1 - x_parabola)
    plt.plot(x_parabola, y_parabola, color="blue")

    # Creating the line
    plt.plot([0, 1], [0, 1], color="red")

    # Setting up scaling and aspect
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.gca().set_aspect("equal", adjustable="box")

    #Plotting the graph
    plt.show()

if __name__ == "__main__":
    main()