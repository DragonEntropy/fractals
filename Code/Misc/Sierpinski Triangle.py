import matplotlib.pyplot as plt
import math
import numpy as np

# This is a generator function. It is more efficient, but a more advanced topic.
# The function yields every value of x, y, z one at a time
# The function yields:
#   x : The column
#   y : The row
#   z : The value at the cell
def pascal_gen(size):

    # Loops through each row of the triangle
    for y in range(0, size):

        #Loops through each column of the triangle
        for x in range(0, y + 1):

            # The cell's value is given by math.comb(y, x)
            yield x, y, math.comb(y, x)

def main():
    # The size of the triangle (from rows 0 to size - 1)
    # 2^n creates a perfect triangle
    size = 512

    # Creates an array of 0s to store the "image" of the triangle
    # 0 repesents white
    image = np.zeros((size, size))

    # Loops through each cell in the triangle
    for x, y, z in pascal_gen(size):

        # If the cell's value is odd, it is given the value 1
        # 1 represents black
        if z % 2 == 1:
            # Setting the row to y - x flips the triangle the right way
            image[y - x, x] = 1
    
    # The image is generated from the array and displayed
    plt.imshow(image, interpolation="nearest", cmap="binary", origin="lower")
    plt.show()

if __name__ == "__main__":
    main()