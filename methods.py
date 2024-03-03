from filters import edge_filters
import numpy as np
from utils.methods import normalize

def scharr_filter(img_array: np.ndarray):
    """Sharr filter to detect diagonal edges"""
    padded_img = np.pad(img_array, 1, mode='constant')
    filtered_x = np.zeros_like(img_array)
    filtered_y = np.zeros_like(img_array)
    for i in range(img_array.shape[0]):
        for j in range(img_array.shape[1]):
            filtered_x[i, j] = np.sum(padded_img[i:i+3, j:j+3] * edge_filters['scharr_filter']['x'])
            filtered_y[i, j] = np.sum(padded_img[i:i+3, j:j+3] * edge_filters['scharr_filter']['y'])
    # Combine the results to get the gradient magnitude
    gradient = np.sqrt(filtered_x**2 + filtered_y**2)
    # Normalize the gradient for visualization
    gradient = (gradient - gradient.min()) / (gradient.max() - gradient.min()) * 255
    gradient = gradient.astype(np.uint8)
    return gradient

def image_downscaler(image: np.ndarray, stride: tuple=(1, 1), filter_size=3, padding_width: int=3, padding_value=0):
    """Returns a condenced image with dimentions as (image_width-filter_size, image_height-filter_size)"""
    assert filter_size <= image.shape[0] and filter_size <= image.shape[1]

    image = np.pad(image, padding_width, mode='constant', constant_values=padding_value)

    start = 1
    seq = np.concatenate((
        np.arange(start, filter_size), 
        np.arange(filter_size - (1 if filter_size % 2 == 0 else 2), start - 1, -1)
    ))
    x, y = np.meshgrid(seq, seq)
    
    filter_arr: np.ndarray = normalize(x*y)
    output_img = np.zeros((
        image.shape[0] - len(filter_arr) + 1, 
        image.shape[1] - len(filter_arr) + 1,
    ))
    for i in range(0, image.shape[0] - len(filter_arr) + 1, stride[0]): # row
        for j in range(0, image.shape[1] - len(filter_arr) + 1, stride[1]): # each entry in row
            img_subset = image[i:i+len(filter_arr[0]), j:j+len(filter_arr[1])]
            output_img[i][j] = np.sum(img_subset * filter_arr)
    
    return normalize(output_img, new_max=255)

# def gaussian_blur(image, kernel_size=(3, 3), sigma=0.5):
#     """Applying gaussian denoising (this causes the img to blur)"""
#     eqn = lambda x, y, sigma: (1 / (2*np.pi*sigma**2)) * np.exp(-(x**2 + y**2) / (x*sigma**2))
    # Later!