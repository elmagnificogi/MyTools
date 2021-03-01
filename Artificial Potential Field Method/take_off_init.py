import sys
import maya.cmds as cmds
import copy
import random
import math
import datetime
import csv
# save the default console interface -- maya script editor
__console__=sys.stdout
reload(sys)
# set gbk encode for Chinese
sys.setdefaultencoding('gbk')

class Sports_quality:
    def __init__(self,name,cur_pos,target_pos):
        self.pos   = cur_pos
        self.pre_pos = copy.deepcopy(cur_pos)
        self.target = target_pos
        self.acc   = [0.0,0.0,0.0]
        self.speed = [0.0,0.0,0.0]
        self.mass      = 1.0
        self.max_acc   = 2.4
        self.max_speed = 2.4
        self.max_dis = ((cur_pos[2] - target_pos[2]) ** 2 + (cur_pos[1] - target_pos[1]) ** 2 + (cur_pos[0] - target_pos[0]) ** 2) ** 0.5
        self.pos_list = []
        self.pos_list.append(tuple(cur_pos))
        self.knote = 0
        self.k = []
        self.k.append(self.knote)
        self.arrived = False 
        self.updated = False
        self.obj = name
        self.slow_speed = 0
        self.transfer_force = [0.0,0.0,0.0]
        self.dv_direction = {}
        # 0 ground
        # 1 takingoff
        # 2 cruising
        self.state = 0

        obj_name = name
        if not cmds.attributeQuery('speed',node = obj_name,exists = True):
            cmds.select(obj_name)
            cmds.addAttr(longName = 'speed', attributeType = 'double', defaultValue = 0.0, keyable=True)
            cmds.setAttr(obj_name + '.speed',edit = True,keyable = True)
            
            cmds.addAttr(longName = 'speed_x', attributeType = 'double', defaultValue = 0.0, keyable=True)
            cmds.setAttr(obj_name + '.speed_x',edit = True,keyable = True)
            
            cmds.addAttr(longName = 'speed_y', attributeType = 'double', defaultValue = 0.0, keyable=True)
            cmds.setAttr(obj_name + '.speed_y',edit = True,keyable = True)
            
            cmds.addAttr(longName = 'speed_z', attributeType = 'double', defaultValue = 0.0, keyable=True)
            cmds.setAttr(obj_name + '.speed_z',edit = True,keyable = True)
            
            cmds.addAttr(longName = 'speed_xy', attributeType = 'double', defaultValue = 0.0, keyable=True)
            cmds.setAttr(obj_name + '.speed_xy',edit = True,keyable = True)   

# clear the windows
Dmd_UAVC_exfunc_clear_output_windows()

# get the operation object
Dmd_UAVC_reset_radius()

cmds.currentTime(1,update = True)
spheres = cmds.ls("dmd*", transforms = True)
cmds.setKeyframe(spheres)

takeoff_safe_radius = 8.0
ground_height = 0.0
takeoff_height = 10.0
takeoff_num = len(spheres)
target_time = 3400

# table of takeoff time
takeoff_table = {}

# get the graph center
center = [0.0,0.0,0.0]
for s in spheres:
    pos = cmds.objectCenter(s,gl = True)
    center[0] += pos[0]
    center[1] += pos[1]
    center[2] += pos[2]

center[0] /= len(spheres)
center[1] /= len(spheres)
center[2] /= len(spheres)

ground_height = center[2]
#print height_limit
# a new one

# first get the dis of source to dest
search_list = {}
source_pos = {}
dest_pos = {}

cmds.currentTime(1,update = True)
for s in spheres:
    source_pos[s] = cmds.objectCenter(s,gl = True)

cmds.currentTime(target_time,update = True)
for s in spheres:
    dest_pos[s] = cmds.objectCenter(s,gl = True)

for s in spheres:
    pos = source_pos[s]
    pos1 = dest_pos[s]
    dis = (pos[0] - pos1[0]) ** 2 + (pos[1] - pos1[1]) ** 2 + (pos[2] - pos1[2]) ** 2
    dis = dis ** 0.5
    search_list[s] = dis

search_list_sorted = sorted(search_list.items(),key = lambda x:x[1],reverse = True)

first_takeoff_list = []
#first_takeoff_list.append(search_list_sorted[0][0])

# first search
for s1 in search_list_sorted:
    pos1 = source_pos[s1[0]]
    add = True
    for s2 in first_takeoff_list:
        if s1 != s2:
            pos2 = source_pos[s2[0]]
            dis = (pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2 + (pos1[2] - pos2[2]) ** 2
            dis = dis ** 0.5
            if dis < takeoff_safe_radius:
                add = False
    if add == True:
        first_takeoff_list.append(s1)
        
first_takeoff_list= list(set(first_takeoff_list))
#print 'first takeoff:',first_takeoff_list

# set first take off time
for s in first_takeoff_list:
    takeoff_table[s] = 1

print '第一次起飞数量：',len(first_takeoff_list)
 
# cut other no use frames
cmds.cutKey(spheres,time = (2, 50000), clear = True)

obj_num = takeoff_num
update_obj_list = []

# create a sports quality
obj_list = []
cmds.currentTime(1)
for i in range(1,obj_num+1,1):
    #print i 
    #print update_obj_list
    sq = Sports_quality('dmd'+ str(i),source_pos['dmd'+ str(i)], dest_pos['dmd'+ str(i)])
    obj_list.append(sq)

for s in first_takeoff_list:
    for i in range(len(obj_list)):
        if obj_list[i].obj == s:
            update_obj_list.append(obj_list[i])
            obj_list[i].state = 1
            
wait_obj_list = [item for item in obj_list if item not in set(update_obj_list)]
'''
for u in update_obj_list:
    print u.obj

for u in obj_list:
    print u.obj


for i in range(1,obj_num+1,1):
    #print i 
    #print update_obj_list
    sq = Sports_quality('dmd'+ str(i),cmds.objectCenter('dmd'+ str(i),gl = True),cmds.objectCenter('target'+ str(i),gl = True))
    update_obj_list.append(sq)
'''

# update at 0.5 sec
update_time = 0.1
cur_frame = 1
dis_threshold = 0.005

all_arrived = 0

# set param
max_a = 5.0
max_v_xy = 5.0
max_v_z = 2.8

# Attractive force
Attr_force = 5.0

# repulsive force
Repu_force = 2.0

slow_down_dis = 3.0
safe_radius = 8.0
view_radius = 15.0

# acc and speed constraint
acc_hor_max = 5.0
acc_ver_max = 3.0

speed_hor_max = 5.0
speed_ver_max = 2.8

# deflection k
deflection_k = 1.0

# overtime limit
overtime = 8000.0

# show the result of maya, if not show will reduce about 30% time
maya_show = True