cur_frame += update_time * 24
    
# update the wait obj list
wait_obj_list = [item for item in obj_list if item not in set(update_obj_list)]
if len(wait_obj_list) >0:
    #print wait_obj_list
    # make a sorted with dis
    # get the search list sorted    
    # get the graph center
    center = [0.0,0.0,0.0]
    for s in wait_obj_list:
        center[0] += s.pos[0]
        center[1] += s.pos[1]
        center[2] += s.pos[2]
        
    center[0] /= len(wait_obj_list)
    center[1] /= len(wait_obj_list)
    center[2] /= len(wait_obj_list)
    
    #print center
    search_list = {}
    for s in wait_obj_list:
        dis = (s.pos[0] - center[0]) ** 2 + (s.pos[1] - center[1]) ** 2 + (s.pos[2] - center[2]) ** 2
        dis = dis ** 0.5
        search_list[s.obj] = dis
        
    search_list_sorted = sorted(search_list.items(),key = lambda x:x[1],reverse = True)
    #print search_list_sorted
        
    new_wait_obj_list = []
        
    for s in search_list_sorted:
        for u in wait_obj_list:
            if s[0] == u.obj:
                new_wait_obj_list.append(u)
                break
    
for s in new_wait_obj_list:
    pos1 = s.pos
    collision_c = False
    if len(update_obj_list)==167:
        break
    for u in update_obj_list:
        pos2 = u.pos
        dis = (pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2 + (pos1[2] - pos2[2]) ** 2
        dis = dis ** 0.5
        if dis < 5.0:
            collision_c = True
    if collision_c == False:
        print "add",s.obj
        update_obj_list.append(s)
        print len(update_obj_list)
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
        
    # calculate the friction force
    # set the 8 as the slowdown dis
    # Ff = [0.0,0.0,0.0]
    Fd = [0.0,0.0,0.0]
        
    Fd[0] = -sq.speed[0] * (max_a/max_v)
    Fd[1] = -sq.speed[1] * (max_a/max_v)
    Fd[2] = -sq.speed[2] * (max_a/max_v)
    #print 'Fd',Fd
               
    # calculate the attractive force
    Fa = [0.0,0.0,0.0]
    Fa[0] = Attr_force * sq.mass * (sq.target[0] - sq.pos[0]) / dis
    Fa[1] = Attr_force * sq.mass * (sq.target[1] - sq.pos[1]) / dis 
    Fa[2] = Attr_force * sq.mass * (sq.target[2] - sq.pos[2]) / dis
            
    if dis < slow_down_dis:
        Fa[0] *= dis / slow_down_dis
        Fa[1] *= dis / slow_down_dis
        Fa[2] *= dis / slow_down_dis
                
    #print 'Fa',Fa
    Fr = [0.0,0.0,0.0]
        
    # calculate the repulsive force
        
    for sq2 in update_obj_list:
        if sq2 != sq:
            if sq2.updated:
                pos = sq2.pre_pos
            else:
                pos = sq2.pos
                        
            b_dis = ((pos[0] - sq.pos[0])**2 + (pos[1] - sq.pos[1])**2 + (pos[2] - sq.pos[2])**2)**0.5
            #print 'b_dis',b_dis
            if b_dis < view_radius:
                sv = [0.0,0.0,0.0]
                sv[0] = sq.speed[0] - sq2.speed[0]
                sv[1] = sq.speed[1] - sq2.speed[1]
                sv[2] = sq.speed[2] - sq2.speed[2]
                        
                pv = [0.0,0.0,0.0]
                pv[0] = sq2.pos[0] - sq.pos[0] 
                pv[1] = sq2.pos[1] - sq.pos[1] 
                pv[2] = sq2.pos[2] - sq.pos[2] 
                        
                d = sv[0] * pv[0] + sv[1] * pv[1] + sv[2] * pv[2]
                n1 = (sv[0]**2 + sv[1]**2 + sv[2]**2)**0.5
                n2 = (pv[0]**2 + pv[1]**2 + pv[2]**2)**0.5
                        
                #print 's p ',sv,pv
                        
                # same speed direction and value
                if math.fabs(n1 - 0.0) < 0.01:
                    # just jump left it to next state
                    #print 'dif angle'
                    theta = 3*math.pi
                    pass
                else:
                    #print ''
                    # theta is the angle of speed 
                    theta = math.acos(max(min(d/n1/n2,1.0),-1.0))
                    #print(d/n1/n2)
                    #print d,n1,n2,n1*n2
                # calculate the collision angle
                safe_angle = math.asin(max(min(safe_radius/b_dis,1.0),-1.0))
        
                if (theta < 2*math.pi) and (math.fabs(theta) < safe_angle):# or (math.pi - theta) < safe_angle):
                    #print 'collision'
                    #print 'angle',theta,safe_angle
                    #print theta/3.14*180
                    #print safe_angle/3.14*180
                    #break
                    #print 'angle',theta,safe_angle
                            
                    # calculate the deflection force
                            
                    t = safe_angle - theta #(safe_angle-(math.pi - theta)) if theta > safe_angle else (safe_angle - theta)
                    defl = math.tan(t) * (sv[0]**2+sv[1]**2+sv[2]**2)**0.5 * deflection_k
                            
                    #if theta < math.pi/2:
                    #    defl *= -1.0
    
                    Fdef =[0.0,0.0,0.0]
                    # (-sv[2]-sv[1]/sv[0],1.0,1.0)
                    Fdef[0] = random.random() * deflection_k#defl * (-sv[2]-sv[1])/sv[0] / ((((-sv[2]-sv[1])/sv[0])**2 + 2.0)**0.5)
                    Fdef[1] = random.random() * deflection_k#defl * 1.0 / ((((-sv[2]-sv[1])/sv[0])**2 + 2.0)**0.5)
                    Fdef[2] = random.random() * deflection_k#defl * 1.0 / ((((-sv[2]-sv[1])/sv[0])**2 + 2.0)**0.5)

                    '''
                    if sv[0]<0:
                        Fdef[0] *= -1.0
                                
                    if sv[1]<0:
                        Fdef[1] *= -1.0
                                
                    if sv[2]<0:
                        Fdef[2] *= -1.0
                    '''
                    #print 'Fdef',Fdef
                    #print defl
                    if sq2.arrived == False:    
                        Fr[0] += Fdef[0]
                        Fr[1] += Fdef[1]
                        Fr[2] += Fdef[2]
                        
                        Fr[0] +=  -math.fabs(Repu_force) * sq.mass * (pos[0] - sq.pos[0]) / b_dis / b_dis#math.fabs(b_dis-safe_radius)
                        Fr[1] +=  -math.fabs(Repu_force) * sq.mass * (pos[1] - sq.pos[1]) / b_dis / b_dis#math.fabs(b_dis-safe_radius)
                        Fr[2] +=  -math.fabs(Repu_force) * sq.mass * (pos[2] - sq.pos[2]) / b_dis / b_dis#math.fabs(b_dis-safe_radius)

    #print 'Fr',Fr
            
    if dis < slow_down_dis:
        #Fd = [0.0,0.0,0.0]
        Fr = [0.0,0.0,0.0]
    # calculate all force
    
    Fx = Fa[0] + Fd[0] + Fr[0]
    Fy = Fa[1] + Fd[1] + Fr[1]
    Fz = Fa[2] + Fd[2] + Fr[2]
    
    #print 'F',Fx,Fy,Fz   
    
    # make it rigid body
    Frb = [0.0,0.0,0.0]
    for sq2 in update_obj_list:
        if sq2 != sq:
            rb_dis = ((sq2.pos[0] - sq.pos[0])**2 + (sq2.pos[1] - sq.pos[1])**2 + (sq2.pos[2] - sq.pos[2])**2)**0.5
            #print 'rb',rb_dis
            if rb_dis < safe_radius:
                pv = [0.0,0.0,0.0]
                pv[0] = sq2.pos[0] - sq.pos[0] 
                pv[1] = sq2.pos[1] - sq.pos[1] 
                pv[2] = sq2.pos[2] - sq.pos[2] 
    
                d = (sq.speed[0] * pv[0] + sq.speed[1] * pv[1] + sq.speed[2] * pv[2])
                n1 = (sq.speed[0]**2 + sq.speed[1]**2 + sq.speed[2]**2)**0.5
                n2 = (pv[0]**2 + pv[1]**2 + pv[2]**2)**0.5
                l = d / n2 
                if l < 0:
                    l = 0
                    
                #print 'l',l,pv
                # make a brake
                sq.speed[0] = sq.speed[0] - l * pv[0]/n2
                sq.speed[1] = sq.speed[1] - l * pv[1]/n2
                sq.speed[2] = sq.speed[2] - l * pv[2]/n2
    
                d = (Fx* pv[0] + Fy * pv[1] + Fz * pv[2])
                n1 = (Fx**2 + Fy**2 + Fz**2)**0.5
                l = d / n2 
                if l < 0:
                    l = 0
                    
                #print 'l2',l
                # counter force
                Fx = Fx - l * pv[0]/n2
                Fy = Fy - l * pv[1]/n2
                Fz = Fz - l * pv[2]/n2
                    
    #print 'Final',Fx,Fy,Fz  
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
    if acc[2] > acc_ver_max:
        acc_scale = min(acc_scale,acc_ver_max / math.fabs(acc[2]))
                    
    sq.acc[0] = (Fx / sq.mass) * acc_scale #max(min(Fx / sq.mass,5.0),-5.0)
    sq.acc[1] = (Fy / sq.mass) * acc_scale #max(min(Fy / sq.mass,5.0),-5.0)
    sq.acc[2] = (Fz / sq.mass) * acc_scale #max(min(Fz / sq.mass,5.0),-5.0)
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
                        
    #speed = min((new_speed[0]**2 + new_speed[1]**2 + new_speed[2]**2) ** 0.5,2.4)
    speed_ver = new_speed[2] * speed_scale
                
    #acc = (sq.acc[0]**2 + sq.acc[1]**2 + sq.acc[2]**2 )**0.5
    sq.speed[0] = new_speed[0] * speed_scale
    sq.speed[1] = new_speed[1] * speed_scale
    sq.speed[2] = new_speed[2] * speed_scale
               
    #print 'speed',sq.speed
                
    # calculate new pos
    sq.pre_pos[0] = sq.pos[0]
    sq.pre_pos[1] = sq.pos[1]
    sq.pre_pos[2] = sq.pos[2]
                
    sq.updated = True
    sq.pos[0] = sq.pos[0] + sq.speed[0] * update_time
    sq.pos[1] = sq.pos[1] + sq.speed[1] * update_time
    sq.pos[2] = sq.pos[2] + sq.speed[2] * update_time
    #print 'pos',sq.pos
                
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
    cmds.setKeyframe(sq.obj)
                    
    #print ''
    sq.pos_list.append(tuple(sq.pos))
    sq.knote += 1
    sq.k.append(sq.knote)
    # check end
    dis = ((sq.pos[2] - sq.target[2]) ** 2 + (sq.pos[1] - sq.target[1]) ** 2 + (sq.pos[0] - sq.target[0]) ** 2) **0.5   
    if dis < sq.max_dis * dis_threshold:
        print sq.obj
        print 'arrived-------------------------------------------------------------------------------------------------'
        cmds.curve(degree = 1, point = sq.pos_list,knot = sq.k)
        sq.arrived = True
        all_arrived +=1
                
        #print dis,sq.max_dis,dis_threshold
        print ''
        #break    
                
