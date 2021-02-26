


maya自身的transform节点

maya自身位置的计算

maya自身的位置矩阵是由多部分构成的，这样的好处是为了做动画的时候，可以通过各种参数控制来调整动画。
所以有必要理解多部分的位置矩阵是如何计算出来最终的位置的。

矩阵后乘---也就是矩阵右乘

比如把P从对象空间转化到世界空间时，是 p' = p * wm


               -1                      -1
    matrix = SP * S * SH * SP * ST * RP * RA * R * RP * RT * T
    
    \* 矩阵乘法
    -1 矩阵转置
    
    SP = |  1    0    0    0 |     ST = |  1    0    0    0 |
         |  0    1    0    0 |          |  0    1    0    0 |
         |  0    0    1    0 |          |  0    0    1    0 |
         | spx  spy  spz   1 |          | sptx spty sptz  1 |


    S  = |  sx   0    0    0 |     SH = |  1    0    0    0 |
         |  0    sy   0    0 |          | shxy  1    0    0 |
         |  0    0    sz   0 |          | shxz shyz  1    0 |
         |  0    0    0    1 |          |  0    0    0    1 |



    RP = |  1    0    0    0 |     RT = |  1    0    0    0 |
         |  0    1    0    0 |          |  0    1    0    0 |
         |  0    0    1    0 |          |  0    0    1    0 |
         | rpx  rpy  rpz   1 |          | rptx rpty rptz  1 |
    
    RA = AX * AY * AZ



     AX = |  1    0    0    0 |     AY = |  cy   0   -sy   0 |
          |  0    cx   sx   0 |          |  0    1    0    0 |
          |  0   -sx   cx   0 |          |  sy   0    cy   0 |
          |  0    0    0    1 |          |  0    0    0    1 |



     AZ = |  cz   sz   0    0 |     sx = sin(rax), cx = cos(rax)
          | -sz   cz   0    0 |     sy = sin(ray), cx = cos(ray)
          |  0    0    1    0 |     sz = sin(raz), cz = cos(raz)
          |  0    0    0    1 |


    旋转:
        如果用 rotationInterpolation 属性指定四元数，那么需要使用下面的OpenMaya API来构造矩阵
    
            Mquaternion q( rx, ry, rz, rw )
            R  = q.asMatrix()
    
        否则使用欧拉角来计算旋转矩阵
    
            R  = RX * RY * RZ  (Note: order is determined by rotateOrder)
    
            RX = |  1    0    0    0 |     RY = |  cy   0   -sy   0 |
                 |  0    cx   sx   0 |          |  0    1    0    0 |
                 |  0   -sx   cx   0 |          |  sy   0    cy   0 |
                 |  0    0    0    1 |          |  0    0    0    1 |
    
            RZ = |  cz   sz   0    0 |     sx = sin(rx), cx = cos(rx)
                 | -sz   cz   0    0 |     sy = sin(ry), cx = cos(ry)
                 |  0    0    1    0 |     sz = sin(rz), cz = cos(rz)
                 |  0    0    0    1 |
    
    T  = |  1    0    0    0 |
         |  0    1    0    0 |
         |  0    0    1    0 |
         |  tx   ty   tz   1 |























现有的无人机组网技术依赖于传统的由移动节点组成的自组网(ad hoc)， 其包括移动自组网(Mobile Ad Hoc Network，MANET)和车载网(vehicular ad hoc network，VANET)，为无人机集群分布式通信提供了理论和技术依据。MANET 和VANET网络为无人机集群提供分布式组网协议和数据通信架构(包括网络接 入机制，信道访问机制，路由协议等)，使得数据包在无人机之间分发

述无人机与集群云控制器之间传输位置信息、飞行状态数据、 飞行控制数据、WIFI数据链路的状态和路由信息时所使用的协议为Openflow 协议。


```
使用logging来记录log

import logging

# Logging setup
LOG_FILEPATH = '/path/to/log_file.log'
logger = logging.getLogger('My logger')
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

# Logging to file
file_handler = logging.FileHandler( LOG_FILEPATH )
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.INFO)
logger.addHandler(file_handler)

# Logging to stdout
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setFormatter(formatter)
stdout_handler.setLevel(logging.INFO)
logger.addHandler(stdout_handler)

# Usage
logger.info('Hello')       # Log infos
logger.warning('Oops')     # Log warnings
logger.error('Dang!')      # Log errors
```


