import os
import re
#import requests

# use for replace old url

# first get all file
dir = r"E:\Github\elmagnificogi.github.io\_posts"
#dir = r"E:\elmagnificogi.github.io\_posts"

# replace url
replace_url = "https://img.elmagnifico.tech/static/upload/elmagnifico/"

all_img_url = []

for file in os.listdir(dir):
    # show file name
    print(file)
    file_path = dir + "\\" + file
    f = open(file_path, 'r', encoding='utf-8')
    content = f.readlines()
    f.close()

    lines = ""
    for line in content:
        new_line = ""
        # print(line)
        if re.search(r'!\[(.*)\]\((.*)\)', line) != None:
            print(line)
            pre = line.find("![")
            # print(line[0:pre])
            new_line += line[0:pre]

            line = line.strip()
            img_url = line.split("![")
            # print(img_url)
            find = False
            for url in img_url:
                if url != "":
                    # print("!["+url)
                    # print(url)
                    # print(url.split("("))
                    prefix = "![]("
                    real_url = (url.split("("))[1]
                    # print(real_url)
                    real_url = real_url.split(")")[0]
                    all_img_url.append(real_url)
                    # print(real_url)
                    file_name = real_url.split("/")[-1]
                    file_name_index = url.find(file_name)
                    new_line += prefix + replace_url + file_name + ")"
                    print(new_line)
                    find = True
                else:
                    new_line += url
            if find:
                new_line += "\n"
        elif re.search(r'<img src=', line) != None:
            # check old img link
            new_line = line
            print(line)
        else:
            new_line = line

        lines += new_line

    f = open(file_path, 'w', encoding='utf-8')
    f.write(lines)
    f.close()
