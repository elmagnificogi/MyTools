import datetime
import csv
import sys

# export implicit-crowds data format in csv
# implicit-crowds repository:https://github.com/johnoriginal/implicit-crowds

spheres = cmds.ls("dmd*", selection=True, transforms=True)
start_time = 1
end_time = 313

curpath = "F:\\Github\\implicit-crowds\\data\\"
cur_time = datetime.datetime.now().__format__('%Y%m%d%H%M%S')

start_poss = []
end_poss = []

min_x = min_y = sys.float_info.max
max_x = max_y = sys.float_info.min

cmds.currentTime(start_time)
for s in spheres:
    pos = cmds.objectCenter(s, gl=True)
    # print pos
    start_str = str(pos[0]) + " " + str(pos[2])
    start_poss.append(start_str)
    min_x = min(pos[0], min_x)
    min_y = min(pos[2], min_y)
    max_x = max(pos[0], max_x)
    max_y = max(pos[2], max_y)

cmds.currentTime(end_time)
for s in spheres:
    pos = cmds.objectCenter(s, gl=True)
    # print pos
    start_str = str(pos[0]) + " " + str(pos[2])
    end_poss.append(start_str)
    min_x = min(pos[0], min_x)
    min_y = min(pos[2], min_y)
    max_x = max(pos[0], max_x)
    max_y = max(pos[2], max_y)

with open(curpath + cur_time + '.csv', 'w') as f:
    writer = csv.writer(f)
    index = 0
    speed = 4.0
    radius = 1.74
    writer.writerow([str(min_x - 10) + " " + str(max_x + 10)])
    writer.writerow([str(min_y - 10) + " " + str(max_y + 10)])
    writer.writerow([str(len(spheres))])
    for s in spheres:
        writer.writerow(
            [str(index) + " " + start_poss[index] + " " + end_poss[index] + " " + str(speed) + " " + str(radius)])
        index += 1
