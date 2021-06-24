import os
import re

# use for find all pic in markdown doc

# first get all file
dir = r"F:\GD32\dmd_uav_f4"
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
        time_line = " * Date    : "+now+'\n'
        #continue
        find_time =False
        for line in content:
            new_line = line
            # print(line)
            if re.search(r' * Date    :', line) != None:
                print(line)
                new_line = time_line
                find_time = True
            new_file+=new_line
                # print(line.replace(origin_str, replace_str))
                # new_line = line.replace(origin_str, replace_str)
        if find_time:
            f = open(file_path,'w')
            f.write(new_file)
            f.close()
            # new_file += new_line
        # f.write(new_file)
        # f.close()
