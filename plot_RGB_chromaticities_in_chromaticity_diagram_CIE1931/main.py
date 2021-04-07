import colour
import os
import numpy as np

# RGB = colour.read_image('F://temp//ACES2065-1_ColorChecker2014.exr')
# RGB = colour.read_image(r'ACES2065-1_ColorChecker2014.exr')
# RGB = np.array([[[1, 1, 1], [0.5, 0.5, 0.5], [0.2, 0.2, 0.2], [0.3, 0.3, 0.3]],[[1, 1, 1], [0.5, 0.5, 0.5], [0.2, 0.2, 0.2], [0.3, 0.3, 0.3]],[[1, 1, 1], [0.5, 0.5, 0.5], [0.2, 0.2, 0.2], [0.3, 0.3, 0.3]],[[1, 1, 1], [0.5, 0.5, 0.5], [0.2, 0.2, 0.2], [0.3, 0.3, 0.3]]])
RGB = np.array([[[0.36653649, 0.07554075, 0.28952463]], [[0.69990608,0.53677301,0.61425992]],[[0.99,0.99,0.99]]])
#RGB = np.random.random((2, 1, 3))
print(RGB)
colour.plotting.plot_RGB_chromaticities_in_chromaticity_diagram_CIE1931(
    RGB, colourspace='ACES2065-1', colourspaces=['sRGB'], scatter_kwargs={'c': 'k', 'marker': '+'})

# Customising the scatter appearance, the dict is passed to
# the "matplotlib.pyplot.scatter" definition.
# colour.plotting.plot_RGB_chromaticities_in_chromaticity_diagram_CIE1931(
#     RGB[::5, ::5, ...], colourspace='ACES2065-1', colourspaces=['sRGB'],
#     scatter_kwargs={'c': 'k', 'marker': '+'});
