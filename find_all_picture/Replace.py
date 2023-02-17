import os

# user for replace a str in markdown doc

# first get all file
dir = r"E:\elmagnificogi.github.io\_posts"
dir = r"E:\Github\elmagnificogi.github.io\_posts"
no_replace = []
origin_str = "png"
replace_str = "jpg"
line_num_limit = 30

for file in os.listdir(dir):
    # show file name
    print(file)
    file_path = dir + "\\" + file
    f = open(file_path, encoding='utf-8')
    content = f.readlines()
    f.close()
    # print(content)
    # replace it
    f = open(file_path, 'w', encoding='utf-8')
    new_file = ""
    for line in content:
        new_line = line
        # print(line)
        find = False
        # jump no replace
        if line.find("header-img:") != -1:
            for np in no_replace:
                if line.find(np) != -1:
                    find = True
                    break

            if not find:
                print(line)
                print(line.replace(origin_str, replace_str))
                new_line = line.replace(origin_str, replace_str)

        new_file += new_line
    f.write(new_file)
    f.close()
