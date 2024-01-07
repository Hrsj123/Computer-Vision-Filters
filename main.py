from methods import image_to_array, apply_filter, plot_image
from edge_filters import edge_filters

img_path = './Images/{}'

img = image_to_array(img_path.format('lowpoly_circle.jpg'))

filters = [
    ('Horizontal Edges', apply_filter(edge_filters['horizontal_edge'], img)),
    ('Vertical Edge', apply_filter(edge_filters['vertical_edge'], img)),
]

plot_image(img, filters)