```
Maya 内建UI的结构

#main window
'MayaWindow'

#menu (model state)
'mainFileMenu',
'mainEditMenu',
'mainCreateMenu',
'mainSelectMenu',
'mainModifyMenu',
'mainDisplayMenu',
'mainWindowMenu',
'mainMeshMenu',
'mainEditMeshMenu',
'mainMeshToolsMenu',
'mainMeshDisplayMenu',
'mainCurvesMenu',
'mainSurfacesMenu',
'mainDeformMenu',
'mainUVMenu',
'mainGenerateMenu',
'HotBoxRecentCommandsMenu',
'HotBoxControlsMenu',
'mainKeysMenu',
'mainPlaybackMenu',
'mainVisualizeMenu',
'mainDeformationMenu',
'mainConstraintsMenu',
'mainParticlesMenu',
'mainFluidsMenu',
'mainNClothMenu',
'mainHairMenu',
'mainNConstraintMenu',
'mainNCacheMenu',
'mainFieldsSolverMenu',
'mainDynEffectsMenu',
'mainShadingMenu',
'mainRenTexturingMenu',
'mainRenderMenu',
'mainCartoonMenu',
'mainStereoMenu',
'mainRigSkeletonsMenu',
'mainRigSkinningMenu',
'mainRigDeformationsMenu',
'mainRigConstraintsMenu',
'mainRigControlMenu',
'mainPipelineCacheMenu',
'HotboxNorth1',
'HotboxNorth2',
'HotboxNorth3',
'HotboxSouth1',
'HotboxSouth2',
'HotboxSouth3',
'HotboxEast1',
'HotboxEast2',
'HotboxEast3',
'HotboxWest1',
'HotboxWest2',
'HotboxWest3',
'HotboxCenter1',
'HotboxCenter2',
'HotboxCenter3',
'ArnoldMenu',
'mainBifrostMenu',
'mainBossMenu',
'mainMashMenu',
'MainHelpMenu'

# 右上角图标
type('iconTextCheckBox')
'StatusLine|MainStatusLineLayout|formLayout4|formLayout7|modelingToolkitButton'
'StatusLine|MainStatusLineLayout|formLayout4|formLayout7|channelLayerBoxButton'

# Shelf位置
'Shelf|MainShelfLayout|formLayout13|ShelfLayout|Custom|shelfButton5'

```


```
如果对UI里的某一类control想做某方面的统一样式，如宽度、高度、边框等等，就可以定义个template，以后所有UI里的control都会自动统一到template，不用每次自定义了
from pymel.core import *

template = uiTemplate('ExampleTemplate', force=True)
template.define(button, width=100, height=30, align='right')
template.define(frameLayout, borderVisible=True, labelVisible=False)

if window('firstWithWindow', exists = 1): deleteUI('firstWithWindow', window = True)
with window('firstWithWindow', menuBar=True,menuBarVisible=True, title = 'WithWindow') as win:
    # start the template block
    with template:
        with columnLayout( rowSpacing=5, adj = 1 ):
            with frameLayout():
                with columnLayout(adj = 1):
                    button(label='One')
                    button(label='Two')
                    button(label='Three')

            with frameLayout():
                with horizontalLayout() as h5:
                    button(label = 'Push Me!')
                    button(label = 'Pull Him!')
                    h5.redistribute(30, 30)
            with frameLayout():
                with optionMenu():
                    menuItem(label='Red')
                    menuItem(label='Green')
                    menuItem(label='Blue')

    # add a menu to an existing window
with win:
    with menu(label = 'File'):
        menuItem(label='One')
        menuItem(label='Two')
        with subMenuItem(label='Sub'):
            menuItem(label='A')
            menuItem(label='B')
        menuItem(label='Three')

```






```
maya中真正的可以多线程或者是回调函数
scriptJob

```

```
maya中真正的dock控制器
dockControl = cmds.workspaceControl(
    '123',
    tabToControl=["AttributeEditor", -1],
    initialWidth=123,
    minimumWidth=True,
    widthProperty="preferred",
    label='text'
)
```


