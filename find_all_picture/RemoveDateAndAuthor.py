import os
import re

# use for find all pic in markdown doc

# first get all file
dir = r"F:\NXP\dmd_uav"
target_str = "![*](*)"
# origin_str = "Raspberrypi-head-bg.jpg"
# replace_str = "Raspberrypi-head-bg.png"
import datetime

for root, dirs, files in os.walk(dir):
    for file in files:
        # print(root)
        #print(file)
        suffix = file.split('.')
        #print(suffix)
        if len(suffix) < 2:
            continue
        # filter
        if  suffix[1] not in ['c', 'cpp', 'hpp', 'h']:
            continue
        
        file_path = os.path.join(root, file)
        print(file_path)
        
        f = open(file_path)
        try:
            content = f.readlines()
        except:
            f.close()
            continue
        f.close()
    # print(content)
        # replace it
        # f = open(file_path, 'w', encoding='utf-8')
        new_file = ""
        time_stamp = datetime.datetime.now()
        now = time_stamp.strftime('%Y.%m.%d %H:%M:%S')
        #continue
        find_title =False
        find_state = 0
        find_line = 0
        jump_line = False
        for line in content:
            new_line = line
            # print(line)
            if r'Copyright (c) Shenzheng DMDUAV Ltd. All rights reserved' in line:
                #print(line)
                find_state = 1
                find_line = 0
                find_title = True
            if find_state == 1 and find_line>0 and find_line < 7:
                print(line)
                find_line+=1
                jump_line = True
            else:
                jump_line = False
            if find_line == 0:
                find_line +=1
            if not jump_line:
                new_file+=new_line
                # print(line.replace(origin_str, replace_str))
                # new_line = line.replace(origin_str, replace_str)
        if find_title:
            #print("write a new file")
            f = open(file_path,'w')
            f.write(new_file)
            f.close()
            new_file += new_line