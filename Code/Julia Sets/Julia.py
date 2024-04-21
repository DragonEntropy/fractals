import numpy as np
import matplotlib.pyplot as plt

def function(z):

    # This can be changed to whatever works with numpy arrays
    return z**12 - 0.25 * z**3 - 1

def julia(n, m, x_min=-2.5, x_max=2.5, y_min=-2.5, y_max=2.5):

    # Step 1: Generate an n by n matrix of complex numbers in the bounds x_min, x_max, y_min, y_max
    x, y = np.meshgrid(np.linspace(x_min, x_max, n), np.linspace(y_min, y_max, n) * 1j)
    z = x + y

    # Step 2: Generate an n by n matrix determining how many stages each point lasts before reaching "infinity"
    total_stages = np.zeros([n, n])

    # Step 3: Apply the Julia set function m times
    for k in range(m):
        # Updates the complex numbers' values at the kth iteration
        z = function(z)

        # A matrix of booleans corresponding to which initial complex numbers have not reached "infinity" after the kth iteration
        is_non_escapee = np.abs(z) < np.inf

        # If the complex number has not yet reached infinity, it survives another stage
        total_stages += is_non_escapee

    # Step 4: Return the real intervals, imaginary intervals and total stages survived
    return np.linspace(x_min, x_max, n), np.linspace(y_min, y_max, n), total_stages
    

def main():

    # Generates the real intervals, imaginary intervals and total stages survived
    x, y, total_stages = julia(1000, 100)

    # Plots the real and imaginary intervals, with the darkness of the pixel representing the stages survived
    plt.figure(figsize = (10, 10))
    plt.pcolormesh(x, y, total_stages, cmap = "binary")
    plt.axis('equal')
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    main()