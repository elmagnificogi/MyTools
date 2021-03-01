;***********************************************************
;*
;*	Enter Name of file here
;*
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
.def	A = r3					; A variable
.def	B = r4					; Another variable
.def	mpr = r16				; Multipurpose register 
.def	oloop = r17				; Outer Loop Counter
.def	iloop = r18				; Inner Loop Counter
.def	dataptr = r19			; data ptr

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
.org	$0046					; End of Interrupt Vectors
;-----------------------------------------------------------
; Program Initialization
;-----------------------------------------------------------
INIT:	; The initialization routine
	clr  zero
	; To do
	; your code goes in this area

;-----------------------------------------------------------
; Main procedure
;-----------------------------------------------------------
MAIN:
	; more code
	; you will probably have an infinite loop in your code that handles input from the user
	jmp	MAIN

;***********************************************************
;*	Procedures and Subroutines
;***********************************************************
; your code can go here as well


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


;***********************************************************
;*	Additional Program Includes
;***********************************************************
.include "LCDDriver.asm"		; Include the LCD Driver from Lab 4
