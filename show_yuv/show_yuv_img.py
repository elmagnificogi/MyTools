import os
import struct
import matplotlib.pyplot as plt

filepath = "./yuv_data/0.yuv"
f = open("./yuv_data/0.yuv", 'rb')

yuv = []
size = os.path.getsize(filepath)
for i in range(size):
    data = f.read(1)
    byte = struct.unpack('B', data)[0]
    if i % 2 == 0:
        yuv.append(byte)
print(yuv)

fig, ax = plt.subplots()
ax.grid(False)
fig.tight_layout()
ax.set_title('yuv only show y')

for row in range(120):
    for col in range(160):
        index = (row * 160 + col)
        y = yuv[index]
        ax.plot([col], [(120 - row)], '.', linewidth=1, color='black', alpha=(255 - y) / 255.0)
plt.show()
