; Name:						Ruben Nunez
; Class and Section:		CS 245 01
; Assignment:				Programming Assignment Additional Chapter 04
; Due Date : 				Wednesday, April 21, 2021 
; Date Turned in :			Wednesday, April 21, 2021 
; Program Description :		The price of one share of a stock fell 4 dollars each day for 8 days.
; 							This program outputs how much value did one share of the stock lose 
;							after 8 days.

.586
.MODEL FLAT

INCLUDE io.h; header file for input / output

.STACK 4096

.DATA
decrease	DWORD	4
days		DWORD	8
helloLabel  BYTE    "Stock Price", 0
prompt1     BYTE    "A share of stock lost:", 0
valueLbl  	BYTE    "Value lost", 0
valueLost	BYTE    11 DUP(? ), " dollars", 0

.CODE
_MainProc	PROC
        	output  helloLabel, prompt1     ; output label and sum
            mov     eax, decrease			; eax = decrease per days
			mul		days					; eax = decrease per days * days = 4 * 8
			dtoa    valueLost, eax			; convert to ASCII characters
			
			output  valueLbl, valueLost 	; output result

			mov     eax, 0					; exit with return code 0
			ret
_MainProc 	ENDP
END											; end of source code

