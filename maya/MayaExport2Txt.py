name = "dmd"
num = 300
start_time = 1
end_time = 1715
output_file_path = r"F:\DmdPathFinding\Dmd_pathfinding\Dmd_pathfinding_test\Resourse\divider_test.txt"

f = open(output_file_path, "w")
ouput_str = []

cmds.currentTime(start_time)
for i in range(num):
    obj_name = name + str(i + 1)
    pos = cmds.objectCenter(obj_name, gl=True)
    pos[0] = round(pos[0], 2)
    pos[1] = round(pos[1], 2)
    pos[2] = round(pos[2], 2)

    ouput_str.append(str(pos[0]) + " " + str(pos[1]) + " " + str(pos[2]))

cmds.currentTime(end_time)
for i in range(num):
    obj_name = name + str(i + 1)
    pos = cmds.objectCenter(obj_name, gl=True)
    pos[0] = round(pos[0], 2)
    pos[1] = round(pos[1], 2)
    pos[2] = round(pos[2], 2)

    ouput_str[i] += " " + str(pos[0]) + " " + str(pos[1]) + " " + str(pos[2]) + "\n"

for s in ouput_str:
    f.write(s)
f.close()
