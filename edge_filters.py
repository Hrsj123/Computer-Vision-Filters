import numpy as np

"""
Assigin any other edge detection filters here!
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
    ]),
    'scharr_filter': {     # For diagonal edges!
        'x': np.array([[-3, 0, 3],
                    [-10, 0, 10],
                    [-3, 0, 3]]),
        'y': np.array([[-3, -10, -3],
                    [0, 0, 0],
                    [3, 10, 3]])
    },
    # 'prewitt_filter': np.array([    # For edges in all direction!

    # ]),
    # 'laplacian_filter': np.array([  # Finds abrupt intensity changes 

    # ])
}