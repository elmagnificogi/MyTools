;******************************************************
;LAB 6 TIMER/COUNTERS
;*****************************************************
; BOYUAN GAO
; 2020/11/20
;**************************************************
.include "m128def.inc"	; include definition file
;**************************************************
;internal register definition and constants
;**************************************************

.def	mpr = r16
.def	speedCnt = r17
.def	waitcnt = r18
.def	ilcnt = r19
.def	olcnt = r20
.def	speedDial = r21
.equ	debounceTime = 20
;*******************************************************
; start of code segment
;*******************************************************

.cseg		;beginning of code segment
;*******************************************************
;interrupt vector
;*******************************************************
.org	$0000
		rjmp	INIT
.org	$0046
;********************************************************
;program initialization
;*******************************************************
INIT:			; the initialization routine

		LDI		mpr, LOW(RAMEND)
		OUT		SPL, mpr			;Load spl with low byte of ramend
		LDI		mpr, HIGH(RAMEND)
		OUT		SPH, mpr			;load sph with high byte of ramend

		LDI		mpr, $FF			; set portB data direction register
		OUT		DDRB, mpr			;for output
		LDI		mpr, $00			;set port d data direction register
		OUT		DDRD, mpr			;for input

		LDI		mpr, 0b01111001		;cofigure 8bit timer
		OUT		TCCR0, mpr
		OUT		TCCR2, mpr

		LDI		mpr, 255
		OUT		OCR0, mpr
		OUT		OCR2, mpr
		OUT		PORTB,mpr
		LDI		speedCnt, 0			;display on port b initial duty cycle
		LDI		speedDial, 0
		OUT		OCR0, speedDial
		OUT		OCR2, speedDial

		IN		mpr, PORTB			; get whisker input feom portD
		ANDI	mpr, $F0
		OR		mpr, speedCnt
		OUT		PORTB, mpr			;set mpr to outpot
;***********************************************************
; main program
;***********************************************************
MAIN:
;***********************************************************
;MAKE SPEED LEVEL ADD 1
;***********************************************************
SPEEDUP:
		IN		mpr, PIND
		SBRC	mpr, 0		;touch first button
		RJMP	SPEEDDOWN	;jump
		CPI		speedCnt, $0F
		BREQ	ENDUPBUTTON
		LDI		waitcnt, debounceTime 
		CALL	Wait		;use wait function
		INC		speedCnt
		LDI		mpr, 17		;255/15=17
		ADD		speedDial, mpr
ENDUPBUTTON:
		OUT		OCR0, speedDial
		OUT		OCR2, speedDial
;**************************************************************
;MAKE SPEED LEVEL MINUS 1
;**************************************************************
SPEEDDOWN:
	IN		mpr, PIND
		SBRC	mpr, 1		;touch second button
		RJMP	SPEEDHIGH	;jump
		CPI		speedCnt, $00
		BREQ	ENDDOWNBUTTON
		LDI		waitcnt, debounceTime	
		CALL	Wait		;use wait function
		DEC		speedCnt
		SUBI	speedDial, 17		;255/15=17
ENDDOWNBUTTON:
		OUT		OCR0, speedDial
		OUT		OCR2, speedDial
;************************************************************
;MAKE SPEED LEVEL HIGHEST
;************************************************************
SPEEDHIGH:
		IN		mpr, PIND
		SBRC    mpr, 2		;touch third button
		RJMP	SPEEDLOW	;jump
		CPI		speedCnt, $0F
		BREQ	ENDHIGHBUTTON
		LDI		waitcnt, debounceTime 
		INC		speedCnt
		LDI		mpr, 17			;255/15=17
		ADD		speedDial, mpr
ENDHIGHBUTTON:
		OUT		OCR0, speedDial
		OUT		OCR2, speedDial
;****************************************************************
;MAKE SPEED LEVEL LOWEST
;****************************************************************
SPEEDLOW:
		IN		mpr, PIND
		SBRC	mpr, 3		;touch forth button 
		RJMP	TESTEND		;jump
		CPI		speedCnt, $00
		BREQ	ENDLOWBUTTON
		LDI		waitcnt, debounceTime	
		DEC		speedCnt
		SUBI	speedDial, 17		;255/15=17
ENDLOWBUTTON:
		OUT		OCR0, speedDial
		OUT		OCR2, speedDial
;***************************************************************
;END TEST
;****************************************************************
TESTEND:
		IN		mpr, PORTB		;read in port b
		ANDI	mpr, $F0		;out the led
		OR		mpr, speedCnt	;for lower value port b count
		OUT		PORTB, mpr		;set portb mpr to output
		NOP
END:
		rjmp	MAIN
;*********************************************************************
;wait loop that is 16+ 159975 * waitcnt cycles or roughly
;*********************************************************************
Wait:
		push	waitcnt		;save wait register
		push	ilcnt		;save ilcnt register
		push	olcnt		;save olcnt register

Loop:	ldi		olcnt, 224	;load olcnt register
OLoop:	ldi		ilcnt, 237	;load ilcnt register
ILoop:	dec		ilcnt		;decrement  ilcnt
		brne	ILoop		;continue inner loop
		dec		olcnt		;decrement plcnt
		brne	OLoop		;continue outer loop
		dec		waitcnt		;decrement wait
		brne	Loop		;continue wait loop

		pop		olcnt		;restore olcnt register
		pop		ilcnt		;restore ilcnt register
		pop		waitcnt		;restore wait register
		ret					;return from subroutine

