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
mem[local3] = 0xD3617DCA  # buff 前4字节
mem[local4] = 0x154369FC  # buff 后4字节
mem[local5] = 0  # 这个值每次也+8
mem[local6] = 0x4
mem[local7] = 0x1513F8C
mem[local8] = 0x20  # count 
mem[local9] = 0x100
mem[local10] = 0x318234B4
# 这个值来源不明
mem[local11] = 0x29A1FA54  # [ebp+edx*4-0x34]
mem[local12] = 0x9E81C901
mem[local13] = 0x81FBC617
mem[local14] = 0x4
mem[local15] = 0x513F8C
mem[0x19F168 - 6] = 0x7C00  # [ebp-0x6] 这个值每次+8

mem[0x19F20C] = 0x4FEA1C8

ebp = 0x19F168

ebx = ds[0x839634]
ebx = ebx * ds[0x839630] & 0xFFFFFFFF
eax = mem[local1]
eax = mem[eax]  # 0x4FEA1C8
edx = mem[local5]
eax = eax + edx
edx = mem[local4]
ecx = 0x8
# move 准备工作
# mem[local4] = 0x7EAB1EA0
# mem[local5] = 0x625214C8
eax = ds[0x839630]  # 20

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
    ebx = ds[0x839634]
    ebx = ebx * ds[0x839630] & 0xFFFFFFFF
    eax = mem[local1]
    eax = mem[eax]  # 0x4FEA1C8
    edx = mem[local5]
    eax = eax + edx
    edx = mem[local4]
    ecx = 0x8

    for i in range(32):
        # loop2
        esi = mem[local4]
        eax = esi
        eax = eax << 4 & 0xFFFFFFFF
        edx = esi
        edx = edx >> 5 & 0xFFFFFFFF
        eax = eax ^ edx
        eax = (eax + esi) & 0xFFFFFFFF
        edx = ebx
        edx = edx >> 0xB & 0xFFFFFFFF
        edx = edx & 0x3
        edx = mem[ebp + edx * 4 - 0x34]
        edx = (edx + ebx) & 0xFFFFFFFF
        ecx = mem[ebp - 0x6]
        edx = (edx + ecx) & 0xFFFFFFFF
        eax = eax ^ edx
        mem[local3] = (mem[local3] - eax) & 0xFFFFFFFF
        ebx = (ebx - ds[0x839634]) & 0xFFFFFFFF
        edi = mem[local3]
        eax = edi
        eax = eax << 4 & 0xFFFFFFFF
        edx = edi
        edx = edx >> 5 & 0xFFFFFFFF
        eax = eax ^ edx
        eax = (eax + edi) & 0xFFFFFFFF
        edx = 0x3
        edx = edx & ebx
        edx = mem[ebp + edx * 4 - 0x34]
        edx = (edx + ebx) & 0xFFFFFFFF
        ecx = mem[ebp - 0x6]
        edx = (edx + ecx) & 0xFFFFFFFF
        eax = eax ^ edx
        mem[local4] = (mem[local4] - eax) & 0xFFFFFFFF
        mem[local8] -= 1
        # loop2 end
    mem[local5] += 8
    mem[0x19F168 - 6] += 8

    decrypt_mem.append(mem[local4])
    decrypt_mem.append(mem[local3])

    # print(hex(mem[local3]))
    # print(hex(mem[local4]))

print(decrypt_mem)

def bytes2hex(data):
    lin = ['%02X' % i for i in data]
    return "".join(lin)

for i in range(0, 64, 2):
    print(hex((decrypt_mem[i + 0] & 0x00FF0000) >> 16).zfill(4) + hex((decrypt_mem[i + 0] & 0xFF000000) >> 24).replace("0x",'').zfill(2))

    print(hex((decrypt_mem[i + 1] & 0x000000FF)).zfill(4) + hex((decrypt_mem[i + 1] & 0x0000FF00) >> 8).replace("0x",'').zfill(2) + hex(
        (decrypt_mem[i + 1] & 0x00FF0000) >> 16).replace("0x",'').zfill(2) + hex((decrypt_mem[i + 1] & 0xFF000000) >> 24).replace("0x",'').zfill(2))

    # print(hex((decrypt_mem[i + 1] & 0x00FFFFFF) << 32 | decrypt_mem[i + 1]).zfill(16))
    # print(decrypt_mem[i+4])
    # print(decrypt_mem[i+5])
    # print(decrypt_mem[i+6])
    # print(decrypt_mem[i+7])

end = True
