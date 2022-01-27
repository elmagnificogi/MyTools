import os
import re
import requests

# use for find all pic in markdown doc

# first get all file
dir = r"E:\Github\elmagnificogi.github.io\_posts"
target_str = "![*](*)"
#origin_str = "Raspberrypi-head-bg.jpg"
#replace_str = "Raspberrypi-head-bg.png"

def download(url):
    print ("download:"+url)
    header = {}
    r = requests.get(url, headers=header, stream=True)
    print(r.status_code) # 返回状态码
    file_name = url.split("/")[-1]
    print("file:"+file_name)
    if r.status_code == 200:
        open('.\img\\'+file_name, 'wb').write(r.content) # 将内容写入图片
        print("done")
    del r

all_img_url = []

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
            # # check some un SM.MS pic
            # if "loli" in line:
            #     continue
            # else:
            #     print(line)
            # split imgs in one line
            line = line.strip()
            img_url = line.split("![")
            #print(line)
            for url in img_url:
                if url != "":
                    #print("!["+url)
                    #print(url)
                    #print(url.split("("))
                    real_url = (url.split("("))[1]
                    #print(real_url)
                    real_url = real_url.split(")")[0]
                    all_img_url.append(real_url)
                    print(real_url)
                    download(real_url)
            continue
        elif re.search(r'<img src',line) != None:
            # check old img link
            print(line)
            #print(line.replace(origin_str, replace_str))
            #new_line = line.replace(origin_str, replace_str)

        #new_file += new_line
    #f.write(new_file)
    #f.close()