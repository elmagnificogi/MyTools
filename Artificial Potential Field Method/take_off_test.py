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

        # update the speed 
        cmds.setAttr(sq.obj + '.speed',0)
        cmds.setAttr(sq.obj + '.speed_x',0)        
        cmds.setAttr(sq.obj + '.speed_y',0)        
        cmds.setAttr(sq.obj + '.speed_z',0)        
        cmds.setAttr(sq.obj + '.speed_xy',0)

        cmds.setKeyframe(sq.obj + '.speed')
        cmds.setKeyframe(sq.obj + '.speed_x')
        cmds.setKeyframe(sq.obj + '.speed_y')
        cmds.setKeyframe(sq.obj + '.speed_z')
        cmds.setKeyframe(sq.obj + '.speed_xy')

# clear the windows
Dmd_UAVC_exfunc_clear_output_windows()

# get the operation object
Dmd_UAVC_reset_radius()

spheres = cmds.ls("dmd*",selection = True, transforms = True)

start_time   = cmds.floatField("Dmd_UAVC_Motion_start_time", query = True, value = True)
end_time     = cmds.floatField("Dmd_UAVC_Motion_end_time", query = True, value = True)

# first get the dis of source to dest
search_list = {}
source_pos = {}
dest_pos = {}

cmds.currentTime(start_time,update = True)
for s in spheres:
    source_pos[s] = cmds.objectCenter(s,gl = True)

cmds.currentTime(end_time,update = True)
for s in spheres:
    dest_pos[s] = cmds.objectCenter(s,gl = True)

update_obj_list = []

# create a sports quality
obj_list = []
cmds.currentTime(start_time)
for i in range(0,len(spheres),1):
    sq = Sports_quality('dmd'+ str(i+1),source_pos['dmd'+ str(i+1)], dest_pos['dmd'+ str(i+1)])
    obj_list.append(sq)

for i in range(len(obj_list)):
    update_obj_list.append(obj_list[i])
    #obj_list[i].state = 1


# PARAM for APF

# update at 0.5 sec
update_time = 0.01 # /s
cur_frame = start_time

# overtime limit
overtime = end_time

# end threshold
dis_threshold = 0.005
all_arrived = 0

# speed and acc limit
max_a = 5.0
max_v_xy = 5.0
max_v_z = 2.8

# Attractive force
Attr_force = 5.0

# repulsive force
Repu_force = 2.0

slow_down_dis = 3.0
safe_radius = 8
view_radius = 15.0

# acc and speed constraint
acc_hor_max = 5.0
acc_ver_max = 3.0

speed_hor_max = 5.0
speed_ver_max = 2.8

# deflection k
deflection_k = 2.0

#Dynamic friction
dy_friction = 2.5

# show the result of maya, if not show will reduce about 30% time
maya_show = True

