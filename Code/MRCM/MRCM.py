import PIL.Image as Image
import numpy as np
import os

"""
The MRCM class manages performing transformations on an initial image

Constructor Argumentss:
    transforms - A list of transform objects or 3x3 numpy arrays
    x_size - The width of the image
    y_size - The height of the image
    <default_depth> - The depth at which the MRCM should iterate to on default (default value is 10)

User Methods:
    MRCM(transforms, x_size, y_size, <default_depth>)
        Creates an instance of the MRCM class
    MRCM.run(start_img, <depth>, <show>)
        Runs the MRCM on a starting image
        start_img - The starting image that must be of the same size as the MRCM
        <depth> - The depth at which the MRCM should iterate to (default value is default_depth)
        <show> - A boolean determining if stages should be displayed while running (default value is True)
    MRCM.run_save(start_img, folder_name, depth, <show>)
        Runs the MRCM and saves its stages to a directory
        start_img - The starting image that must be of the same size as the MRCM
        folder_name - The directory where the images are saved
        <depth> - The depth at which the MRCM should iterate to (defaults value is default_depth)
        <show> - A boolean determining if stages should be displayed while running (default value is False)

Other Methods:
    MRCM.apply_transformations(img, scaled_transformations)
        Performs all transformations on an image and returns a list of transformed images
        img - The image having transformations applied
    MRCM.apply_merge(imgs)
        Returns the merged image of transformed images
        imgs - The images to merge
"""
class MRCM:
    # Stores transforms and inverse transforms arrays or Transform objects
    transforms = []
    inv_transforms = []

    def __init__(self, transforms, x_size, y_size, default_depth=10):
        # Setting class attributes
        self.transforms = transforms
        self.x_size = x_size
        self.y_size = y_size
        self.default_depth = default_depth

        # Finds the inverse transformations for each matrix or Transform object
        if isinstance(transforms[0], Transform):
            for trans in transforms:
                self.inv_transforms.append(np.linalg.inv(trans.get_matrix()))
        else:
            for trans in transforms:
                self.inv_transforms.append(np.linalg.inv(trans))
        
    def run(self, start_img, depth=-1, show=True):
        # If no depth is given, defaults to the default depth
        if depth == -1:
            depth = self.default_depth
        
        # A list of stages of the image's creation
        img = start_img
        stages = [start_img]
        for i in range(depth):
            # Applies each transformation on the image, then merges them
            img_transforms = self.apply_transforms(img)
            img = self.apply_merge(img_transforms)
            stages.append(img)

            # Shows the image if show is set to True
            if show:
                img.convert("RGB").show()

        return stages

    def run_save(self, start_img, folder_name, depth=-1, show=False):
        # Finds the current file directory (not needed in most IDEs but included as a precaution)
        path = os.path.dirname(__file__)
        if not os.path.exists(path + "/" + folder_name):
            os.mkdir(path + "/" + folder_name)

        # Saves each stage of the image in the specified directory
        stages = self.run(start_img, depth, show)
        for i in range(len(stages)):
            stages[i].convert("RGB").save("{0}\\{1}\stage_{2}.png".format(path, folder_name, i))

    def apply_transforms(self, img):
        # Applies each transformation as an affine transformation on the current image and places them into a list
        # Note that inverse transformations are required by the AFFINE transformation implementation
        outputs = []
        for trans in self.inv_transforms:
            outputs.append(img.transform((self.y_size, self.x_size), Image.AFFINE, data=trans.flatten()[:6], resample=Image.NEAREST, fillcolor=(255, 255, 255, 0)))
        return outputs

    @staticmethod
    def apply_merge(imgs):
        # Merges images by averaging each pixel's colour values weighted by their alpha values
        base = imgs[0]
        for i in range(1, len(imgs)):
            layer = imgs[i]
            base = Image.alpha_composite(base, layer)
        return base

"""
The Transform class manages the creation of transformation matrices

Constructor Arguments:
    base - The base transformation matrix
        Can be passed as a numpy ndarray
        Can be passed as an integer identifying a default matrix
    x_size - The width of the transformation image
    y_size - The height of the transformation image
    x_scale - The x-scaling of the transformation
    y_scale - The y-scaling of the transformation
    x_shift - The x-translation of the transformation
    y_shift - The y-translation of the transformation

User Methods:
    get_matrix()
        Returns the matrix for the transformation

Other Methods:
    default_matrix(id)
        Retuns a default matrix with a specific id
        id - The integer id for the matrix
"""
class Transform:
    def __init__(self, base, x_size, y_size, x_scale, y_scale, x_shift, y_shift):
        # Defining the scaling and translation matrices
        m_scale = np.array([
            [x_scale, 0, 0],
            [0, y_scale, 0],
            [0, 0, 1]
        ])
        m_translate = np.array([
            [0, 0, x_shift],
            [0, 0, y_shift],
            [0, 0, 0]
        ])

        # Setting class attributes
        self.x_size = x_size
        self.y_size = y_size
        self.base = base

        # If a index is supplied instead of a matrix, a default matrix will be used as the base
        if isinstance(base, np.ndarray):
            self.base = base
        else:
            self.base = self.default_matrix(base)

        # Applies the scaling and translation matricies on the base matrix to obtain the final transformation matrix
        self.matrix = np.add(np.matmul(m_scale, self.base), m_translate)

    def get_matrix(self):
        return self.matrix

    def default_matrix(self, id):
        # Defining important basic matrices for the default matrices
        m_identity = np.array([
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ])
        m_shift_back = np.array([
            [1, 0, -self.x_size/2],
            [0, 1, -self.y_size/2],
            [0, 0, 1]
        ])
        m_shift_forward = np.array([
            [1, 0, self.x_size/2],
            [0, 1, self.y_size/2],
            [0, 0, 1]
        ])
        m_corner_clockwise = np.array([
            [0, -1, 0],
            [1, 0, 0],
            [0, 0, 1]
        ])
        m_clockwise = np.matmul(m_shift_forward, np.matmul(m_corner_clockwise, m_shift_back))
        m_halfrotate = np.matmul(m_clockwise, m_clockwise)
        m_anticlockwise = np.matmul(m_clockwise, m_halfrotate)

        m_flip_x = np.array([
            [-1, 0, self.x_size],
            [0, 1, 0],
            [0, 0, 1]
        ])
        m_flip_y = np.array([
            [1, 0, 0],
            [0, -1, self.y_size],
            [0, 0, 1]
        ])

        # 0: Identity matrix
        if id == 0:
            return m_identity

        # 1: Anticlockwise rotation
        elif id == 1:
            return m_anticlockwise

        # 2: Half rotation
        elif id == 2:
            return m_halfrotate

        # 3: Clockwise rotation
        elif id == 3:
            return m_clockwise

        # 4: Reflect along x-axis
        elif id == 4:
            return m_flip_x

        # 5: Reflect along y-axis
        elif id == 5:
            return m_flip_y

        # 6: Flip along y = -x axis
        elif id == 6:
            return np.matmul(m_clockwise, m_flip_y)

        # 7: Flip along y = x axis
        elif id == 7:
            return np.matmul(m_clockwise, m_flip_x)

        # Default: Identiy matrix
        else:
            return m_identity