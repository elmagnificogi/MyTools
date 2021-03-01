# clear the windows
Dmd_UAVC_exfunc_clear_output_windows()

# get the operation object
spheres = cmds.ls("dmd*", transforms = True)

# divide group manually
g1 = cmds.ls("dmd*",selection = True, transforms = True)
g2 = cmds.ls("dmd*",selection = True, transforms = True)

all_group = []
all_group.append(g1)
all_group.append(g2)

takeoff_safe_radius = 5.0
takeoff_height = 10.0
onetimetakeoff_maxnum = 15
takeoff_speed_ver = 2.0
takeoff_speed_hor = 4.0
time_interval = 3.0
takeoff_num = len(spheres)
target_time = 3400

search_list = {}
source_pos = {}
dest_pos = {}

cmds.currentTime(1,update = True)
for s in spheres:
    source_pos[s] = cmds.objectCenter(s,gl = True)
    
cmds.currentTime(target_time,update = True)
for s in spheres:
    dest_pos[s] = cmds.objectCenter(s,gl = True)
    
# first get the dis of source to dest
for s in spheres:
    pos = source_pos[s]
    pos1 = dest_pos[s]
    dis = (pos[0] - pos1[0]) ** 2 + (pos[1] - pos1[1]) ** 2 + (pos[2] - pos1[2]) ** 2
    dis = dis ** 0.5
    search_list[s] = dis

all_dis_sorted = dict(sorted(search_list.items(),key = lambda x:x[1],reverse = True))
# print search_list_sorted
takeoff_table = {}
takeoff_groups = []
curtime = 0
# first search
search_list_sorted = {}
cmds.currentTime(1,update = True)
for g in all_group:
    for s in g:
        search_list_sorted[s] = all_dis_sorted[s]

    while len(search_list_sorted)>0 :
        takeoff_group = []
        add_num = 0
        for s1 in search_list_sorted:
            if add_num == onetimetakeoff_maxnum:
                break;
            #print search_list_sorted
            #print s1
            pos1 = cmds.objectCenter(s1,gl = True)
            add = True
            for s2 in takeoff_group:
                #print takeoff_group
                pos2 = cmds.objectCenter(s2,gl = True)
                dis = (pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2 + (pos1[2] - pos2[2]) ** 2
                dis = dis ** 0.5
                if dis < takeoff_safe_radius:
                    add = False
            if add:
                takeoff_group.append(s1)
                add_num+=1
        for t in takeoff_group:
            #print takeoff_group
            #print t
            #print search_list_sorted['dmd100']
            search_list_sorted.pop(t)
            takeoff_table[t] = curtime * 24 +1
        takeoff_groups.append(takeoff_group)
        curtime +=time_interval   
 
# print takeoff_table
# print takeoff_groups
# print len(takeoff_groups)

#i = 0
#cmds.select(takeoff_groups[i])
#i+=1

for t in takeoff_table:
    #print t
    cmds.currentTime(takeoff_table[t]+1+takeoff_height/takeoff_speed_ver*24,update = False)
    #print (takeoff_table[t]+1)*24
    #print (takeoff_table[t]+2))*24
    cmds.move(source_pos[t][0],source_pos[t][1],source_pos[t][2]+takeoff_height,t, worldSpace = True)
    cmds.setKeyframe(t)
    cmds.copyKey(t, time=(1,1))
    cmds.pasteKey(t, time=((takeoff_table[t]+1),(takeoff_table[t]+2)),option = "replace")

for s in spheres:
    x=dest_pos[s][0] - source_pos[s][0]
    y=dest_pos[s][1] - source_pos[s][1]
    z=dest_pos[s][2] - source_pos[s][2] - takeoff_height
    maxtime = max(math.fabs(z / takeoff_speed_ver),math.sqrt(x**2+y**2)/takeoff_speed_hor)*24.0+1.0 + takeoff_height/takeoff_speed_ver*24
    cmds.copyKey(s, time=(3400,3400))
    cmds.pasteKey(s, time=(int(takeoff_table[s]+1+maxtime),int(takeoff_table[s]+2+maxtime)),option = "replace")
    
    
for s in spheres:
    cmds.curve(degree = 1, point = [source_pos[s],(source_pos[s][0],source_pos[s][1],source_pos[s][2]+takeoff_height),dest_pos[s]],knot = [1,2,3])
#print source_pos[s],dest_pos[s]
#print takeoff_table['dmd11'],takeoff_table['dmd13']

cmds.keyTangent(spheres, edit=True, time=(1,target_time), inTangentType = 'linear', outTangentType = 'linear')

Dmd_UAVC_td_check_overspeed_collision()

curpath = cmds.workspace(q=True, directory=True)

t1 = []

for t in takeoff_table:
    t1.append((t,(takeoff_table[t]-1)/24))

print data
data = t1
print curpath
with open(curpath+'takeoff_table.csv', 'w') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)