# main code
cmds.progressWindow(isInterruptable=1)
begin = datetime.datetime.now()
while True :
    # a progress bar
    if cmds.progressWindow(query=1, isCancelled=1) :
        break
        
    cur_frame += update_time * 24
    if cur_frame > overtime:
        print("overtime,stop mp")
        break
    
    for sq in update_obj_list:
        sq.updated = False
            
    # update
    for sq in update_obj_list:
        if sq.arrived:
            continue

        #print sq.obj
        # calculate some var first
        dis2 = (sq.target[0] - sq.pos[0])**2 + (sq.target[1] - sq.pos[1])**2 + (sq.target[2] - sq.pos[2])**2
        dis = dis2 ** 0.5
        
        # check end
        if dis < sq.max_dis * dis_threshold:
            #print sq.obj
            #print 'arrived-----------------------------'
            #cmds.curve(degree = 1, point = sq.pos_list,knot = sq.k)
            sq.arrived = True
            all_arrived +=1
            sq.mass = 0.7
            if maya_show:
                cmds.progressWindow(edit=True, progress = int((all_arrived+len(update_obj_list))* 50.0 / len(spheres)))   

        # calculate the friction force
        # set the 8 as the slowdown dis
        Fd = [0.0,0.0,0.0]
        
        s_m = sq.speed[0]**2 + sq.speed[1]**2 + sq.speed[2]**2
        s_m = s_m ** 0.5
        if math.fabs(s_m) > 0.001:
            Fd[0] = -dy_friction * sq.speed[0] / s_m # -sq.speed[0] #* (max_a/max_v_xy)
            Fd[1] = -dy_friction * sq.speed[1] / s_m # -sq.speed[1] #* (max_a/max_v_xy)
            Fd[2] = -dy_friction * sq.speed[2] / s_m # -sq.speed[2] #* (max_a/max_v_z)
        else:
            Fd[0] = 0
            Fd[1] = 0
            Fd[2] = 0

        # calculate the attractive force
        Fa = [0.0,0.0,0.0]
        Fa[0] = Attr_force * sq.mass * (sq.target[0] - sq.pos[0]) / dis
        Fa[1] = Attr_force * sq.mass * (sq.target[1] - sq.pos[1]) / dis
        Fa[2] = Attr_force * sq.mass * (sq.target[2] - sq.pos[2]) / dis
            
        if dis < slow_down_dis:
            Fa[0] *= dis / slow_down_dis
            Fa[1] *= dis / slow_down_dis
            Fa[2] *= dis / slow_down_dis

#-------------------------------------------------------------
        collision_list = []
        Fr = [0.0,0.0,0.0]
        # calculate the repulsive force
        for sq2 in update_obj_list:
            if sq2 != sq:
                if sq2.updated:
                    pos = sq2.pre_pos
                else:
                    pos = sq2.pos
                        
                b_dis = ((pos[0] - sq.pos[0])**2 + (pos[1] - sq.pos[1])**2 + (pos[2] - sq.pos[2])**2)**0.5

                if b_dis < view_radius and b_dis >=slow_down_dis:
                    if b_dis < safe_radius:
                        collision_list.append(sq2)

                    sv = [0.0,0.0,0.0]
                    sv[0] = sq.speed[0] - sq2.speed[0]
                    sv[1] = sq.speed[1] - sq2.speed[1]
                    sv[2] = sq.speed[2] - sq2.speed[2]
                        
                    pv = [0.0,0.0,0.0]
                    pv[0] = pos[0] - sq.pos[0] 
                    pv[1] = pos[1] - sq.pos[1] 
                    pv[2] = pos[2] - sq.pos[2] 
                        
                    d = sv[0] * pv[0] + sv[1] * pv[1] + sv[2] * pv[2]
                    n1 = (sv[0]**2 + sv[1]**2 + sv[2]**2)**0.5
                    n2 = (pv[0]**2 + pv[1]**2 + pv[2]**2)**0.5
                        
                    #print 's p ',sv,pv
                        
                    # same speed direction and value
                    if math.fabs(n1 - 0.0) < 0.01:
                        # just jump ,let it to next state
                        theta = 3*math.pi
                        pass
                    else:
                        # theta is the angle of speed 
                        theta = math.acos(max(min(d/n1/n2,1.0),-1.0))
        
                    if(theta < 2*math.pi) and (math.fabs(theta) <math.pi/2): #safe_angle):# or (math.pi - theta) < safe_angle):   

                        dv = [0.0,0.0,0.0]
                        dv2 = 1.0
                        if sq2.obj in sq.dv_direction:
                            dv2 = sq.dv_direction[sq2.obj]
                        else:
                            dv2 = sq.dv_direction[sq2.obj] = 1.0
                            sq2.dv_direction[sq.obj] = -1.0
                        
                        if math.fabs(sv[0]*pv[2]-pv[0]*sv[2]) <= 0.000001:
                            dv1 = (pv[1]*sv[2] - sv[1]*pv[2]) / 1.0 * dv2
                        else:
                            dv1 = (pv[1]*sv[2] - sv[1]*pv[2]) / (sv[0]*pv[2]-pv[0]*sv[2]) * dv2
                        dv3 = sv[1]*pv[0] - sv[0]*pv[1] * dv2

                        d = dv1**2 + dv2**2 + dv3**2
                        d = d**0.5

                        Fdef =[0.0,0.0,0.0]
                        r = random.random() * deflection_k
                        Fdef[0] = r * dv1 / d
                        Fdef[1] = r * dv2 / d
                        Fdef[2] = r * dv3 / d

                        Fr[0] += Fdef[0]
                        Fr[1] += Fdef[1]
                        Fr[2] += Fdef[2]
                        Fr[0] +=  -math.fabs(Repu_force) * (pos[0] - sq.pos[0]) / b_dis / b_dis
                        Fr[1] +=  -math.fabs(Repu_force) * (pos[1] - sq.pos[1]) / b_dis / b_dis
                        Fr[2] +=  -math.fabs(Repu_force) * (pos[2] - sq.pos[2]) / b_dis / b_dis

        # calculate all force    
        Fx = Fa[0] + Fd[0] + Fr[0] #+ sq.transfer_force[0]
        Fy = Fa[1] + Fd[1] + Fr[1] #+ sq.transfer_force[1]
        Fz = Fa[2] + Fd[2] + Fr[2] #+ sq.transfer_force[2]
        #print 'F',Fx,Fy,Fz 

        sq.transfer_force = [0.0,0.0,0.0]

