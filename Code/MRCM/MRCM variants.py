from MRCM import MRCM, Transform
import PIL.Image as Image
import PIL.ImageDraw as Draw 
import numpy as np
import math

# Creates a transformation matrix from the transformation scaling factors, angles and shifts
def create_matrix(phi, psi, r, s, e, f):

    # Converting angles from degrees to radians
    phi = math.radians(phi)
    psi = math.radians(psi)

    # Finding each matrix constant
    a = r * math.cos(phi)
    b = -s * math.sin(psi)
    c = r * math.sin(phi)
    d = s * math.cos(psi)

    # Returning the transformation matrix and the x, y shift separately
    return np.array([[a, b, e], [c, d, f], [0, 0, 1]])

def main():
    # Sets x and y sizes
    x_size = 1024
    y_size = 1024

    # Sets the base image
    base = Image.new("RGBA", (y_size, x_size), color=(255, 255, 255, 0))
    draw = Draw.Draw(base)
    #draw.polygon([(0, 0), (0, y_size - 1), (x_size/2 - 1, y_size - 1)], fill=(0, 0, 0, 1))
    draw.polygon([(0, 0), (0, y_size - 1), (x_size - 1, y_size - 1), (x_size - 1, 0)], fill=(0, 0, 0, 1))

    # Creating transform objects
    t1 = Transform(0, x_size, y_size, 0.5, 0.5, x_size/4, 0)
    t2 = Transform(3, x_size, y_size, 0.5, 0.5, x_size/2, y_size/4)
    t3 = Transform(1, x_size, y_size, 0.5, 0.5, 0, y_size/2)
    transforms = [t1, t2, t3]

    # Creating and running the MRCM
    mrcm = MRCM(transforms, x_size, y_size)
    mrcm.run_save(base, "test")

if __name__ == "__main__":
    main()