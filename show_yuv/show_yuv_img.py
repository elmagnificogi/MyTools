import colour
import numpy as np
import math
import os
import struct
import sys
import matplotlib.pyplot as plt
filepath = "./yuv_data/0.pic"
f = open("./yuv_data/0.pic",'rb')

yuv=[]
#data = f.readlines()
size = os.path.getsize(filepath)
for i in range(size):
    data = f.read(1)
    byte = struct.unpack('B',data)[0]
    if i %2==0:
        yuv.append(byte)
print(yuv)

#plt.plot([50,1],[40,12],"red")
# plt.plot([50],[40],'red',[30,0,0])
# plt.show()
# while True:
#     pass
import matplotlib.cbook as cbook

# Load a numpy record array from yahoo csv data with fields date, open, close,
# volume, adj_close from the mpl-data/example directory. The record array
# stores the date as an np.datetime64 with a day unit ('D') in the date column.
with cbook.get_sample_data('goog.npz') as datafile:
    price_data = np.load(datafile)['price_data'].view(np.recarray)
price_data = price_data[-250:] # get the most recent 250 trading days

delta1 = np.diff(price_data.adj_close) / price_data.adj_close[:-1]

# Marker size in units of points^2
volume = (15 * price_data.volume[:-2] / price_data.volume[0])**2
close = 0.003 * price_data.close[:-2] / 0.003 * price_data.open[:-2]

fig, ax = plt.subplots()
ax.scatter(delta1[:-1], delta1[1:], c=close, s=volume, alpha=0.5)

ax.set_xlabel(r'$\Delta_i$', fontsize=15)
ax.set_ylabel(r'$\Delta_{i+1}$', fontsize=15)
ax.set_title('Volume and percent change')

ax.grid(True)
fig.tight_layout()

plt.show()

fig , ax = plt.subplots()
#ax.plot([1],[2],'.',alpha=0.1)
ax.set_title('Simple Scatter')

#ax.plot([2],[3],'.',alpha=1)

#plt.show()

#sys.exit(0)

# col = []#np.arange(1,160,1)
# row = []#np.arange(1,120,1)
# 
# for r in range(120):
#     for c in range(160):
#         col.append(c)
#         row.append(row)
#         # index = (row*160+col)
#         # y = yuv[index]
#         # #print(hex(y))
#         # print(col,120-row)
#         # #t.append(col)
#         # plt.plot([col],[120-row],'black',alpha = y/255.0)
# 
# plt.scatter(col,row,s=1,c='b',alpha=yuv)

for row in range(120):
    for col in range(160):
        index = (row*160+col)
        y = yuv[index]
        #print(hex(y))
        #print(col,120-row)
        #t.append(col)

        ax.plot([col*100],[(120-row)*100],'.',linewidth=1,color='black',alpha=y/255.0)
    if index>=100:
        break
        #plt.plot([col],[120-row],'black',alpha = y/255.0)
    #t=[]
    #break
        #plt.plot([col],[120-row],'black',[y,y,y])
plt.show()
#plt.plot([1,2,3],[4,5,6],'ro')
#plt.plot([2,3,4],[1,2,3],'green')


