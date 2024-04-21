from MRCM import MRCM
import PIL.Image as Image
import PIL.ImageDraw as Draw
import numpy as np

size = 8
m_shift_back = np.array([
    [1, 0, -(size-1)/2],
    [0, 1, -(size-1)/2],
    [0, 0, 1]
])
m_shift_forward = np.array([
    [1, 0, (size-1)/2],
    [0, 1, (size-1)/2],
    [0, 0, 1]
])
m_corner_clockwise = np.array([
    [0, 1, 0],
    [-1, 0, 0],
    [0, 0, 1]
])
m_clockwise = np.matmul(m_shift_forward, np.matmul(m_corner_clockwise, m_shift_back))

scale1 = np.array([
    [-1, 0, size-1],
        [0, 1, 0],
        [0, 0, 1]])
scale2 = np.array(
    [[0.5, 0, size/2],
    [0, 0.5, 0],
    [0, 0, 1]])
scale3 = np.array(
    [[0.5, 0, 0],
    [0, 0.5, size/2],
    [0, 0, 1]])

m_right_shift = np.array([
        [0, 0, size/2],
        [0, 0, 0],
        [0, 0, 0]
    ])

transforms = [np.add(m_clockwise, m_right_shift)]

img = Image.new("RGBA", (size, size), color=(255, 255, 255, 0))
draw = Draw.Draw(img)
draw.polygon([(0, 0), (0, size - 1), (size - 1, 0)], fill=(0, 0, 0, 1))

test = MRCM(transforms, size, size)
test.run_save(img, "testing")