```
import maya
maya.utils.loadStringResourcesForModule(__name__)

import maya.cmds as cmds

def positionAlongCurve():
	'''Space selected objects along selected curve by its parameterization.
	Rebuilding the curve to even parameterization will space the objects evenly.'''

	objects = cmds.ls( selection=1 )

	# should have at least 3 objects, 1 being a curve
    检查选取对象，并且找到曲线
	if (objects.__len__()>2):

		# check for the curve in the selection
		curve = r'temporaryCurveNamePlaceholder'
		for object in objects:
			child = cmds.listRelatives( object, shapes=1, fullPath=1)
			# print (child )
			if (cmds.nodeType( child ) == r'nurbsCurve'):
				print (maya.stringTable['y_positionAlongCurve.kTest' ])
				curve = object

		if (curve == r'temporaryCurveNamePlaceholder'):
			errorString = maya.stringTable['y_positionAlongCurve.kNoCurve' ]
			#raise RuntimeError( 'error _L10N( kNoCurve, "Position Along Curve: No curve selected to position along" )' )
			raise RuntimeError( errorString )

		# remove the curve from the list of selected objects
		objects.remove( curve )

		numObjects = objects.__len__()

		if (numObjects>1):
			for i in range( 0, numObjects ):
				position = list()
				normal = list()
				# first object goes to start of curve
				if i == 0:
					position = cmds.pointOnCurve( curve, position=1, parameter=0, turnOnPercentage=1 )
					normal = cmds.pointOnCurve( curve, normal=1, parameter=0, turnOnPercentage=1 )
				# middle objects get evenly spaced along curve
				elif i < numObjects-1:
					position = cmds.pointOnCurve( curve, position=1, parameter=((1.0/(numObjects-1))*i), turnOnPercentage=1)
					normal = cmds.pointOnCurve( curve, normal=1, parameter=((1.0/(numObjects-1))*i), turnOnPercentage=1)
				# last object goes to end of curve
				else:
					position = cmds.pointOnCurve( curve, position=1, parameter=1, turnOnPercentage=1 )
					normal = cmds.pointOnCurve( curve, normal=1, parameter=1, turnOnPercentage=1 )

				# move object to appropriate point on the curve
				#cmds.move( position[0], position[1], position[2], objects[i], absolute=1 )

				# get the pivot for offsetting the object based on pivot
				pivot = cmds.xform( objects[i], query=1, rotatePivot=1 )
				position[0] = position[0] - pivot[0]
				position[1] = position[1] - pivot[1]
				position[2] = position[2] - pivot[2]
				cmds.xform( objects[i], translation= (position[0], position[1], position[2])  )

	else:
		errorString = maya.stringTable['y_positionAlongCurve.kNoSelection' ]
		#raise RuntimeError( 'error _L10N( kNoSelection, "Position Along Curve: Nothing selected. Select a curve and two or more nodes." )' )
		raise RuntimeError( errorString )


# ===========================================================================
# Copyright 2016 Autodesk, Inc. All rights reserved.
#
# Use of this software is subject to the terms of the Autodesk license
# agreement provided at the time of installation or download, or which
# otherwise accompanies this software in either electronic or hard copy form.
# ===========================================================================

```

```
编队飞行通信


无线传感器网络动态覆盖的CVT算法

```

```
python查看全局变量 并查看占用内存大小
for x in locals().keys():
    print x,sys.getsizeof(x)
v = 1
print sys.getsizeof(v)
  del locals()[x]

```



