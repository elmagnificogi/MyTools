;***********************************************************
;*
;*	Enter Name of file here
;*  Boyuan Gao
;*	Enter the description of the program here
;*
;*	This is the skeleton file for the ECE 375 final project
;*
;***********************************************************
;*
;*	 Author: Enter your name
;*	   Date: Enter Date
;*
;***********************************************************
.include "m128def.inc"			; Include definition file
;***********************************************************
;*	Internal Register Definitions and Constants
;*	(feel free to edit these or add others)
;***********************************************************
.def	rlo = r0				; Low byte of MUL result
.def	rhi = r1				; High byte of MUL result
.def	zero = r2				; Zero register, set to zero in INIT, useful for calculations
.def	bytel = r3				; A variable
.def	byteh = r4				; Another variable
.def	mpr = r16				; Multipurpose register 
.def	byte_L = r17			; Outer Loop Counter
.def	morse = r17			; Outer Loop Counter
.def	byte_H = r18			; Inner Loop Counter
.def	len = r18			; Inner Loop Counter
.def	dataptr = r19			; data ptr
.def	input_counter = r20		; data ptr
.def    char_index = r24        ; the input char index
.def    temp = r25        		; some temp value
.def    cur_index = r21
;***********************************************************
;*	Data segment variables
;*	(feel free to edit these or add others)
;***********************************************************
.dseg
.org	$0200						; data memory allocation for operands
operand1:		.byte 2				; allocate 2 bytes for a variable named operand1

; Important Reminder:
; The LCD driver expects its display data to be arranged as follows:
; - Line 1 data is in address space $0100-$010F
; - Line 2 data is in address space $0110-$010F

;***********************************************************
;*	Start of Code Segment
;***********************************************************
.cseg							; Beginning of code segment
;-----------------------------------------------------------
; Interrupt Vectors
;-----------------------------------------------------------
.org	$0000					; Beginning of IVs
		rjmp  INIT				; Reset interrupt

;timer1 interrupt
.org	$0018
		rjmp	TIM1INT
		RETI
;timer1 interrupt
.org	$001C
		rjmp	TIM1INT
		RETI

.org	$0046					; End of Interrupt Vectors
;-----------------------------------------------------------
; Program Initialization
;-----------------------------------------------------------
INIT:	; The initialization routine
	; Initialize Stack Pointer
	ldi	mpr, low(RAMEND)
	out	SPL, mpr        
	ldi	mpr, high(RAMEND)
	out	SPH, mpr  

	clr  zero
	; To do
	; your code goes in this area
	; set the port B Output High Source
	ldi mpr,$FF
	out DDRB,mpr
	; set all PB low,leds disable
	ldi mpr,$00
	out PORTB,mpr

	; set the port D input and pull-up
	ldi mpr,$00
	out DDRD,mpr
	ldi mpr,$FF
	out PORTD,mpr
	;ldi mpr,$02
	;out SFIOR,mpr

	cli
	;init the Timer count 1 CTC mode
	ldi mpr,$00
	out TCCR1A,mpr
	;clk/256
	ldi mpr,$04
	out TCCR1B,mpr
	;disable interrupt
	ldi mpr,$00
	out TIMSK,mpr
	; clean interrupt flag
	ldi mpr,$FF
	out TIFR,mpr
	;set the counter
    ldi byte_H,$00
	ldi byte_L,$00
	;ldi byte_H,30
	;ldi byte_L,D4
	out TCNT1H,byte_H
	out TCNT1L,byte_L
	
	rcall LCDInit			; initialize lcd display
	rcall LCDClr			; clear lcd display in case it is not done in initialization

;-----------------------------------------------------------
; Main procedure
;-----------------------------------------------------------
MAIN:
	; more code
	; you will probably have an infinite loop in your code that handles input from the user
	; show welcome info
	rcall WELCOME

;***********************************************************
;*	wait PD0 to start
;***********************************************************
	; check input key
WAITPD0START:
	; debouncing 8ms
	rcall KeyWait
	; stores pind input to multipurpose register
	in	mpr, PIND       
	; check if PD0 has been pressed
	cpi	mpr, 0b11111110	
	; if not, continue to WAITPD0
	brne WAITPD0START
	;if PD0 press,go on,show tip3 and A
	ldi input_counter ,1
	ldi char_index ,0
	rcall LCDClr	
	;write the value A
	rcall WriteLCDAddr
	;show it
	rcall SHOWTIP3
	rcall SHOWINPUT

