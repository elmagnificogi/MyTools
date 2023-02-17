import os
import re

# use for find all pic in markdown doc

# first get all file
dir = r"E:\Github\elmagnificogi.github.io\_posts"
#target_str = "![*](*)"
#target_str = "Foreword"#"Forward"
target_str = "Foreward"
line_num_limit = 30
#origin_str = "Raspberrypi-head-bg.jpg"
#replace_str = "Raspberrypi-head-bg.png"

for file in os.listdir(dir):
    # show file name
    #print(file)
    file_path = dir + "\\" + file
    f = open(file_path, encoding='utf-8')
    content = f.readlines()
    f.close()
    # print(content)
    # replace it
    #f = open(file_path, 'w', encoding='utf-8')
    #new_file = ""
    line_num = 0
    for line in content:
        new_line = line
        line_num+=1
        # print(line)
        if target_str in line and line_num < line_num_limit:
            print(file_path)
            break
        #new_file += new_line
    #f.write(new_file)
    #f.close()
