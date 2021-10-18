import os
import sys

ds = {}
ds[0x839634] = 0x9E3779B9
ds[0x839630] = 0x20
local0 = 0x19F168
local1 = 0x19F164
local2 = 0x19F160  # [ebp-0x6]
local3 = 0x19F15C
local4 = 0x19F158
local5 = 0x19F154
local6 = 0x19F150
local7 = 0x19F14C
local8 = 0x19F148
local9 = 0x19F144
local10 = 0x19F140
local11 = 0x19F13C  # [ebp+edx*4-0x34]
local12 = 0x19F138
local13 = 0x19F134
local14 = 0x19F130
local15 = 0x19F12C
mem = {}
# uart buff addr
mem[local1] = 0x19F20C
mem[local2] = 0x7C00A1C8
mem[local3] = 0  
mem[local4] = 0x154369FC  #
mem[local5] = 0  # 
mem[local6] = 0x4
mem[local7] = 0x1513F8C
mem[local8] = 0x20  # count 
mem[local9] = 0x100
# 
mem[local10] = 0x318234B4  # need
mem[local11] = 0x29A1FA54  # [ebp+edx*4-0x34] need
mem[local12] = 0x9E81C901 # need
mem[local13] = 0x81FBC617 # 0x19F134 need
mem[local14] = 0x4
mem[local15] = 0x513F8C
mem[0x19F168 - 6] = 0x7C00  # [ebp-0x6] 

mem[0x19F20C] = 0x4FEA1C8

ebp = 0x19F168

# mem[local4] = 0x7EAB1EA0
# mem[local5] = 0x625214C8
eax = ds[0x839630]  # 0x20

# uart buff
uart_buff = []
f = open(os.path.dirname(__file__) + "/crypt_data.txt")
hex_data = f.read()
print(hex_data)
start = None
end = None

state = 0
for i in range(0, len(hex_data), 3):
    if (hex_data[i] + hex_data[i + 1]) == "03" and state == 0:
        state = 1
    elif (hex_data[i] + hex_data[i + 1]) == "00" and state == 1:
        state = 2
    elif (hex_data[i] + hex_data[i + 1]) == "00" and state == 2:
        state = 3
    elif (hex_data[i] + hex_data[i + 1]) == "F0" and state == 3:
        state = 4
        start = i + 3
        break
    else:
        state = 0
if start == None:
    print("no start,exit")
    sys.exit(0)

print(len(hex_data))
output_data = ""

n = 4
for i in range(start, start + 256 * 3, 3):
    print(hex_data[i], hex_data[i + 1])
    uart_buff.append("" + hex_data[i] + hex_data[i + 1])
    # uart_buff.append(int(""+hex_data[i] + hex_data[i + 1],base=16))

f.close()

print(uart_buff)

decrypt_mem = []

# loop1
mem[local8] = eax
for i in range(0, 0x100, 8):
    mem[local4] = int(uart_buff[i + 3] + uart_buff[i + 2] + uart_buff[i + 1] + uart_buff[i + 0], base=16)
    mem[local3] = int(uart_buff[i + 7] + uart_buff[i + 6] + uart_buff[i + 5] + uart_buff[i + 4], base=16)

    ebx = ds[0x839634] * ds[0x839630] & 0xFFFFFFFF
    
    for i in range(32):
        # loop2
        eax = mem[local4] << 4 & 0xFFFFFFFF
        edx = mem[local4] >> 5 & 0xFFFFFFFF
        eax = eax ^ edx
        eax = (eax + mem[local4]) & 0xFFFFFFFF
        edx = ebx >> 0xB & 0xFFFFFFFF
        edx = edx & 0x3
        local = 0x19F134 + edx * 4
        edx = mem[local]
        edx = (edx + ebx) & 0xFFFFFFFF
        edx = (edx + mem[ebp - 0x6]) & 0xFFFFFFFF
        eax = eax ^ edx
        mem[local3] = (mem[local3] - eax) & 0xFFFFFFFF
        ebx = (ebx - ds[0x839634]) & 0xFFFFFFFF
        
        eax = mem[local3] << 4 & 0xFFFFFFFF
        edx = mem[local3] >> 5 & 0xFFFFFFFF
        eax = eax ^ edx
        eax = (eax + mem[local3]) & 0xFFFFFFFF
        edx = 0x3 & ebx
        edx = mem[ebp + edx * 4 - 0x34]
        edx = (edx + ebx) & 0xFFFFFFFF
        edx = (edx + mem[ebp - 0x6]) & 0xFFFFFFFF
        eax = eax ^ edx
        mem[local4] = (mem[local4] - eax) & 0xFFFFFFFF
        # loop2 end
    mem[0x19F168 - 6] += 8

    decrypt_mem.append(mem[local4])
    decrypt_mem.append(mem[local3])

    # print(hex(mem[local3]))
    # print(hex(mem[local4]))

print(decrypt_mem)

def byte2hex(data):
    lin = '%02X' % data
    return "0x"+"".join(lin)

pd = ""
for i in range(0, 64, 2):
    #print ((decrypt_mem[i + 0] & 0x00FF0000) >> 16)
    data = byte2hex((decrypt_mem[i + 0] & 0x00FF0000) >> 16)
    pd = data+" "
    #print(data)    
    data = byte2hex((decrypt_mem[i + 0] & 0xFF000000) >> 24)
    pd += data+" "
    #print(data)
    data = byte2hex((decrypt_mem[i + 1] & 0x000000FF) >> 0)
    pd += data+" "
    #print(data)
    data = byte2hex((decrypt_mem[i + 1] & 0x0000FF00) >> 8)
    pd += data+" "
    #print(data)
    data = byte2hex((decrypt_mem[i + 1] & 0x00FF0000) >> 16)
    pd += data+" "
    #print(data)
    data = byte2hex((decrypt_mem[i + 1] & 0xFF000000) >> 24)
    pd += data
    #print(data)
    print(pd)
