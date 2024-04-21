import matplotlib.pyplot as plt
import numpy as np
import math
import random
import os

from matplotlib.animation import FuncAnimation, PillowWriter

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

def animate(frame):
    # The increment between frames
    increment = 100
    plt.clf()

    global point, points, matrix_count, weights, matrices

    for i in range(frame * increment):
        outcome = random.random()

        for i in range(matrix_count):
            if outcome < weights[i]:

                # When the outcome falls into a function, it is applied to the point
                point = apply_matrix(point, *matrices[i])

                # The point is then stored and moves to the next point
                points.append(point)
                
                break
    
    # Splits the x and y coordinates of each point
    x, y = zip(*points)

    # Plots and shows the graph
    plt.xlim([0, 1])
    plt.ylim([0, math.sqrt(3)/2])
    plt.gca().set_aspect('equal', adjustable='box')
    plt.axis('off')
    plt.scatter(x, y, color="black", s=0.01)

def main():
    folder_name = "animations"
    path = os.path.dirname(__file__)
    if not os.path.exists(path + "/" + folder_name):
        os.mkdir(path + "/" + folder_name)
    file_name = "triangle"
    
    # The minimum for the determinant used
    delta = 0.01

    # The starting point and list of points
    global point, points, matrix_count, weights, matrices
    point = np.array([0, 0])
    points = [point]

    # The input transforms in terms of scaling factors, angles and shifts
    """
    For the barnsley fern
    transforms = [
        [-2.5, -2.5, 0.85, 0.85, 0, 1.6],
        [49, 49, 0.3, 0.34, 0, 1.6],
        [120, -50, 0.3, 0.37, 0, 0.44],
        [0, 0, 0, 0.16, 0, 0]
    ]
    """
    
    # The matrices, their determinants and their weights based off their determinant magnitude
    matrices = [
        (np.array([[0.5, 0], [0, 0.5]]), np.array([0, 0])),
        (np.array([[0.5, 0], [0, 0.5]]), np.array([0.5, 0])),
        (np.array([[0.5, 0], [0, 0.5]]), np.array([0.5, 0.5])),
        (np.array([[0.5, 0], [0, 0.5]]), np.array([1, 0])),
        (np.array([[0.5, 0], [0, 0.5]]), np.array([1, 0.5])),
        (np.array([[0.5, 0], [0, 0.5]]), np.array([1, 1])),
    ]
    determinants = []
    weights = [1/3, 2/3, 1]

    """
    # Converts each input transform into a transformation matrix and a shift vector
    # Also finds their determinants
    for trans in transforms:
        matrix = create_matrices(*trans)
        matrices.append(matrix)
        det = abs(np.linalg.det(matrix[0]))
        if det < delta:
            det = delta
        determinants.append(det)

    # The sum of determinants to weight each matrix against
    determinant_sum = sum(determinants)

    # Calculates the weights for each matrix based off the determinant
    current_weight = 0
    for det in determinants:
        current_weight += det/determinant_sum
        weights.append(current_weight)
    """

    # The matrices present
    matrix_count = len(matrices)

    plt.figure(figsize=(10, 10))
    animation = FuncAnimation(plt.gcf(), animate, frames=100, interval=200, repeat=True)
    writergif = PillowWriter(fps=10)
    animation.save("{0}\\{1}\\{2}.gif".format(path, folder_name, file_name), writer=writergif)
    plt.close()

if __name__ == "__main__":
    main()