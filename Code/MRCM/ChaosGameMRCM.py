import matplotlib.pyplot as plt
import numpy as np
import math
import random

# Creates a transformation matrix from the transformation scaling factors, angles and shifts
def create_matrices(phi, psi, r, s, e, f):

    # Converting angles from degrees to radians
    phi = math.radians(phi)
    psi = math.radians(psi)

    # Finding each matrix constant
    a = r * math.cos(phi)
    b = -s * math.sin(psi)
    c = r * math.sin(phi)
    d = s * math.cos(psi)

    # Returning the transformation matrix and the x, y shift separately
    return np.array([[a, b], [c, d]]), np.array([e, f])

# Applies the transformation matrix and shift to a point
def apply_matrix(point, matrix, shift):
    new_point = np.add(np.matmul(matrix, point), shift)
    return new_point

def main():
    # The number of iterations
    iterations = 250000

    # The minimum for the determinant used
    delta = 0.01

    # The starting point and list of points
    point = np.array([0, 0])
    points = [point]

    # The input transforms in terms of scaling factors, angles and shifts
    
    transforms = [
        [-2.5, -2.5, 0.85, 0.85, 0, 1.6],
        [49, 49, 0.3, 0.34, 0, 1.6],
        [120, -50, 0.3, 0.37, 0, 0.44],
        [0, 0, 0, 0.16, 0, 0]
    ]

    # Colours for each transform
    transform_colours = ["black", "black", "black", "black"]
    colours = ["black"]

    # The matrices, their determinants and their weights based off their determinant magnitude
    matrices = []
    determinants = []
    weights = []

    # Converts each input transform into a transformation matrix and a shift vector
    # Also finds their determinants
    for trans in transforms:
        matrix = create_matrices(*trans)
        matrices.append(matrix)
        det = abs(np.linalg.det(matrix[0]))
        # if det < delta:
        #    det = delta
        determinants.append(det)

    # The sum of determinants to weight each matrix against
    determinant_sum = sum(determinants)

    # Calculates the weights for each matrix based off the determinant
    current_weight = 0
    for det in determinants:
        current_weight += det/determinant_sum
        weights.append(current_weight)

    # The matrices present
    matrix_count = len(matrices)

    # Plots a point for each iteration
    for step in range(0, iterations):

        # Generates a random number from 0 to 1
        outcome = random.random()

        # Checks which function the outcome falls into
        for i in range(matrix_count):
            if outcome < weights[i]:

                # When the outcome falls into a function, it is applied to the point
                point = apply_matrix(point, *matrices[i])

                # The point is then stored and moves to the next point
                points.append(point)
                
                # The colour is also stored
                colours.append(transform_colours[i])
                break
    
    # Splits the x and y coordinates of each point
    x, y = zip(*points)

    # Plots and shows the graph
    plt.scatter(x, y, color=colours, s=0.01)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

if __name__ == "__main__":
    main()