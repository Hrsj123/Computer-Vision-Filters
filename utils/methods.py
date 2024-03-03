import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def image_to_array(image_path: str) -> np.array:
    """Return np.array 2D (grayscale) of any image"""
    img = Image.open(image_path).convert('L')
    img = np.array(img)
    return img

def apply_padding(image: np.ndarray, value: int=0, width: int=1):
    """Apply padding to imput image (for grayscale only!)"""
    return np.pad(image, pad_width=width, mode='constant', constant_values=value)

def apply_filter(filter: np.ndarray, image: np.ndarray, padded: bool=False):
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

def plot_image(image: np.ndarray, filtered_images: np.ndarray=[]):
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

def normalize(matrix: np.ndarray, new_min: int=0, new_max: int=1):
  """
  Normalizes all values in a NumPy matrix to a specified range.

  Args:
    matrix: The NumPy matrix to be normalized.
    new_min: The minimum value for the normalized range (default 0).
    new_max: The maximum value for the normalized range (default 1).

  Returns:
    A new NumPy matrix with all values normalized to the specified range.
  """

  # Find minimum and maximum values in the matrix
  min_val = np.min(matrix)
  max_val = np.max(matrix)

  # Handle the case where all elements are equal
  if min_val == max_val:
    return matrix / min_val  # Normalize to new_min if all elements are the same

  # Normalize the matrix using vectorized operations
  return ((matrix - min_val) / (max_val - min_val)) * (new_max - new_min) + new_min
