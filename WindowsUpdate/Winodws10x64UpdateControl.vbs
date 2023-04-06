' 管理Win10自动更新v2.vbs.
' 20190607 初始版本,实现了基本功能;
' 使用说明 https://blog.csdn.net/milaoshu1020/article/details/91126200
Const wuauserv_reg = "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\wuauserv"
Set fso = createobject("scripting.filesystemobject")
Set shell = createobject("wscript.shell")
curdir = fso.getparentfoldername(wscript.scriptfullname)
 
If wscript.arguments.count = 0 Then
	Set sh = createobject("shell.application")
	sh.shellexecute wscript.fullname,"""" & wscript.scriptfullname & """ -admin",,"runas"
ElseIf wscript.arguments.count = 1 And wscript.arguments(0) = "-admin" Then
	run
Else
	msgbox "脚本启动参数错误!"
End If
 
Sub Run()
	Do
		ret = inputbox("1. 禁止Win10自动更新;" & vbcrlf & _
						"2. 恢复Win10自动更新;" & vbcrlf & _
						vbcrlf & _
						"请输入序号:","管理Win10自动更新v2","1")
		Select Case ret
		Case "1"
			retnum = shell.run("sc.exe stop wuauserv",0,True)
			shell.regwrite wuauserv_reg & "\WOW64",&H14c,"REG_DWORD"
			msgbox "已禁止Win10自动更新!",vbexclamation
			Exit Do
		Case "2"
			shell.regdelete wuauserv_reg & "\WOW64"
			retnum = shell.run("sc.exe start wuauserv",0,True)
			msgbox "已恢复Win10自动更新!",vbexclamation
			Exit Do
		Case ""
			Exit Do
		Case Else
			msgbox "输入错误!请重新输入!",vbcritical
		End Select
	Loop
End Sub