```
设定对象永远面朝相机，需要aim绑定设置 并且确定好偏移值
if (`window -ex amiWin`) deleteUI amiWin; window -t "FaceToCam" -wh 170 110 amiWin;windowPref -r amiWin;columnLayout -adj 1 Colmain;
separator -h 5 -style "none";
text -l "First: Select Cam and Geomentrys" textUi;
separator -h 5 -style "none";
button -l "Face To Cam!" -c FaceToCamera FTCbutton;
separator -h 5 -style "none";
button -l "Break Connect!" -c deleteCons Breakbutton;
separator -h 5 -style "none";
button -l "Set to default!" -c resetTo resetbutton;
showWindow amiWin;

//-----------------------------------------------------------------------
global proc FaceToCamera(){
string $list_cam[] = `ls -sl -dag -type camera `;
string $sel_cam[] =`listRelatives -p $list_cam[0]`;
string $list_obj[]=`ls -sl -dag -typ mesh`;
string $sel_obj[] =`listRelatives -p $list_obj`; for ($each in $sel_obj) {
setAttr ($each+".rotateX") 90; aimConstraint -u 0 1 0 -aim 0 0 1 -skip x $sel_cam[0] $each; }}
//-----------------------------------------------------------------------
global proc deleteCons(){ string $all_cons[]=`ls -type constraint`; select $all_cons; delete;}
//------------------------------------------------------------------------
global proc resetTo(){ string $list_obj[]=`ls -sl -dag -typ mesh`;
string $sel_obj[] =`listRelatives -p $list_obj`; for ($each in $sel_obj) { setAttr ($each+".r") 0 0 0; }}
```

```
外置大纲视图
window = cmds.window()
sl = cmds.scrollLayout(width =260)

frame2 = cmds.frameLayout(label='分组', collapsable=True, collapse = False,width =250)
tv = cmds.treeView(numberOfButtons = 2,height=200, abr = 1,pressCommand=[(1,Dmd_UAVC_Group_add),(2,Dmd_UAVC_Group_delete)],selectCommand=Dmd_UAVC_Group_select,editLabelCommand = Dmd_UAVC_Group_text_change)
cmds.treeView(tv, e=True, addItem = ('空组', ""))
cmds.treeView(tv, e=True, buttonTextIcon=(['空组', 1, '增'],['空组', 2, '删']),font = ('空组','boldLabelFont'))
cmds.   rowLayout(numberOfColumns = 1)
cmds.       button(label = "刷新分组",width = 250,command = "Dmd_UAVC_Group_sence_refresh()")
cmds.   setParent( '..' )

cmds.   rowLayout(numberOfColumns = 2)
cmds.       button(label = "设置所有可选对象",width = 125,command = "Dmd_UAVC_Group_set_select_all()")
cmds.       button(label = "反选",width = 125,command = "Dmd_UAVC_Group_select_reverse()")
cmds.   setParent( '..' )

cmds.setParent( '..' )

frame3 = cmds.frameLayout(label=' 大纲视图', collapsable=True, collapse = False,height=710,width=250)
#p = cmds.formLayout(parent = frame3)
panel = cmds.outlinerPanel()
outliner = cmds.outlinerPanel(panel, query=True,outlinerEditor=True)
cmds.outlinerEditor( outliner, edit=True, mainListConnection='worldList', selectionConnection='modelList', showShapes=False, showReferenceNodes=False, showReferenceMembers=False, showAttributes=False, showConnected=False, showAnimCurvesOnly=False, autoExpand=False, showDagOnly=True, ignoreDagHierarchy=False, expandConnections=False, showCompounds=True, showNumericAttrsOnly=False, highlightActive=True, autoSelectNewObjects=False, doNotSelectNewObjects=False, transmitFilters=False, showSetMembers=True, setFilter='defaultSetFilter', ignoreHiddenAttribute=False, ignoreOutlinerColor=False )
#cmds.formLayout(p,e=True, attachForm=[(panel,'top', 2),(panel,'left', 2),(panel,'bottom', 2),(panel,'right', 2)])
#cmds.setParent( '..' )
if cmds.dockControl("Dmd_UAVC_Control_Outline_dock", exists = True):
    cmds.deleteUI("Dmd_UAVC_Control_Outline_dock", control=True)
cmds.dockControl('Dmd_UAVC_Control_Outline_dock',area = 'left', content = window, allowedArea = ['right', 'left'],label = "大漠大剧本编辑大纲",width =250)



```

```
提示框 弹出框
cmds.confirmDialog(title='动画',message="导入球数太少,选择球数太多")
```


