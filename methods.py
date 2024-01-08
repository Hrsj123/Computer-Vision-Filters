import matplotlib.pyplot as plt
from edge_filters import edge_filters
import numpy as np
from PIL import Image

def image_to_array(image_path: str) -> np.array:
    """Return np.array 2D (grayscale) of any image"""
    img = Image.open(image_path).convert('L')
    img = np.array(img)
    return img

def apply_filter(filter, image, padded=False):
    """Apply given filter to an image"""
    l, w = len(image) - 2, len(image[0]) - 2
    filtered_image = np.zeros((l, w), dtype=float)
    for i in range(image.shape[0] - 2):
        for j in range(image.shape[1] - 2):
            filtered_image[i, j] = np.sum(image[i:i+3, j:j+3] * filter)
    filtered_image = filtered_image / np.max(filtered_image)
    # To create the filtered image of the same dimensions as the original image: 
    if padded:
        filtered_image = np.pad(filtered_image, 1, mode='constant')
    return filtered_image

def scharr_filter(img_array):
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

def plot_image(image, filtered_images):
    """Plot effects of multiple single filters"""
    l = len(filtered_images)
    plt.figure(figsize=(10, 5))
    plt.subplot(int(f'1{l+1}1'))
    plt.imshow(image, cmap="gray")
    plt.title("Original Image")
    for i, filtered_image in enumerate(filtered_images):     
        title, filtered_image = filtered_image
        plt.subplot(int(f'1{l+1}{i+2}'))
        plt.imshow(filtered_image, cmap="gray")
        plt.title(title)
    plt.show()
