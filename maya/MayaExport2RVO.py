f = open(r"F:\Github\RVO2-3D-update\examples\179.txt","r")
import json
data = json.load(f)
f.close()

spheres_num = len(data[0])/3
print "spheres num:"+str(spheres_num)

sum_frames = len(data)
print sum_frames

base_name = "dmd"

#for i in range(spheres_num):
#    cmds.polySphere(name=base_name+'#')

cur_time = 1



for cur in range(sum_frames):
    cmds.currentTime(cur +1)
    for i in range(0,len(data[cur*10]),3):
        pos = [data[cur*10][i],data[cur*10][i+1],data[cur*10][i+2]]
        name = base_name + str((i/3)+1)
        cmds.move(pos[0] + 2, pos[1], pos[2], name, ws=True)
        cmds.setKeyframe(name, attribute='translate')