;***********************************************************
;*	check input key and show in LCD
;***********************************************************
CHECKINPUT:
	; debouncing 8ms
	rcall KeyWait
	; stores pind input to multipurpose register
	in	mpr, PIND      

	; check if PD7 has been pressed
	cpi	mpr, 0b01111111	
	brne CHECKPD6
	;if PD7 press,show last char
	dec char_index
	CPI char_index,255
	BREQ RESET1
	rcall WriteLCDAddr
	rcall SHOWINPUT
	rjmp CHECKINPUT
	
RESET1:
	ldi char_index,25
	rcall WriteLCDAddr
	rcall SHOWINPUT
	rjmp CHECKINPUT

CHECKPD6:
	; check if PD6 has been pressed
	cpi	mpr, 0b10111111	
	brne CHECKPD0
	;if PD6 press
	inc char_index
	CPI char_index,26
	BREQ RESET2
	rcall WriteLCDAddr
	rcall SHOWINPUT
	rjmp CHECKINPUT
	
RESET2:
	ldi char_index,0
	rcall WriteLCDAddr
	rcall SHOWINPUT
	rjmp CHECKINPUT

CHECKPD0:
	; check if PD0 has been pressed
	cpi	mpr, 0b11111110	
	brne CHECKPD4
	;if PD0 press,next char
	inc input_counter
	CPI input_counter,17
	BREQ PRETRANSMIT
	ldi char_index,0
	rcall WriteLCDAddr
	rcall SHOWINPUT
	rjmp CHECKINPUT

CHECKPD4:
	; check if PD4 has been pressed
	cpi	mpr, 0b11101111	
	brne CHECKINPUT
	;if PD4 press,transmit start
	inc input_counter
	jmp TRANSMIT

PRETRANSMIT:
	;the counter is 17 need -1
	;dec input_counter
	jmp TRANSMIT

TRANSMITEND1:
	jmp INIT

;***********************************************************
;*	start transmit
;***********************************************************
TRANSMIT:
	;PB4 = LED4 enable
	ldi mpr,0b00010000
	out PORTB,mpr
	ldi cur_index,0
;***********************************************************
;*	first get input char,then get the map morse bits
;***********************************************************
GETCHAR:
	; loop
	; read from LCDLn2Addr to get char
	ldi ZH, high(LCDLn2Addr)
	ldi ZL, low(LCDLn2Addr)
	add ZL,cur_index
	inc cur_index
	cp cur_index,input_counter
	; end 
	breq TRANSMITEND1

	ld mpr,Z+
	subi mpr,$41

	;mov ptr to the pos in morse
	ldi ZH, high(MorseBits<<1)
	ldi ZL, low(MorseBits<<1)
	;ldi r22,$FE
	;ldi r25,2
DD:
	;add r22,r25
	;dec mpr
	;brne DD
	;mul r22,mpr
	add zl,mpr
	add zl,mpr
	brcs ADDZH 
	jmp LOADBITS

ADDZH:
	inc zh

LOADBITS:
	lpm morse,Z+
	;dec input_counter
	;brne SEARCH1BIT
	;jmp TRANSMITEND
;***********************************************************
;*	find the first 1 bit in morse bits
;***********************************************************
SEARCH1BIT:
	;first 8 bits to move
	ldi r18,8
FIRST:
	CLC
	rol morse
	;find the first 1
	BRCS PRETRANSMITLOOP1
	;not 1 ,check left bits
	dec r18
	brne FIRST
	; we cant find first 0 in first bytes
	; so we search next bit
	ldi r18,8
	lpm morse,Z+
	;dec r22
SECOND:
	CLC
	rol morse
	;find the first 1
	BRCS PRETRANSMITLOOP2
	;not 1 ,check left bits
	dec r18
	brne SECOND
	;it couldnt here
	jmp INIT

PRETRANSMITLOOP1:
	;move back
	ror morse
	rcall TRANSMITLOOP
	ldi len,8
	lpm morse,Z+
	rcall TRANSMITLOOP
	rcall LEWAIT
	;ldi mpr,8
	;add len,mpr
	;jmp TRANSMITLOOP
	jmp GETCHAR

