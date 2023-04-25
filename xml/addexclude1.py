# -*- coding: UTF-8 -*-
# 从文件中读取数据
import xml.etree.ElementTree as ET

# 全局唯一标识
unique_id = 1


# 遍历所有的节点
def walkData(root_node, level, result_list):
    global unique_id
    temp_list = [unique_id, level, root_node.tag, root_node.attrib]
    result_list.append(temp_list)
    unique_id += 1

    # 遍历每个子节点
    children_node = root_node.getchildren()
    if len(children_node) == 0:
        return
    for child in children_node:
        walkData(child, level + 1, result_list)
    return


# 获得原始数据
# out:
# [
#    #ID, Level, Attr Map
#    [1, 1, {'ID':1, 'Name':'test1'}],
#    [2, 1, {'ID':1, 'Name':'test2'}],
# ]
def getXmlData(file_name):
    level = 1  # 节点的深度从1开始
    result_list = []
    root = ET.parse(file_name).getroot()
    walkData(root, level, result_list)

    return result_list


if __name__ == '__main__':
    file_name = 'movies.xml'
    file_name = 'demo.emProject'
    R = getXmlData(file_name)
    for x in R:
        print(x)
    pass