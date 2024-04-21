import matplotlib.pyplot as plt

def half_function(value):
    if value <= 0.5:
        return 2 * value
    else:
        return 2 * (1 - value)

def logistic_function(p):
    r = 3
    return p + r * p * (1 - p)

def logisitic_function_alt(p):
    r = 3
    return (1 + r) * p - r * p * p

def main():  
    functions = [logistic_function, logisitic_function_alt]
    iterations = 100
    starting_values = [0.1, 0.1]
    value_count = len(starting_values)

    for set_n in range(value_count):
        set_function = functions[set_n]
        x_points = list(i for i in range(iterations + 1))
        y_points = []
        current_value = starting_values[set_n]

        for i in range(iterations):
            y_points.append(current_value)
            current_value = set_function(current_value)
        y_points.append(current_value)

        plt.scatter(x_points, y_points)
    plt.show()

if __name__ == "__main__":
    main()