PRETRANSMITLOOP2:
	;move back
	ror morse
	rcall TRANSMITLOOP
	rcall LEWAIT
	jmp GETCHAR
	;jmp TRANSMITLOOP
;***********************************************************
;*	start to transmit every bit
;***********************************************************
TRANSMITLOOP:
	CLC
	ROL morse;,len
	;if the bit is 1 jump
	BRCS LEDONWAIT
	;BRTS LEDONWAIT
LEDOFFWAIT:
	;the bit is zero
	; make it off
	ldi mpr,0b00010000
	out PORTB,mpr
	rcall TIMERWAIT
	;cpi len,8
	;BREQ LOADNEXTBYTE
RELOOP:
	dec len
	brne TRANSMITLOOP
	;goto next char
	ret
	;jmp LEWAIT

LOADNEXTBYTE:
	lpm morse,Z+
	jmp RELOOP

LEDONWAIT:
	; make it light
	ldi mpr,0b11110000
	out PORTB,mpr
	rcall TIMERWAIT
	;cpi len,8
	;BREQ LOADNEXTBYTE
	dec len
	brne TRANSMITLOOP
	;goto next char
	ret
	;jmp LEWAIT

;***********************************************************
;*	wait between letters
;***********************************************************
LEWAIT:
	ldi mpr,0b00010000
	out PORTB,mpr
	rcall TIMERWAIT
	rcall TIMERWAIT
	rcall TIMERWAIT
	ret
	;jmp GETCHAR

;***********************************************************
;*	Timer wait func
;***********************************************************
TIMERWAIT:
	ret
	push r19
	push ZH
	push ZL
	push r16
	push byte_H
	push byte_L
	; set r19
	ldi r19,1
	;disable all
	cli
	ldi r19,1
	;init the Timer1 normal mode
	ldi mpr,$00
	out TCCR1A,mpr
	;clk/256
	ldi mpr,$04
	out TCCR1B,mpr
	; clean interrupt flag
	ldi mpr,$FF
	out TIFR,mpr
	;set the counter
	ldi ZH, high(UserMode<<1)
	ldi ZL, low(UserMode<<1) 
	lpm r16, Z	
	cpi r16,1
	breq LOADCOUNTER1
	ldi byte_H,$E7
	ldi byte_L,$95
LC:	ldi mpr,0
	out TCNT1H,byte_H
	out TCNT1L,byte_L
	;open intrrupt
	ldi mpr,0b00000100	
	out TIMSK,mpr
	;enable all
	sei
WAITEND1:
	cpi r19,0
	brne WAITEND1
	;wait end,go on next bit
	pop byte_L
	pop byte_H
	pop r16
	pop ZL
	pop ZH
	pop r19
	ret

LOADCOUNTER1:
	ldi byte_H,$0B
	ldi byte_L,$DB
	jmp LC

TRANSMITEND:
	jmp INIT
	
;***********************************************************
;*	Procedures and Subroutines
;***********************************************************
; your code can go here as well

;***********************************************************
;*	show welcome info
;***********************************************************
WELCOME:
		rcall LCDClr		; Clear anything already on the screen
		
		; Move Tip1 from Program Memory to Data Memory
		; Initialize Z-pointer
		ldi ZH, high(Tip1<<1)
		ldi ZL, low(Tip1<<1) 
		; Initialize y pointer
		ldi	YL, low(LCDLn1Addr) 
		ldi	YH, high(LCDLn1Addr)
		; 8 bytes to show
		ldi	r23, 8		

LINE1:
		; Load constant from Program
		lpm r16, Z+		
		; Store constant to one past the address pointed to by Y	
		st  Y+, r16			
		; Decrement Read Counter
		dec	r23	
		; Return back to the start of LINE1 if zero flag is 0
		brne LINE1
		
		; Move string2 from Program Memory to Data Memory
		; Initialize Z-pointer
		ldi ZH, high(Tip2<<1)
		ldi ZL, low(Tip2<<1)
		; Initialize y-pointer
		ldi	YL, low(LCDLn2Addr) 
		ldi	YH, high(LCDLn2Addr)
		; 16 bytes to show
		ldi	r23, 16

