import cv2
from numpy import *
from numpy import zeros

def yuv_import(filename, dims, numfrm, startfrm):
    fp = open(filename, 'rb')
    blk_size = prod(dims)
    fp.seek((int)(blk_size * startfrm), 0)
    Y = []
    U = []
    V = []
    print(dims[0])
    print(dims[1])
    d00 = int(dims[0])
    d01 = int(dims[1])
    print(d00)
    print(d01)
    Yt = zeros((dims[0], dims[1]), uint8, 'C')
    Ut = zeros((d00, d01), uint8, 'C')
    Vt = zeros((d00, d01), uint8, 'C')
    for i in range(numfrm):
        # for yuv packed YUYV
        for m in range(dims[0]):
            for n in range(0, int(dims[1]), 2):
                # print m,n  
                Yt[m, n] = ord(fp.read(1))
                Ut[m, n] = ord(fp.read(1))
                Yt[m, n + 1] = ord(fp.read(1))
                Vt[m, n] = ord(fp.read(1))
                Ut[m, n + 1] = Ut[m, n]
                Vt[m, n + 1] = Vt[m, n]
        # it's for yuv planar
        # for m in range(d00):
        #     for n in range(d01):
        #         Ut[m,n]=ord(fp.read(1))
        # for m in range(d00):
        #     for n in range(d01):
        #         Vt[m,n]=ord(fp.read(1))
        Y = Y + [Yt]
        U = U + [Ut]
        V = V + [Vt]
    fp.close()
    return (Y, U, V)


if __name__ == '__main__':
    width = 160
    height = 120
    data = yuv_import('./yuv_data/0.yuv', (height, width), 1, 0)
    YY = data[0][0]
    cv2.imshow("sohow", YY)
    cv2.waitKey(0)
