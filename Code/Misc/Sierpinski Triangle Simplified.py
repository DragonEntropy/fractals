import matplotlib.pyplot as plt
import math
import numpy as np

# The size of the triangle (from rows 0 to size - 1)
# 2^n creates a perfect triangle
size = 16

# The modulo for choosing the pixel value
modulo = 2

# Creates an array of 0s to store the "image" of the triangle
# 0 repesents white
image = np.zeros((size, size))

# Loops through each row of the triangle
for y in range(size):

    #Loops through each column of the triangle
    for x in range(y + 1):

        # The cell's value is given by math.comb(y, x)
        # If the cell's value is assigned a value based on
        # 1 represents black
        image[y - x, x] = math.comb(y, x) % modulo

# The image is generated from the array and displayed
plt.imshow(image, interpolation="nearest", cmap="binary", origin="lower")
plt.show()
