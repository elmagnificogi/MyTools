import os
import re
#import requests

# first get all file
#dir = r"E:\Github\elmagnificogi.github.io\_posts"
dir = r"E:\elmagnificogi.github.io\_posts"

for file in os.listdir(dir):
    # show file name
    print(file)
    if not ".md" in file:
        continue
    file_path = dir + "\\" + file
    f = open(file_path, 'r', encoding='utf-8')
    content = f.readlines()
    f.close()

    lines = ""
    for line in content:
        new_line = ""
        # print(line)
        if re.search(r'<iframe src="//(.*)', line) != None:
            print(line)
            new_line = line.replace("src=\"//","src=\"https://")
            print(new_line)
        else:
            new_line = line

        lines += new_line

    f = open(file_path, 'w', encoding='utf-8')
    f.write(lines)
    f.close()
