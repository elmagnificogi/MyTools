f = open(r"F:\Github\RVO2-3D-update\examples\807.txt", "r")
import json

data = json.load(f)
f.close()

spheres_num = len(data[0]) / 3
print "spheres num:" + str(spheres_num)

sum_frames = len(data)
print sum_frames

base_name = "dmd"

# for i in range(spheres_num):
#    cmds.polySphere(name=base_name+'#')

cur_time = 1

spheres = []
for i in range(spheres_num):
    name = base_name + str((i) + 1)
    spheres.append(name)

data_interval = 1
time_interval = 1
break_time = 300

cmds.cutKey(spheres, time=(cur_time, len(data) / data_interval * time_interval + 1000), clear=True)
for line in range(0, len(data), data_interval):
    cmds.currentTime(cur_time)
    data_index = line
    for i in range(0, len(data[data_index]), 3):
        pos = [data[data_index][i], data[data_index][i + 1], data[data_index][i + 2]]
        name = base_name + str((i / 3) + 1)
        cmds.move(pos[0] + 2, pos[1], pos[2], name, ws=True)
        cmds.setKeyframe(name, attribute='translate')
    cur_time += time_interval
    if cur_time > break_time:
        break