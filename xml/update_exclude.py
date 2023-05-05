#!/usr/bin/python
# -*- coding: UTF-8 -*-

import xml.dom.minidom

need_CI = ["Ov2f7", "Ov2h7", "Ov3", "Iv2h7"]
need_Boot = ["Ov2f7", "Ov2h7", "Ov3", "Iv2h7"]

ci_branch_map = {
    "Ov2f7": "Ov2f7_CI",
    "Ov2h7": "Ov2h7_CI",
    "Ov3": "Ov3_CI",
    "Iv2h7": "Iv2h7_CI",
}

boot_branch_map = {
    "Ov2f7": "Ov2f7_boot",
    "Ov2h7": "Ov2h7_boot",
    "Ov3": "Ov3_boot",
    "Iv2h7": "Iv2h7_boot",
}

DOMTree = xml.dom.minidom.parse("demo.emProject")
collection = DOMTree.documentElement
project = collection.getElementsByTagName("project")[0]
folders = project.getElementsByTagName("folder")
#print(len(folders))

root_dir = folders[0]
#print("root child:" + str(root_dir.childNodes.length))

exclude_nodes = {}

confs = root_dir.getElementsByTagName('configuration')
if len(confs) > 0:
    #print(len(confs))
    for conf in confs:
        if conf.hasAttribute("build_exclude_from_build"):
            if conf.parentNode in exclude_nodes:
                exclude_nodes[conf.parentNode].append(conf)
            else:
                exclude_nodes[conf.parentNode] = [conf]
            # if conf.parentNode not in exclude_nodes:
            #     exclude_nodes.append(conf.parentNode)
            if conf.hasAttribute("Name"):
                name = conf.parentNode.getAttribute("Name")
                if name == "":
                    name = conf.parentNode.getAttribute("file_name")
                # print(name + " exclude from " + conf.getAttribute("Name"))

#print("*" * 50)
doc = DOMTree
# deal all exclude node
for node in exclude_nodes:
    type = 1
    name = node.getAttribute("Name")
    if name == "":
        type = 2
        name = node.getAttribute("file_name")

    branchs = []
    last_conf = ""
    for conf in exclude_nodes[node]:
        branch = conf.getAttribute("Name")
        #print(name + " exclude from " + branch)
        branchs.append(branch)
        last_conf = conf

    to_add = []
    for branch in branchs:
        if branch in need_CI:
            ci_branch = ci_branch_map[branch]
            if ci_branch not in branchs:
                to_add.append(ci_branch)
                #print("need add CI " + ci_branch)
        if branch in need_Boot:
            boot_branch = boot_branch_map[branch]
            if boot_branch not in branchs:
                to_add.append(boot_branch)
                #print("need add boot " + boot_branch)

    # get tab
    tab = last_conf.previousSibling
    for branch in to_add:
        n = doc.createElement("configuration")

        at_name = doc.createAttribute("Name")
        at_name.value = branch
        n.setAttributeNode(at_name)

        ex = doc.createAttribute("build_exclude_from_build")
        ex.value = "Yes"
        n.setAttributeNode(ex)

        new = node.insertBefore(n, last_conf)

        newline = doc.createTextNode("")
        node.insertBefore(newline, last_conf)

        new_tab = tab.cloneNode(deep=False)
        node.insertBefore(new_tab, last_conf)

f = open("demo1.emProject", "w")
doc.writexml(f)
f.close()
