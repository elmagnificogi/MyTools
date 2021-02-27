spheres = cmds.ls("dmd*", selection=True, transforms=True)
start_time = 1
end_time = 314

cmds.currentTime(start_time)
start_str = "{"
for s in spheres:
    pos = cmds.objectCenter(s, gl=True)
    # print pos
    start_str += str(pos[0]) + "," + str(pos[1]) + "," + str(pos[2]) + ","

start_str += "}"
print start_str

cmds.currentTime(end_time)
start_str = "{"
for s in spheres:
    pos = cmds.objectCenter(s, gl=True)
    # print pos
    start_str += str(pos[0]) + "," + str(pos[1]) + "," + str(pos[2]) + ","

start_str += "}"
print start_str