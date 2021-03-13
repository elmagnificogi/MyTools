select_tools_name = "select_tool"
def select_tools_press():
    import maya.OpenMaya as om
    pressPosition = cmds.draggerContext(select_tools_name, query=True, anchorPoint=True)
    modifier = cmds.draggerContext(select_tools_name, query=True, modifier=True)
    #debug_print("Press: " + str(pressPosition))
    #debug_print(pressPosition[0])
    #debug_print(pressPosition[1])
    list_adjustment = om.MGlobal.kAddToList
    #debug_print(modifier)
    if modifier == "ctrl":
        list_adjustment = om.MGlobal.kRemoveFromList

    om.MGlobal.selectFromScreen(int(pressPosition[0]), int(pressPosition[1]), list_adjustment)


def select_tools_drag():
    import maya.OpenMaya as om
    dragPosition = cmds.draggerContext(select_tools_name, query=True, dragPoint=True)
    modifier = cmds.draggerContext(select_tools_name, query=True, modifier=True)
    #debug_print("drag: " + str(dragPosition))
    #debug_print(dragPosition[0])
    #debug_print(dragPosition[1])
    list_adjustment = om.MGlobal.kAddToList
    #debug_print(modifier)
    if modifier == "ctrl":
        list_adjustment = om.MGlobal.kRemoveFromList

    om.MGlobal.selectFromScreen(int(dragPosition[0]), int(dragPosition[1]), list_adjustment)

cmds.draggerContext(select_tools_name, pressCommand=lambda *args: select_tools_press(),
                                dragCommand=lambda *args: select_tools_drag(), cursor='crossHair',i1="123d.png")

# change to the new tool
cmds.setToolTo(select_tools_name)