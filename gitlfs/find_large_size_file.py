import os
import re

# use for find all pic in markdown doc

# first get all file
dir = r"J:\GITLFS"
# dir = r"J:\GITLFS\基站3.0"

large_file_list = []


def traverse_folder(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            file_name = os.path.splitext(file_path)[1]
            # MB
            file_size = round(os.path.getsize(file_path) / 1024.0 / 1024.0, 3)
            # print(file_name, file_size, file_path)

            find_one = False
            for i in range(len(large_file_list)):
                if file_name == large_file_list[i][1]:
                    find_one = True
                    if file_size > large_file_list[i][2]:
                        large_file_list[i][0] = 0
                        large_file_list[i][1] = file_name
                        large_file_list[i][2] = file_size
                        large_file_list[i][3] = file_path
                    else:
                        break

            if find_one == False:
                large_file_list.append([0, file_name, file_size, file_path])


traverse_folder(dir)
sorted_arr = sorted(large_file_list, key=lambda x: x[2])
# for lf in sorted_arr:
#     print(lf[0], lf[1], lf[2])


new_lfs = []
lfs_config_path = r"J:\templete\.gitattributes"
lfr = open(lfs_config_path)
lines = lfr.readlines()
for l in lines:
    name = l.split(' ')[0]
    # print(name)
    nname = name[1:]
    # print(nname)
    for i in range(len(sorted_arr)):
        if sorted_arr[i][1] == nname:
            sorted_arr[i][0] = 1
            break
lfr.close()

for lf in sorted_arr:
    if lf[0] == 0:
        print("未添加 ", str(lf[1]).ljust(12), str(lf[2]).ljust(12) + "MB", lf[3])
    else:
        print("已优化 ", str(lf[1]).ljust(12), str(lf[2]).ljust(12) + "MB", lf[3])