#-------------------------------------------------------------
        # make it rigid body
        for sq2 in collision_list:
            pv = [0.0,0.0,0.0]
            pv[0] = sq2.pos[0] - sq.pos[0] 
            pv[1] = sq2.pos[1] - sq.pos[1] 
            pv[2] = sq2.pos[2] - sq.pos[2] 
    
            d = (sq.speed[0] * pv[0] + sq.speed[1] * pv[1] + sq.speed[2] * pv[2])
            n2 = (pv[0]**2 + pv[1]**2 + pv[2]**2)**0.5
            l = d / n2 
            if l < 0:
                l = 0

            # Conservation of momentum,the sq2 get half speed
            sq2.speed[0] += min(l * pv[0]/n2,speed_hor_max) * 0.5
            sq2.speed[1] += min(l * pv[1]/n2,speed_hor_max) * 0.5
            sq2.speed[2] += min(l * pv[2]/n2,speed_ver_max) * 0.5

            #print 'l',l,pv
            # make a brake
            sq.speed[0] = sq.speed[0] - l * pv[0]/n2 #* 0.5
            sq.speed[1] = sq.speed[1] - l * pv[1]/n2 #* 0.5
            sq.speed[2] = sq.speed[2] - l * pv[2]/n2 #* 0.5
    
            d = (Fx* pv[0] + Fy * pv[1] + Fz * pv[2])
            l = d / n2 
            if l < 0:
                l = 0
                    
            t = [l * pv[0]/n2,l * pv[1]/n2,l * pv[2]/n2]

            if sq2.arrived:
                all_arrived -= 1
                sq2.arrived = False
                     
            if sq2.mass < 0.99:
                sq2.transfer_force[0] += t[0]
                sq2.transfer_force[1] += t[1]
                sq2.transfer_force[2] += t[2]
          
            # counter force
            Fx = Fx - t[0]
            Fy = Fy - t[1]
            Fz = Fz - t[2]

