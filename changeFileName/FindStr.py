import os
import re

# use for find all pic in markdown doc

# first get all file
dir = r"E:\elmagnificogi.github.io\_posts"

for file in os.listdir(dir):
    print(file)
    if ".markdown" in file:
        new_name = file.replace(".markdown", ".md")
        print(new_name)
        os.rename(dir+'\\'+file, dir+'\\'+new_name)
