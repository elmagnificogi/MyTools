# ECE 375Final

主要是结合Lab6和7然后再用Lab4 老师给好的一个驱动 一起联调 写成一个摩斯码发送系统

>ATmega128的开发板
>
>软件模拟调试
>
>



```
github上一堆lab67的代码
谷歌搜 ECE 375 github
```



## 提交时间

最晚时间-太平洋时间周四24点前-北京时间周五16点前

约定时间-周三





# 作业要求



## 摩斯码

短音-读作滴，用 · 表示，dot

长音-读作嗒 ，用 — 表示，dash

相当于是0和1的表示方法，但是这里有一点不同，由于是使用声音来表示的，所以长短时间很重要，滴只有一拍时间，而长音嗒有3拍的时间

并且为了区分长短音，在每个音中间又有一个停留间隔。

- 一个单词内相同音之间停留一拍

- 单词之间停留3拍

- 一句话之间停留7拍

这样就定义了空格和句号，那么就可以写文章了

![image-20201206173640679](E:\homework\ECE375\ECE375Final.assets\image-20201206173640679.png)

## 目的

用板子上的LED做为摩斯码的信号，发送A-Z的消息

3个LED 在每个摩斯bit的间隔，全灭



启动时：要求LCD显示器上出现，保持长显，直到按下

```
Welcome!
Please press PD0
```

按下PD0以后，出现如下信息

```
Enter word:
A
```

按下 PD7 反向显示一个字母A，Z，Y，X...->A，可以循环

按下 PD6 正向显示一个字母A,B,C,D...->Z，可以循环

按下 PD0 确定按钮，确定以后显示下一个字符，同样从A开始，并且之前的字母不能修改了

最多显示16个字母，再按的时候直接开始发送摩斯码

按下 PD4 直接开始发送摩斯码

在发送摩斯码的时侯，LED4 保持常亮，就算bit间隔也是常亮的

发送完成之后，回到初始状态

必须使用Timer Counter1 来发送摩斯码，不能用空循环等待延时

按键去抖的空循环等待延时可以用，按键去抖不超过10ms

发送摩斯码的时候，按任何按键都没用

PD0，PD4，PD5，PD6，PD7 配置成输入，上拉模式，PD5是用来测试程序是否会对其他按键反应的

LCD不能乱显示



## 时间设置

单位时间是1秒

滴的持续时间是1秒

嗒的持续时间是3秒

相同bit间隔时间是1秒

字母之间是3秒



有一个测试模式（UserMode）的内存字节，为0x01的时候，单位时间变成1s，当为0x00的时候，单位时间变成200ms



时间不要求一模一样，差不多就行了



## 硬件映射

这个3个LED用来表示摩斯码的信号，拉高亮，拉低灭

- PB5,LED1

- PB6,LED2
- PB7,LED3



在发送摩斯码的时侯，LED4 保持常亮，就算bit间隔也是常亮的

- PB4,LED4 



按键，默认为高，按下为低

- PD0，PD4，PD5，PD6，PD7



## 报告

1. 如何实现的



## 提交内容

1. 程序文件 asm，不需要LCD的驱动文件
2. 一个pdf 关于设计的报告，还要流程图
3. 是否使用了中断或者是轮询，说明一下
4. Timer用来干嘛了，精度设置的多少，对应1秒和200ms
5. 重写一遍的话，还有啥想设计的和现在不同的
6. 校对报告，请别人校对一下

报告几页都可以，完美就行



#### 疑问

template 文件是什么样的，为什么要用

```
Your grade will be reduced if you do not use the assembly code template file that is provided.
```

- 解了，给了一个ece375-final_skeleton.asm的模板文件，从这里开始写



# log

- 20分钟安装搭建环境
- 10分钟学习IDE基础操作，完成单步调试，IO显示，memory显示，寄存器显示查看
- 花了50分钟用来阅读整个文档要求，并记录
- 花10分钟阅读了一下原理图
- 60分钟，大概熟悉一下指令
- 30分钟，写出整体框架，完成摩斯码转二进制
- 40分钟，确定Timer的设置，计数值都是多少

已经3小时40分了

