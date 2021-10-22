import sys
import os

f = open(os.path.dirname(__file__) +"/rawdata.txt")
hex_data = f.read()
print hex_data

start = None
end = None

state = 0
for i in range(0, len(hex_data), 3):
    if (hex_data[i] + hex_data[i + 1]) == "FE" and state == 0:
        state = 1
    elif (hex_data[i] + hex_data[i + 1]) == "00" and state == 1:
        state = 2
    elif (hex_data[i] + hex_data[i + 1]) == "01" and state == 2:
        state = 3
    elif (hex_data[i] + hex_data[i + 1]) == "00" and state == 3:
        state = 4
        start = i - 9
        break
    else:
        state = 0

if start == None:
    print "no start,exit"
    sys.exit(0)

state = 0
for i in range(0, len(hex_data), 3):
    if (hex_data[i] + hex_data[i + 1]) == "30" and state == 0:
        state = 1
    elif (hex_data[i] + hex_data[i + 1]) == "01" and state == 1:
        state = 2
    elif (hex_data[i] + hex_data[i + 1]) == "01" and state == 2:
        state = 3
    elif (hex_data[i] + hex_data[i + 1]) == "C0" and state == 3:
        state = 4
        end = i - 9
        break
    else:
        state = 0

if end == None:
    print "no end,exit"
    sys.exit(0)

print(start, end)

print len(hex_data)
output_data = ""

n=4
for i in range(start, end, 3):
    output_data += "0x" + hex_data[i] + hex_data[i + 1] + ','
    n+=1
    if n%24==0:
        output_data+="\n"

f.close()

f = open(os.path.dirname(__file__) +"/settings.txt", 'w')
f.write(output_data[:-1])
print output_data[:-1]
