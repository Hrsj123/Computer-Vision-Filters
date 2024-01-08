from methods import image_to_array, apply_filter, plot_image, scharr_filter
from edge_filters import edge_filters

img_path = './Images/{}'
file_name = 'lowpoly_circle.jpg'
# file_name = 'anvil.jpg'

img = image_to_array(img_path.format(file_name))

# Vertical and Horizontal filters
filters_list = [
    ('Horizontal Edges', apply_filter(edge_filters['horizontal_edge'], img)),
    ('Vertical Edge', apply_filter(edge_filters['vertical_edge'], img)),
]
plot_image(img, filters_list)

# Scharr filter: To detect diagonal edges
filters_list = [
    ('Scharr Filter', scharr_filter(img))
]
plot_image(img, filters_list)