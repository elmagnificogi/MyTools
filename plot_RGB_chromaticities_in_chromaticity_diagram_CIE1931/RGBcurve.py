import colour
import math
import matplotlib.pyplot as plt
import numpy as np

f = open("./LightColor_0-255.txt")
lines = f.readlines()
f.close()

blue_data = []
blue_index = []
b_index = 0

red_data = []
red_index = []
r_index = 0

green_data = []
green_index = []
g_index = 0

for line in lines[1:]:
    data = line.split(',')
    # print(data)
    # max_light = max(int(data[5]), max_light)
    # min_light = min(int(data[5]), min_light)

    if data[1] == '0' and data[2] == '0':
        # blue_data[int(data[2])]=(int(data[3]), int(data[4]), int(data[5]))
        red_data.append((int(data[3]), int(data[4]), int(data[5])))
        red_index.append(r_index)
        r_index += 1

    if data[0] == '0' and data[2] == '0':
        # blue_data[int(data[2])]=(int(data[3]), int(data[4]), int(data[5]))
        green_data.append((int(data[3]), int(data[4]), int(data[5])))
        green_index.append(g_index)
        g_index += 1

    if data[0] == '0' and data[1] == '0':
        # blue_data[int(data[2])]=(int(data[3]), int(data[4]), int(data[5]))
        blue_data.append((int(data[3]), int(data[4]), int(data[5])))
        blue_index.append(b_index)
        b_index += 1

plt.plot(red_index, red_data)
plt.show()

plt.plot(green_index, green_data)
plt.show()

plt.plot(blue_index, blue_data)
plt.show()



