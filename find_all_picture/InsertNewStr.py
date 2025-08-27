import os

# user for replace pic fomart str in markdown doc head

# first get all file
dir = r"K:\Download\LCXkl4\pages"
origin_str = "Forward"
replace_str = "Foreword"
line_num_limit = 30

delete_file_list = [
    "81SN8ME8AdNA16WrmgFLfL",
    "wKojQFStFZDQ5JXDkULrUn",
    "6i7GXJD9Npb4gNwDoVFAv5",
    "qa33MH4B8cnwhGxEpXvaCC",
    "wHPqSU2svHYptqsQCPZfx1",
    "7XTyLVazwQzExXaopFApVC",
    "wTHLv6DCfZG1kXuKxEDV8Z",
    "p1s4CrVVrLQwUDeKJNUYFy",
    "9SxC8M5bo7xijX8NKYbJtm",
    "p97Kaggp8CqFgAxSrdGLxx",
    "covzWF881fVirJ4zG5i2MH",
    "xzJG4PbAWi4RPZXQPEggXy",
    "5Pixzr7tz6Vre6oQ6VcoGC",
    "2WYdYg3LMJBNGSUnJEraeb",
    "8gEHknzWkRWXAX4JUCT7sL",
    "7hRyDKnYmRaieY93WWSMqT",
    "3PuUN94eBK3zgQMW9fB5Q3",
    "oKLS2V19yQUWCsF1WbHn7p",
    "ncUmMcwAxSgdzx8g4LxY3t",
]

for file in os.listdir(dir):
    # show file name
    print(file)
    # 检查文件后缀是否为.md
    if not file.endswith('.md'):
        continue
    # 获取文件名中下划线到点之间的内容
    parts = file.split('_')
    if len(parts) > 1:
        # 如果有下划线,取最后一部分并去掉.md后缀
        name = parts[-1].split('.')[0]
        doc_name = parts[0]
        #print(f"提取的内容: {name}")
        # 如果文件名在删除列表中则跳过
        if name in delete_file_list:
            print(f"删除文件: {name}")
            os.remove(dir + "\\" + file)
            continue
    url = "https://www.wolai.com/你的/"+name
    #print(url)
    insert_str = "["+doc_name+"原文链接]("+url+")"
    #print(insert_str)
    file_path = dir + "\\" + file
    f = open(file_path, encoding='utf-8')
    content = f.readlines()
    f.close()
    
    # 在第二行插入链接
    new_file = ""
    for i, line in enumerate(content):
        if i == 1:  # 在第二行插入
            new_file += insert_str + "\n\n"  # 添加两个换行确保格式正确
        new_file += line

    # 写回文件
    f = open(file_path, 'w', encoding='utf-8')
    f.write(new_file)
    f.close()