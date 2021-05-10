import colour
import math
import matplotlib.pyplot as plt
import numpy as np

max_num = 58

#print(color_space_rgb)
#RGB = np.array(color_space_hsv)
RGB = [[0,0,1],[0,0,0]]
h = 0
s = 1
v = 1
h_inc = 1.0 / (max_num-1)
for i in range(max_num):
    RGB.append([h+i*h_inc,s,v])

print(RGB)

print("-------")
a = colour.HSV_to_RGB(RGB)
#print(RGB)
print(a)

output = "{"
count = 1
for data in a:
    a = int(data[0]*255)*256*256+int(data[1]*255)*256+int(data[2]*255)
    b = str(hex(a))[2:].upper().rjust(6,"0")
    print(b)
    print([hex(int(data[0]*255)),hex(int(data[1]*255)),hex(int(data[2]*255))])
    output+='"'+b+'"'
    if count % 10 == 0 and count!=0:
        output+="},{"
    else:
        output+=','
    count+=1
output+="}"
print(output)