```
预着色

先选择，然后在预着色，类似于bake的方式将当前灯光颜色直接给到顶点着色
cmds.select()
cmds.polyGeoSampler(ids = True,lightingOnly=True,scaleFactor=True,su= True,cdo=True,colorBlend = 'overwrite',alphaBlend = 'overwrite')
polyGeoSampler -ids -lo -sf 1 -su -cdo -colorBlend "add" -alphaBlend "overwrite";

获取顶点颜色
cmds.polyColorPerVertex( query=True, r=True,g=True, b=True )

删除顶点颜色
cmds.polyColorPerVertex(remove=True)

批量设置属性
# get param
#glowIntensity = cmds.floatField("Dmd_UAVC_Color_Render_glowIntensity", query = True, value = True)
end_time   = cmds.floatField("Dmd_UAVC_Color_end_time", query = True, value = True)
spheres = cmds.ls("dmd*", selection = True, transforms = True)

for s in spheres:
    obj_name    = 'dmd_material' + s[3:]
    cmds.setAttr(obj_name + '.translucence', 1.0)
    cmds.setAttr(obj_name + '.diffuse', 1.0)
    cmds.setAttr(obj_name + '.translucenceFocus', 0.0)
    cmds.setAttr(obj_name + '.translucenceDepth', 5.0)
```


```
获取材质所对应UV上的颜色
cmds.colorAtPoint( 'file1', o='RGB',u=.5, v=.5 )

print cmds.colorAtPoint( 'file1', o='RGB', u=.0, v=.0 )




```


```
auto_background = cmds.checkBox('Dmd_UAVC_Color_auto_background', query = True, value = True)
Dmd_UAVC_Color_auto_background
    ui_param["Dmd_UAVC_Color_auto_background"] = ('checkBox',auto_background)
    if auto_background:


```

```
用于面板上产生一个滑动条
def translateXSlider( HUD ):
	# Since undo is not turned off automatically, we must
	# do it ourselves. The HUD will fire off many calls to this
	# procedure during a drag so we don't want to flood the undo
	# queue.
	cmds.undoInfo( swf=False )
	for object in cmds.ls( sl=True ):
		if cmds.objectType( object, isType='transform' ):
		   translateX = object + '.tx'
		   value = cmds.hudSlider( HUD, q=True, v=True )
		   cmds.setAttr( translateX, value )
	# Re-enable the undo queue.
	#
	cmds.undoInfo( swf=True)

# Now create our slider HUD
#
cmds.hudSlider( 'HUDTranslateXSlider',
				section=2,
				block=5,
				visible=1,
				label="TranslateX:",
				value=0,
				type="int",
				minValue=-10,
				maxValue=10,
				labelWidth=80,
				valueWidth=50,
				sliderLength=100,
				sliderIncrement=1,
				pressCommand='translateXSlider( "HUDTranslateXSlider" )',
				dragCommand='translateXSlider( "HUDTranslateXSlider" )',
				releaseCommand='translateXSlider( "HUDTranslateXSlider" )')
```


```
houdini导出剧本

import hou
import json
import sys
node = hou.node('/obj/FX/more_sphere')
print node
geo = node.geometry()
for attrib in geo.pointAttribs():
    attrib_count = attrib.size()
    print attrib_count
    print attrib.name()

number = 0
points = []
chanels = []
point_frames = []
chanel_frames = []
for point in geo.points():
    for attrib in geo.pointAttribs():
        if attrib.name() == 'pscale':
            continue
        elif attrib.name() == 'P':
            pos = point.attribValue(attrib)
            p = {"No" : number,
                        "X" : pos[0],
                        "Y" : pos[1],
                        "Z" : pos[2]}
            points.append(p)
        elif attrib.name() == 'Cd':
            color = point.attribValue(attrib)
            output_color_r = max(min(int(color[0] * 255),255),0)
            output_color_g = max(min(int(color[1] * 255),255),0)
            output_color_b = max(min(int(color[2] * 255),255),0)

            # add to chanels
            chanel = {"No" : number,
                        "Chanel1" : output_color_r,
                        "Chanel2" : output_color_g,
                        "Chanel3" : output_color_b}
            chanels.append(chanel)
    number+=1

#print len(geo.points())
current_time_ms = 0
point_frame = {"Points" : points,
                "ID" : 0,
                "Time" : current_time_ms}
point_frames.append(point_frame)

chanel_frame = {"Chanels" : chanels,
                "ID" : 0,
                "Time" : current_time_ms}
chanel_frames.append(chanel_frame)

drama = [{"PointFrames" : point_frames,
            "ChanelFrames" : chanel_frames,
            "Name" : "drama.jsdm",
            "Description" : "dmd",
            "PlaneCount" : len(geo.points()),
            "FrameCount" : 1}]

fileId =open(r'F:\Maya\houdinidrama1.jsdm',"w")
# indent = 4 will make the drama easy to read,and indent = None make the size of drama 327% smaller than 4
fileId.write(json.dumps(drama, sort_keys = True, indent = 4))
fileId.close()




```

