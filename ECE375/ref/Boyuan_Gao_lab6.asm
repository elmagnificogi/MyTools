;***********************************************************
;*
;*	Enter Name of file here
;*
;*	Enter the description of the program here
;*
;*	This is the skeleton file for Lab 6 of ECE 375
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
;***********************************************************
.def	mpr = r16	
.def	waitcnt = r17
.def	ilcnt = r18	
.def	olcnt = r19	

.equ	WTime = 100	

.equ	WskrR = 0
.equ	WskrL = 1
.equ	EngEnR = 4
.equ	EngEnL = 7	
.equ	EngDirR = 5	
.equ	EngDirL = 6	

.equ	MovFwd = (1<<EngDirR|1<<EngDirL)
.equ	MovBck = $00
.equ	TurnR = (1<<EngDirL)
.equ	TurnL = (1<<EngDirR)
.equ	Halt = (1<<EngEnR|1<<EngEnL)	
;***********************************************************
;*	Start of Code Segment
;***********************************************************
.cseg							; Beginning of code segment

;***********************************************************
;*	Interrupt Vectors
;***********************************************************
.org	$0000					; Beginning of IVs
		rjmp 	INIT			; Reset interrupt

		; Set up interrupt vectors for any interrupts being used
.org	$0002
		rcall HitRight
		reti
.org	$0004
		rcall HitLeft
		reti

.org	$0046					; End of Interrupt Vectors

;***********************************************************
;*	Program Initialization
;***********************************************************
INIT:							; The initialization routine
		; Initialize Stack Pointer
		ldi		mpr, low(RAMEND)
		out		SPL, mpr
		ldi		mpr, high(RAMEND)
		out		SPH, mpr
		; Initialize Port B for output
		ldi		mpr, $FF
		out		DDRB, mpr
		ldi		mpr, $00
		out		PORTB, mpr
		; Initialize Port D for input
		ldi		mpr, $00
		out		DDRD, mpr
		ldi		mpr, $FF
		out		PORTD, mpr
		ldi mpr, (1<<ISC01)|(0<<ISC00)|(1<<ISC11)|(0<<ISC10)
		sts EICRA, mpr
		ldi mpr,$00
		sts EICRA,mpr
		ldi mpr, (1<<INT0)|(1<<INT1)
		out EIMSK, mpr
	
		sei
			; NOTE: This must be the last thing to do in the INIT function

;***********************************************************
;*	Main Program
;***********************************************************
MAIN:							; The Main program

		; TODO: ???
		ldi mpr, MovFwd
		out PORTB, mpr

		rjmp	MAIN			; Create an infinite while loop to signify the 
								; end of the program.

;***********************************************************
;*	Functions and Subroutines
;***********************************************************

;-----------------------------------------------------------
;	You will probably want several functions, one to handle the 
;	left whisker interrupt, one to handle the right whisker 
;	interrupt, and maybe a wait function
;------------------------------------------------------------

;-----------------------------------------------------------
; Func: Template function header
; Desc: Cut and paste this and fill in the info at the 
;		beginning of your functions
;-----------------------------------------------------------
FUNC:							; Begin a function with a label
ret
HitRight:
		push	mpr
		push	waitcnt
		in		mpr, SREG
		push	mpr
		ldi		mpr, MovBck
		out		PORTB, mpr
		ldi		waitcnt, WTime
		rcall	Wait

		ldi		mpr, TurnL
		out		PORTB, mpr
		ldi		waitcnt, WTime
		rcall	Wait

		ldi		mpr, MovFwd
		out		PORTB, mpr

		pop		mpr	
		out		SREG, mpr
		pop		waitcnt	
		pop		mpr	
		ret	

		; Execute the function here
HitLeft:
		push	mpr
		push	waitcnt
		in		mpr, SREG
		push	mpr

		ldi		mpr, MovBck
		out		PORTB, mpr
		ldi		waitcnt, WTime
		rcall	Wait

		ldi		mpr, TurnR
		out		PORTB, mpr
		ldi		waitcnt, WTime
		rcall	Wait

		ldi		mpr, MovFwd
		out		PORTB, mpr

		pop		mpr	
		out		SREG, mpr
		pop		waitcnt	
		pop		mpr	
		ret	
Wait:
		push	waitcnt
		push	ilcnt
		push	olcnt

Loop:	ldi		olcnt, 224
OLoop:	ldi		ilcnt, 237
ILoop:	dec		ilcnt
		brne	ILoop
		dec		olcnt
		brne	OLoop
		dec		waitcnt
		brne	Loop

		pop		olcnt
		pop		ilcnt
		pop		waitcnt	
		ret


;***********************************************************
;*	Stored Program Data
;***********************************************************

; Enter any stored data you might need here

;***********************************************************
;*	Additional Program Includes
;***********************************************************
; There are no additional file includes for this program