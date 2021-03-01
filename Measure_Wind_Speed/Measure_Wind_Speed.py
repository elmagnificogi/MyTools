f = open("my AcuRite PC Connect Log.txt",'r',encoding='UTF-8')
fout = open("wind.csv","w+")

lines = f.readlines()
for line in lines:
    if line.find('Raw bytes:01') != -1 :
        #print(line);
        raw = line.split(" ")
        n = ((int(raw[7],16) & 0x1f) << 3) | ((int(raw[8],16) & 0x70) >> 4)
        #print(int(raw[7],16),int(raw[8],16))
        #print(n)
        if n == 0:
            kph = 0
        else :
            kph = 0.8278 * n + 1.0
        mps = kph / 3.6
        #print(mps)
        fout.write(raw[0] + ',' + str(mps) + '\n')
f.close()
fout.close()