```
houdini获取geometry spreadsheet数据
hou.Attrib class

node = hou.pwd()
geo = node.geometry()

# CONFIG
filename = "test.csv"
separator = ","

# Get File
f = file(filename, "w")

# Create Column
for attrib in geo.pointAttribs():
    attrib_count = attrib.size()
    if 1 != attrib_count:
        for i in range(0,attrib_count):
            if i > 2:   # if its a Multi Array
                f.write(attrib.name() + " [" + chr(94 + i) + "]" + separator) # ASCII to Char
            else:
                f.write(attrib.name() + " [" + chr(88 + i) + "]" + separator) # ASCII to Char

    else:
        f.write(attrib.name())
        f.write(separator)
f.write("\n")

# Insert Points in File
for point in geo.points():
    for attrib in geo.pointAttribs():
        attrib_count = attrib.size()
        if 1 != attrib_count:
            for i in range(0,attrib_count):
                f.write(str(point.attribValue(attrib)[i]) + separator)
        else:
            f.write(str(point.attribValue(attrib)))
            f.write(separator)
    f.write("\n")

# Save the CSV File
f.close()

```



## Code Snippet

```
二进制方式写入字节流
#-*- coding: utf-8 -*-
import struct
import array
f = open('f:/test.bin','wb')
data = [0,1,2,3]
for j in range(100):
    for i in range(256):
        data = [i]*512
        a = array.array('B', data)
        #data.tofile(f)
        f.write(a)
f.close()
```




```

python默认的递归深度是很有限的，大概是900多的样子，当递归深度超过这个值的时候，就会引发这样的一个异常。
解决的方式是手工设置递归调用深度，方式为
import sys
sys.setrecursionlimit(1000000) #例如这里设置为一百万
最大流dinic算法
zkw
费用流
网络流
最小流
裸的最大流
isap
Hopcroft-Karp
Hungarian算法
```


``` python

kinematic chain path plot 运动链路径图
```

```c
MARS
静态规划->集中规划 centralized planning 全局路径规划

解耦规划 decoupled plannning

sofa problem  W.E.Howden

可视顶点图 VGRAPH 仅限平移运动

位姿空间 configuration space 可用

势场法 可用

PSO 粒子群优化算法

PSPACE-Hard 刚体空间运动归属于

GA Genetic Algorithm  遗传算法

Principles of Robot Motion: Theory, Algorithms, and Implementations，然后再找具体的论文


Decoupled Multiagent Path Planning via Incremental Sequential Convex Programming


Nash合作与非合作对策

粒子群优化算法（PSO, Particle Swarm Optimization），属于进化计算技术（evolutionary computation）领域，是一种集群优化算法，在1995年由Eberhart博士和Kennedy博士发明[


我推荐使用RRT-star算法。RRT*算法是RRT算法的变种算法，算法可以收敛到最优解，不仅可以实现二维环境下的路径规划，多维度的环境也可以使用RRT*算法，而且由于算法是均匀采样，并不会出现局部最小的情况。相关论文RRT*Sampling-based algorithms for optimal motion planninghttp://arxiv.org/abs/1005.0416RRTRandomized Kinodynamic Planning

作者：施晋
链接：https://www.zhihu.com/question/26342064/answer/100974273
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

人工鱼群算法，不适合做为运动规划，适合求一些最优参数类似的问题

formation control 编队控制
flocking control 集群控制

RRT 快速拓展随机数方法，路径不是最优，但是无碰撞，行之有效

参数化，难度大，条件多，但是结果最优
```