- 60分钟，确认初始化设置ok，运行正常

- 82分钟，才完成了一部分初始化过程，核心还没开始写

- 50分钟，完成部分初始和运行逻辑内容，依然还有核心没写

截至到现在用时大概6小时30分钟

- 花30分钟，阅读lab6源码，看懂他干什么了，并且有什么源码可以再利用
- 120分钟完成显示主流程，摩斯码发送框架
- 60分钟完成所有编码部分，准备开始debug
- 60分钟，key与LCD显示ok
- 80分钟，中断调试，有问题重构发送循环
- 60分钟，写报告



# 指令

## 伪指令

.include 包含一个定义文件，一般都是关于内部寄存器的定义的

.def 定义寄存器符号名，相当于是寄存器有了别名而已

.dseg 声明数据段

.org 设置程序起始位置

.byte 在 SRAM 中预留存储单元 有点像new

.cseg 声明代码段

.DB 定义字节常数，需要对齐，并且其内容无法修改

.equ 定义标识符常量



## 汇编指令

clr 清零寄存器

jmp 直接跳转

ldi 赋值立即数

out 输出到端口，就是赋值给硬件寄存器

sts 存储到sram中

cpi 比较内容

brne 不相等跳转指令



#### 寄存器

r16之前部分指令无法使用

r26开始不要用

X、Y 和 Z：地址指针寄存器（X=R27:26；Y=R29:28；Z=R31:R30）



# 主流程

1. 初始化LED IO与KEY IO
2. 初始化timer，从固定地址读取数值，然后转换成对应的一个unit的时间
3. 初始化LCD
4. 轮询等待输入，根据输入各种情况判定，并切亮灯
5. 等待中断完成，返回回到开始初始化的地方



```
当前位index = 第一位的
BST 获取该位
BRTS 根据该位为1决定跳转
如果跳转，那么LED亮，并且等待结束
如果不跳转，LED灭，并且等待结束
结束以后，位数+1，如果位数==8，那么读取下一个字节，继续循环，
如果位数==16，那么结束循环，等待3个时间周期，然后回到最初的循环
```



### timer的设定

timer 可以设置成触发一次是1s，如果读取到某个固定的值，那么将所有PB拉高/低



timer count 1 是16位计数器，使用CTC模式，比价匹配后清零计数器

0100



TCCR1A

位

0 0 0 0 0 0 0 0 

此时处于比较输出模式



TCCR1B，后三位选择时钟源，全0为无时钟源，停止，

0 0 0 0 1 1 0 0



 TCNT1H与 TCNT1L 计数器，当前值



TIMSK 中断屏蔽寄存器，OCIE1A为比较溢出中断使能位



计数器的比较值为OCR1A



TIFR 中断标志寄存器，当溢出时OCF1A被置位，写入逻辑1可以清除该标志位



时钟源是16Mhz，可以1分频，8分频，64分频，最大1024分频

1024分频以后，大概频率变成了15625Hz，这样的最大计数65535就是 就是4秒了，绰绰有余

比较计数值为15625即可定时为1秒

定时为100ms，则设置为1562即可，这样就能完成Timer的定时功能了。



也可以用256分频，变成62500HZ，然后设置为62500就是1秒，6250就是100ms

对应的 CS就是100，



### 摩斯码二次编码

对摩斯码二次编码,短音用bit 1表示，停顿用bit0表示，长音用3个bit1表示

这样对二十六个字母重新编码，得到的最多不超过2个字节，编码后有一个稳定规律，就是一个摩斯码的开头和结尾必然是1，那么就可以通过字符比较来得到实际需要输出的编码（从第一个不为0的bit开始输出，到最后一个bit即可）



