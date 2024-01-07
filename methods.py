import matplotlib.pyplot as plt
import numpy as np
import cv2

def image_to_array(image_path: str) -> np.array:
    """Return np.array 2D (grayscale) of any image"""
    img = cv2.imread(image_path)
    img = np.array(img)
    if len(img.shape) == 3:
        img = np.mean(img, axis=2)
    return img

def apply_filter(filter, image):
    """Apply given filter to an image"""
    l, w = len(image) - 2, len(image[0]) - 2
    filtered_image = np.zeros((l, w), dtype=float)
    # To create the filtered image of the same dimensions as the original image: 
    # filtered_image = np.zeros_like(image)
    for i in range(image.shape[0] - 2):
        for j in range(image.shape[1] - 2):
            filtered_image[i, j] = np.sum(image[i:i+3, j:j+3] * filter)
    filtered_image = filtered_image / np.max(filtered_image)
    return filtered_image

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