```c
支持网络DMX协议ArtNet，并可扩充其它协议。
同时输出DMX512信号，方便接入不同的灯具。
ARTNET网络灯光控制器

artnet 3 协议

1.4 Art-Net协议

这个FreeStyler 3.5.0是至2012-9-21月最新版的USB-DMX512灯光控台控制软件，支持3D的,可使用MIDI配合Cubase软件实现音乐同步控制,效果是专业级别的。

Vectorworks的软件

Vectorworks的软件

MIDI控制器

ASIO

LED Music Effect

音序器 sequencer

All of the sequences were generated by lining up timings of beats/measures in Audacity (audio editor) to particular commands to my sequencer.

If you're already used to MIDI sequencers it's maybe the best option to do it using the sequencer and MIDI input in QLC+ when it works fine for you.
```

```c
crowdmaker 群集控制 自动寻路

linstep 获取百分比关系 进而得到UV值
，它们就是sphere的control vertex，简称CV
```


```c
SciPy是一个开源的Python算法库和数学工具包。
SciPy包含的模块有最优化、线性代数、积分、插值、特殊函数、快速傅里叶变换、信号处理和图像处理、常微分方程求解和其他科学与工程中常用的计算。与其功能相类似的软件还有MATLAB、GNU Octave和Scilab。

重点是pymedia：
Pymedia 是个 C/C++/Python 的多媒体模块，可以对包括 mp3/ogg/avi等多媒体格式文件进行编码解码和播放，基于 ffmpeg 提供了简单的 Python 接口。
```



```c
子线程安全调用主线程的函数
import maya.utils import maya.cmds
def doSphere( radius ):
	maya.cmds.sphere( radius=radius )
maya.utils.executeInMainThreadWithResult( doSphere, 5.0 )
```

```c
使用esc打断脚本执行 进度条
import maya.cmds as cmds
cmds.progressWindow(isInterruptable=1)
while 1 :
    print "kill me!"
    if cmds.progressWindow(query=1, isCancelled=1) :
        break

cmds.progressWindow(endProgress=1)
```


```c
动画师之路
动画师生存手册
微妙动画网 注册一个  很多动画教程
http://www.cg-yy.com/site/index.html
http://www.cg-yy.com/
```

```c
内部弹窗提示
#cmds.inViewMessage( amg="your workspace is :"+curpath +'  <hl>please put the Dmdmapgenerator at your workspace</hl>.', pos='midCenter', fade=True )
```

```c
获取当前使用工具
print cmds.currentCtx()
切换到目标工具
cmds.setToolTo('RotateSuperContext')
```

```c
获取通道栏属性
import maya.cmds as cmds
import maya.mel as cmds_mel
channelBox = cmds_mel.eval('global string $gChannelBoxName; $temp=$gChannelBoxName;')
attrs = cmds.channelBox(channelBox, q=True, sma=True)
print attrs
```


```
给模型添加属性，并且让该属性显示到通道盒里 并且显示在曲线编辑器中 并且判断是否存在当前属性，不存在的情况下不创建对应的表达式
import maya.cmds as cmds
obj_name = 'pSphere1'

if not cmds.attributeQuery('speed',node = obj_name,exists = True):
    cmds.select(obj_name)
    cmds.addAttr(longName = 'speed', attributeType = 'double', defaultValue = 0.0)
    cmds.setAttr(obj_name + '.speed',edit = True, channelBox = True)
    cmds.expression(string = "float $x = `getAttr -t (frame) "+obj_name+".translateX` - `getAttr -t (frame-1) "+obj_name+".translateX`;\nfloat $y = `getAttr -t (frame) "+obj_name+".translateY` - `getAttr -t (frame-1) "+obj_name+".translateY`;\nfloat $z = `getAttr -t (frame) "+obj_name+".translateZ` - `getAttr -t (frame-1) "+obj_name+".translateZ`;\n"+obj_name+".speed = $x*$x + $y * $y + $z * $z;\n"+obj_name+".speed = sqrt("+obj_name+".speed) * 24;" ,object = obj_name, alwaysEvaluate = True , unitConversion = 'all')
    # 修改采样率为20帧一采样 否则会特别卡
    cmds.animCurveEditor('graphEditor1GraphEd', edit=1, showResults='on',af='on',resultSamples=20,s='fine',vlt='on')
```

