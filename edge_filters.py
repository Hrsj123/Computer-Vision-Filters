import numpy as np

"""
Assigin any other filters here!
"""
edge_filters = {
    'horizontal_edge': np.array([
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1]
    ]),
    'vertical_edge': np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ])
}