#-------------------------------------------------------------
        # calculate the acc 
        acc = [0.0,0.0,0.0]
        acc_scale = 1.0
        acc[0] = math.fabs(Fx / sq.mass)
        acc[1] = math.fabs(Fy / sq.mass)
        acc[2] = math.fabs(Fz / sq.mass)
                
        # Acceleration constraint
        acc_hor = (acc[0]**2 + acc[1]**2) ** 0.5
        if acc_hor > acc_hor_max:
            acc_scale = min(acc_scale,acc_hor_max / acc_hor)
        if math.fabs(acc[2]) > acc_ver_max:
            acc_scale = min(acc_scale,acc_ver_max / math.fabs(acc[2]))
                    
        sq.acc[0] = (Fx / sq.mass) * acc_scale 
        sq.acc[1] = (Fy / sq.mass) * acc_scale
        sq.acc[2] = (Fz / sq.mass) * acc_scale 
        #print 'acc',sq.acc,acc_scale
                
        # calculate new speed 
                
        new_speed = [0.0,0.0,0.0]
        speed_scale = 1.0
        new_speed[0] = sq.speed[0] + sq.acc[0] * update_time
        new_speed[1] = sq.speed[1] + sq.acc[1] * update_time
        new_speed[2] = sq.speed[2] + sq.acc[2] * update_time
                
        # speed constraint
        speed_hor = (new_speed[0]**2 + new_speed[1]**2) ** 0.5
        if speed_hor > speed_hor_max:
            speed_scale = min(speed_scale,speed_hor_max / speed_hor)
        if math.fabs(new_speed[2]) > speed_ver_max:
            speed_scale = min(speed_scale,speed_ver_max / math.fabs(new_speed[2]))
                        
        speed_ver = new_speed[2] * speed_scale
                
        sq.speed[0] = new_speed[0] * speed_scale
        sq.speed[1] = new_speed[1] * speed_scale
        sq.speed[2] = new_speed[2] * speed_scale
        
        speed_hor = (sq.speed[0]**2 + sq.speed[1]**2) ** 0.5
        #print 'speed',sq.speed
                
        # calculate new pos
        sq.pre_pos[0] = sq.pos[0]
        sq.pre_pos[1] = sq.pos[1]
        sq.pre_pos[2] = sq.pos[2]

        sq.pos[0] = sq.pos[0] + sq.speed[0] * update_time
        sq.pos[1] = sq.pos[1] + sq.speed[1] * update_time
        sq.pos[2] = sq.pos[2] + sq.speed[2] * update_time
        sq.updated = True

#-------------------------------------------------------------
        if maya_show:
            # update the pos
            cmds.currentTime(cur_frame,update = False)
            cmds.move(sq.pos[0], sq.pos[1], sq.pos[2],sq.obj, worldSpace = True)
                        
            speed = (sq.speed[0]**2 + sq.speed[1]**2 + sq.speed[2]**2)**0.5
            # update the speed 
            cmds.setAttr(sq.obj + '.speed',speed)
            cmds.setAttr(sq.obj + '.speed_x',sq.speed[0])        
            cmds.setAttr(sq.obj + '.speed_y',sq.speed[1])        
            cmds.setAttr(sq.obj + '.speed_z',sq.speed[2])        
            cmds.setAttr(sq.obj + '.speed_xy',speed_hor)

            cmds.setKeyframe(sq.obj + '.translate')
            cmds.setKeyframe(sq.obj + '.speed')
            cmds.setKeyframe(sq.obj + '.speed_x')
            cmds.setKeyframe(sq.obj + '.speed_y')
            cmds.setKeyframe(sq.obj + '.speed_z')
            cmds.setKeyframe(sq.obj + '.speed_xy')

    if all_arrived == len(update_obj_list):
        print 'Final time:',cur_frame
        break

cmds.progressWindow(endProgress=1)
end = datetime.datetime.now()
if cur_frame <= overtime:
    if maya_show:
        cmds.floatField("Dmd_UAVC_Motion_start_time", edit=True,value =1)
        cmds.floatField("Dmd_UAVC_Motion_end_time", edit=True,value =cur_frame+1)
        #Dmd_UAVC_td_check_overspeed_collision()
else:
    print "over time:",overtime
print '总共耗时',end-begin