| 字符 | 编码前 | 编码后        | 两字节，十六进制 |
| ---- | ------ | ------------- | ---------------- |
| A    | .-     | 10111         | 0x00,0x17        |
| B    | -...   | 111010101     | 0x01,0xD5        |
| C    | -.-.   | 11101011101   | 0x07,0x5D        |
| D    | -..    | 1110101       | 0x00,0x75        |
| E    | .      | 1             | 0x00,0x01        |
| F    | ..-.   | 101011101     | 0x01,0x5D        |
| G    | --.    | 111011101     | 0x01,0xDD        |
| H    | ....   | 1010101       | 0x00,0x55        |
| I    | ..     | 101           | 0x00,0x05        |
| J    | .---   | 1011101110111 | 0x17,0x77        |
| K    | -.-    | 111010111     | 0x01,0xD7        |
| L    | .-..   | 101110101     | 0x01,0x75        |
| M    | --     | 1110111       | 0x00,0x77        |
| N    | -.     | 11101         | 0x00,0x1D        |
| O    | ---    | 11101110111   | 0x07,0x77        |
| P    | .--.   | 10111011101   | 0x05,0xDD        |
| Q    | --.-   | 1110111010111 | 0x1D,0xD7        |
| R    | .-.    | 1011101       | 0x00,0x5D        |
| S    | ...    | 10101         | 0x00,0x15        |
| T    | -      | 111           | 0x00,0x07        |
| U    | ..-    | 1010111       | 0x00,0x57        |
| V    | ...-   | 101010111     | 0x01,0x57        |
| W    | .--    | 101110111     | 0x01,0x77        |
| X    | -..-   | 11101010111   | 0x07,0x57        |
| Y    | -.--   | 1110101110111 | 0x1D,0x77        |
| Z    | --..   | 11101110101   | 0x07,0x75        |



# ref

参考代码

>https://github.com/search?o=desc&q=ece375&s=updated&type=Repositories
>
>https://github.com/garcaaro/ECE375/blob/main/Aaron_Garcia_Lab4_sourcecode.asm
>
>https://github.com/garcaaro/ECE375/blob/main/Aaron_Garcia_Lab6_sourcecode.asm
>
>https://github.com/garcaaro/ECE375/blob/main/Aaron_Garica_lab7_sourcecode.asm



lab4中根据counter来决定显示的内容

```
Updatescreen:
		rcall	LCDClr			;clear anything currently on the screen	
		ldi		ZH, high(STRING1_BEG<<1); Initialize z pointer to address of first letter in string1 
		ldi		ZL, low(STRING1_BEG<<1)
		ldi		YH, high(LCDLn1Addr)	; Initialize y pointer to address of first line of LCD
		ldi		YL, low(LCDLn1Addr)
		ldi		mpr, leftlength
		mov		counter, mpr	; Initialize counter to length of first string
LINE1:
		lpm		mpr, Z+			; Grab ascii value of next character from address pointed to by z, move z to address of next character
		st		Y+, mpr			; Store next ascii character value at the address of that bit of the display, move to next display bit
		dec		counter			; Decrement remaining string lenght counter
		brne	LINE1			; Loop if entire string has not been passed in
		mov		mpr, leftcount	; Move left count into a temporary register to add ascii offset without affecting the count
		ldi		r23, $30		; Store ascii offset in another temporary register
		add		mpr, r23		; Add ascii offset to x register so numbers are printed correctly
		st		Y, mpr			; Stores offset number to last screen address for line 1
		ldi		ZH, high(STRING2_BEG<<1); Initialize z pointer to address of first letter in string2 
		ldi		ZL, low(STRING2_BEG<<1)
		ldi		YH, high(LCDLn2Addr)	; Initialize y pointer to address of second line of LCD
		ldi		YL, low(LCDLn2Addr)
		ldi		mpr, rightlength
		mov		counter, mpr	; Initialize counter to length of second string
LINE2:
		lpm		mpr, Z+			; Grab ascii value of next character from address pointed to by z, move z to address of next character
		st		Y+, mpr			; Store next ascii character value at the address of that bit of the display, move to next display bit
		dec		counter			; Decrement remaining string lenght counter
		brne	LINE2			; Loop if entire string has not been passed in
		mov		mpr, rightcount ; Move left count into a temporary register to add ascii offset without affecting the count
		ldi		r23, $30		; Store ascii offset in another temporary register
		add		mpr, r23		; Add ascii offset to x register so numbers are printed correctly
		st		Y, mpr			; Stores offset number to last screen address for line 1
		rcall LCDWrite			; Writes new values to LCD
		ret
```











