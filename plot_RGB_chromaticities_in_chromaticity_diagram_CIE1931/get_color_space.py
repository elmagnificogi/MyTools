import colour
import numpy as np
import math


def hsi2rgb(hsv):
    h = float(hsv[0])
    s = float(hsv[1])
    v = float(hsv[2])
    h60 = h / 60.0
    h60f = math.floor(h60)
    hi = int(h60f) % 6
    f = h60 - h60f
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    r, g, b = 0, 0, 0
    if hi == 0:
        r, g, b = v, t, p
    elif hi == 1:
        r, g, b = q, v, p
    elif hi == 2:
        r, g, b = p, v, t
    elif hi == 3:
        r, g, b = p, q, v
    elif hi == 4:
        r, g, b = t, p, v
    elif hi == 5:
        r, g, b = v, p, q
    r, g, b = int(r * 255), int(g * 255), int(b * 255)
    return [r, g, b]


f = open("./LightColor_1.txt")
lines = f.readlines()
f.close()

color_space_hsi = []

max_light = 0
min_light = 0
for line in lines[1:]:
    data = line.split(',')
    # print(data)
    max_light = max(int(data[5]), max_light)
    min_light = min(int(data[5]), min_light)
    color_space_hsi.append([int(data[3]), int(data[4]), int(data[5])])

print("max and min light:")
print(max_light)
print(min_light)

color_space_hsv = []
for hsi in color_space_hsi:
    color_space_hsv.append([hsi[0] / 360.0, hsi[1] / 100.0, hsi[2] * 1.0 / max_light])

color_space_rgb = []
for hsv in color_space_hsv:
    color_space_rgb.append(colour.HSV_to_RGB(hsv))

# print(color_space_rgb)
# RGB = np.array(color_space_hsv)
# print(RGB)
# print("-------")
# colour.HSV_to_RGB(RGB)
# print(RGB)
#
# print(RGB)
colour.plotting.plot_RGB_chromaticities_in_chromaticity_diagram_CIE1931(
    [], colourspace='ACES2065-1', colourspaces=['sRGB'])

colour.plotting.plot_RGB_chromaticities_in_chromaticity_diagram_CIE1931(
    color_space_rgb, colourspace='ACES2065-1')
