import os
import re

# use for find all pic in markdown doc

# first get all file
dir = r"E:\elmagnificogi.github.io\_posts"
target_str = "![*](*)"
#origin_str = "Raspberrypi-head-bg.jpg"
#replace_str = "Raspberrypi-head-bg.png"

for file in os.listdir(dir):
    # show file name
    print(file)
    file_path = dir + "\\" + file
    f = open(file_path, encoding='utf-8')
    content = f.readlines()
    f.close()
    # print(content)
    # replace it
    #f = open(file_path, 'w', encoding='utf-8')
    #new_file = ""
    for line in content:
        new_line = line
        # print(line)
        if re.search(r'!\[(.*)\]\((.*)\)',line) != None:
            print(line)
            #print(line.replace(origin_str, replace_str))
            #new_line = line.replace(origin_str, replace_str)

        #new_file += new_line
    #f.write(new_file)
    #f.close()