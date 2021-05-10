import colour
import math
import matplotlib.pyplot as plt
import numpy as np

grid_head = [[0, 0, 1], [0, 0, 0], [26 / 360.0, 1, 1], [39.0 / 360.0, 1, 1], [60 / 360.0, 1, 1], [81 / 360.0, 1, 1],
             [180.0 / 360.0, 1, 1], [216.0 / 360.0, 1, 1], [300.0 / 360.0, 1, 1], [341.0 / 360.0, 1, 1]]

grid_color = []

row_num = 6
col_num = 10

for hsv in grid_head:
    grid_color.append(hsv)
    # for i in range(row_num-1):

    if hsv == [0, 0, 0]:
        # black
        grid_color.append([hsv[0], hsv[1], 0.1])
        grid_color.append([hsv[0], hsv[1], 0.2])
        grid_color.append([hsv[0], hsv[1], 0.3])
        grid_color.append([hsv[0], hsv[1], 0.4])
        grid_color.append([hsv[0], hsv[1], 0.5])
    elif hsv == [0, 0, 1]:
        # white
        grid_color.append([hsv[0], hsv[1], 0.9])
        grid_color.append([hsv[0], hsv[1], 0.8])
        grid_color.append([hsv[0], hsv[1], 0.7])
        grid_color.append([hsv[0], hsv[1], 0.6])
        grid_color.append([hsv[0], hsv[1], 0.5])
    else:
        grid_color.append([hsv[0], hsv[1], 0.8])
        grid_color.append([hsv[0], hsv[1], 0.6])
        grid_color.append([hsv[0], hsv[1], 0.5])
        grid_color.append([hsv[0], hsv[1], 0.4])
        grid_color.append([hsv[0], hsv[1], 0.2])

gird_color_rc = []

for i in range(row_num):
    gird_color_rc.append(grid_color[i])
    gird_color_rc.append(grid_color[i + 1 * row_num])
    gird_color_rc.append(grid_color[i + 2 * row_num])
    gird_color_rc.append(grid_color[i + 3 * row_num])
    gird_color_rc.append(grid_color[i + 4 * row_num])
    gird_color_rc.append(grid_color[i + 5 * row_num])
    gird_color_rc.append(grid_color[i + 6 * row_num])
    gird_color_rc.append(grid_color[i + 7 * row_num])
    gird_color_rc.append(grid_color[i + 8 * row_num])
    gird_color_rc.append(grid_color[i + 9 * row_num])
    # gird_color_rc.append(grid_color[i+10*row_num])

print("-------")
a = colour.HSV_to_RGB(gird_color_rc)
# print(RGB)
print(a)

output = "{"
count = 1
for data in a:
    a = int(data[0] * 255) * 256 * 256 + int(data[1] * 255) * 256 + int(data[2] * 255)
    b = str(hex(a))[2:].upper().rjust(6, "0")
    print(b)
    print([hex(int(data[0] * 255)), hex(int(data[1] * 255)), hex(int(data[2] * 255))])
    output += '"' + b + '"'
    if count % 10 == 0 and count != 0:
        output += "},{"
    else:
        output += ','
    count += 1
output += "}"
print(output)
