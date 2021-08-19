import cv2
from numpy import *
from PIL import Image
from numpy import zeros
import colour
import numpy as np
import math
import os
import struct
import sys
import matplotlib.pyplot as plt

screenLevels = 255.0
def yuv_import(filename,dims,numfrm,startfrm):
    fp=open(filename,'rb')
    blk_size = prod(dims) #/ 2
    fp.seek((int)(blk_size*startfrm),0)
    Y=[]
    U=[]
    V=[]
    print(dims[0])
    print( dims[1])
    d00=int(dims[0]/2)
    d01=int(dims[1]/2)
    print( d00)
    print( d01)
    Yt=zeros((dims[0],dims[1]),uint8,'C')
    Ut=zeros((d00,d01),uint8,'C')
    Vt=zeros((d00,d01),uint8,'C')
    for i in range(numfrm):
        for m in range(dims[0]):
            for n in range(dims[1]):
                #print m,n  
                Yt[m,n]=ord(fp.read(1))
        for m in range(d00):
            for n in range(d01):
                Ut[m,n]=ord(fp.read(1))
        for m in range(d00):
            for n in range(d01):
                Vt[m,n]=ord(fp.read(1))
        Y=Y+[Yt]
        U=U+[Ut]
        V=V+[Vt]
    fp.close()
    return (Y,U,V)

filepath = "./yuv_data/0.pic"
f = open("./yuv_data/0.pic",'rb')


Y=[]
U=[]
V=[]
#data = f.readlines()
size = os.path.getsize(filepath)
for i in range(size):
    data = f.read(1)
    byte = struct.unpack('B',data)[0]
    if i %2==0:
        Y.append(byte)
    if i %4==1:
        U.append(byte)
    if i %4==3:
        V.append(byte)
#print(yuv)

if __name__ == '__main__':
    width=160
    height=120
    data=yuv_import('./yuv_data/127.pic',(height,width),1,0)
    #data = (Y,U,V)
    YY=data[0][0]
    cv2.imshow("sohow",YY)
    cv2.waitKey(0)