LINE2:
		; Load constant from Program
		lpm r16, Z+	
		; Store constant to one past the address pointed to by Y		
		st  Y+, r16	
		; Decrement Read Counter		
		dec	r23		
		; Return back to the start of LINE1 if zero flag is 0	
		brne LINE2		

		; Write new values to lcd
		rcall LCDWrite	
		; End a function with RET
		ret
		
SHOWINPUT:
		; Write new values to lcd
		rcall LCDWrite	
		; End a function with RET
		ret

;***********************************************************
;*	show input info and input char
;***********************************************************
;use for show tip3 string
SHOWTIP3:
		push r23
		; Initialize Z-pointer
		ldi ZH, high(Tip3<<1)
		ldi ZL, low(Tip3<<1) 
		; Initialize y pointer
		ldi	YL, low(LCDLn1Addr) 
		ldi	YH, high(LCDLn1Addr)
		; 8 bytes to show
		ldi		r23, 11		

SHOWTIP3L:
		; Load constant from Program
		lpm r16, Z+		
		; Store constant to one past the address pointed to by Y	
		st  Y+, r16			
		; Decrement Read Counter
		dec	 r23	
		; Return back to the start of LINE1 if zero flag is 0
		brne SHOWTIP3L
		pop r23
		ret
		
WriteLCDAddr:
		;write cur char in to the LCDLn2Addr,then show it
		;first jump to the addr
		; Initialize y pointer to address of first line of LCD
		ldi		YH, high(LCDLn2Addr)	
		ldi		YL, low(LCDLn2Addr)
		mov		mpr, input_counter
		; Initialize counter to length of first string
CHECK:
		dec		mpr
		brne	MP
		; at the next char pos
		ldi		r23, $41
		add		r23,char_index
		st      Y,r23
		ret
MP:
		ld r23,Y+
		jmp CHECK
		;move point

;*******************************************************
;* Func:	key wait about 8ms
;* Desc:	A wait loop that is 10 + 159*wait cycles or
;*			roughly wait*10us.  Just initialize wait
;*			for the specific amount of time in 10us 
;*			intervals.
;*******************************************************
KeyWait:push	mpr				; Save mpr
		push    r17
		push	r18
		ldi     r18,1
Wait4:	ldi     r17,200
Wait1:	ldi		mpr, $49		; Load with a 10us value
Wait2:	dec		mpr				; Inner Wait Loop
		brne	Wait2
		dec		r17				; Outer Wait Loop
		brne	Wait1
		dec		r18				; Outer Wait Loop
		brne	Wait4
		pop     r18
		pop     r17
		pop		mpr				; Restore mpr
		ret						; Return from Wait Function		

TIM1INT:
		;make r19 2
		ldi r19,0
		;disable intrrupt
		CLI
		ret

;***end of your code***end of your code***end of your code***end of your code***end of your code***
;******************************* Do not change below this point************************************
;******************************* Do not change below this point************************************
;******************************* Do not change below this point************************************


;***********************************************************
;*	Stored Program Data
;***********************************************************

; Contents of program memory will be changed during testing
; The label names are not changed

; If UserMode is 0x01, then one unit of time is 1 second
UserMode:	.DB	0x01, 0x00
; You can ignore the second byte (it's only included so that there is an even number of bytes)

; If UserMode is 0x00, then one unit of time is 200 milliseconds
; This would look like the following:
;UserMode:	.DB	0x00, 0x00
; (again, ignore the second byte)

; UserMode will always be set to either 0x00 or 0x01
Tip1:       .DB	"Welcome!"	
Tip2:       .DB	"Please press PD0"
Tip3:       .DB	"Enter word:"	
Chars:		.DB	"ABCDEFGHIJKLMNOPQRSTUVWXYZ"	
MorseBits:		.DB	0x00,0x17,0x01,0xD5,0x07,0x5D,0x00,0x75,0x00,0x01,0x01,0x5D,0x01,0xDD,0x00,0x55,0x00,0x05,0x17,0x77,0x01,0xD7,0x01,0x75,0x00,0x77,0x00,0x1D,0x07,0x77,0x05,0xDD,0x1D,0xD7,0x00,0x5D,0x00,0x15,0x00,0x07,0x00,0x57,0x01,0x57,0x01,0x77,0x07,0x57,0x1D,0x77,0x07,0x75

;***********************************************************
;*	Additional Program Includes
;***********************************************************
.include "LCDDriver.asm"		; Include the LCD Driver from Lab 4
