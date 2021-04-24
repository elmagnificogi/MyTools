import colour
import math
import matplotlib.pyplot as plt
import numpy as np

#f = open("./LightColor_0-255.txt")
f = open("./LightColor_5081_0-255.txt")
lines = f.readlines()
f.close()

min_saturation = 100
intensity_limit = 9999
saturation_limit = 5

r_255 = []
g_255 = []
b_255 = []
white_list_sorted = []
first = True
append_white = []

while len(white_list_sorted) <= 1:
    low_saturation_list = []
    if not first:
        intensity_limit -= 100

    for line in lines[1:]:
        data = line.split(',')
        # print(data)
        # max_light = max(int(data[5]), max_light)
        # min_light = min(int(data[5]), min_light)

        # filter the data
        if int(data[5]) > intensity_limit and int(data[4]) < saturation_limit:
            min_saturation = min(int(data[4]), min_saturation)
            low_saturation_list.append(
                (int(data[0]), int(data[1]), int(data[2]), int(data[3]), int(data[4]), int(data[5])))

        # find r,g,b max data
        if data[0] == '255' and data[1] == '0' and data[2] == '0':
            r_255 = data

        if data[0] == '0' and data[1] == '255' and data[2] == '0':
            g_255 = data

        if data[0] == '0' and data[1] == '0' and data[2] == '255':
            b_255 = data

    # first time,update the intensity_limit
    if first:
        print(r_255)
        print(g_255)
        print(b_255)
        intensity_limit = max(int(r_255[5]), int(g_255[5]), int(b_255[5]))
        first = False

    # white evaluation
    white_list = []
    for c in low_saturation_list:
        score = c[0] + c[1] + c[2]
        score += -c[4] * 100 + c[5]
        white_list.append((score, c))

    # just one data,try next time
    if len(white_list) == 1:
        append_white.append(white_list[0])
        continue

    # append last white data
    for c in append_white:
        white_list.append(c)
    append_white = []

    # sort it
    white_list_sorted = sorted(white_list, key=lambda x: x[0], reverse=True)

    # print(white_list_sorted)
    # find one
    if len(white_list_sorted) > 1:
        print(white_list_sorted[0])
        break
print("Find white point")

rgb_scale = (white_list_sorted[0][1][0] / 255.0, white_list_sorted[0][1][1] / 255.0, white_list_sorted[0][1][2] / 255.0)
# print(rgb_scale)
# normalize it
scale = 1.0 / max(rgb_scale[0], rgb_scale[1], rgb_scale[2])
rgb_scale_normalized = (rgb_scale[0] * scale, rgb_scale[1] * scale, rgb_scale[2] * scale)

print(rgb_scale_normalized)
