' ����Win10�Զ�����v2.vbs.
' 20190607 ��ʼ�汾,ʵ���˻�������;
' ʹ��˵�� https://blog.csdn.net/milaoshu1020/article/details/91126200
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
	msgbox "�ű�������������!"
End If
 
Sub Run()
	Do
		ret = inputbox("1. ��ֹWin10�Զ�����;" & vbcrlf & _
						"2. �ָ�Win10�Զ�����;" & vbcrlf & _
						vbcrlf & _
						"���������:","����Win10�Զ�����v2","1")
		Select Case ret
		Case "1"
			retnum = shell.run("sc.exe stop wuauserv",0,True)
			shell.regwrite wuauserv_reg & "\WOW64",&H14c,"REG_DWORD"
			msgbox "�ѽ�ֹWin10�Զ�����!",vbexclamation
			Exit Do
		Case "2"
			shell.regdelete wuauserv_reg & "\WOW64"
			retnum = shell.run("sc.exe start wuauserv",0,True)
			msgbox "�ѻָ�Win10�Զ�����!",vbexclamation
			Exit Do
		Case ""
			Exit Do
		Case Else
			msgbox "�������!����������!",vbcritical
		End Select
	Loop
End Sub