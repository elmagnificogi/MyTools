import os

# user for replace pic fomart str in markdown doc head

# first get all file
dir = r"E:\elmagnificogi.github.io\_posts"
dir = r"E:\Github\elmagnificogi.github.io\_posts"
origin_str = "Forward"
replace_str = "Foreword"
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
    line_num = 0
    for line in content:
        new_line = line
        # print(line)
        line_num+=1
        if line.find(origin_str) != -1 and line_num < line_num_limit:
            print(line)
            print(line.replace(origin_str, replace_str))
            new_line = line.replace(origin_str, replace_str)

        new_file += new_line
    f.write(new_file)
    f.close()
