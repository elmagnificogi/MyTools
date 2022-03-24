import os

# user for replace pic fomart str in markdown doc head

# first get all file
dir = r"E:\elmagnificogi.github.io\_posts"
dir = r"E:\Github\elmagnificogi.github.io\_posts"
origin_str = "BLog"
replace_str = "Blog"
line_limit_num = 30

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
    find_tag = False
    line_num = 0
    for line in content:
        line_num +=1
        new_line = line
        if find_tag:
            #print(line)
            if origin_str in line and replace_str not in line:
                print(line)
                new_line = line.replace(origin_str,replace_str)
                print(new_line)
            
        if line == "---\n" and find_tag==True:
            find_tag=False
            #break
            
        if line == "tags:\n" and line_num <30:
            #print(line)
            find_tag = True
            
        new_file += new_line
    f.write(new_file)
    f.close()