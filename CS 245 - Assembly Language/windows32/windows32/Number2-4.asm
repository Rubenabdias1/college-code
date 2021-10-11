; Name:						Ruben Nunez
; Class and Section:		CS 245 01
; Assignment:				Programming Assignment Additional Chapter 04
; Due Date : 				Wednesday, April 21, 2021 
; Date Turned in :			Wednesday, April 21, 2021 
; Program Description :		This program outputs the overall decrease or increase
;							of the price of gas by the end of the day on Tuesday
;							when on Monday, the price of gas decreased 6 cents
;							and on Tuesday, it increased 9 cents. 

.586
.MODEL FLAT

INCLUDE io.h; header file for input / output

.STACK 4096

.DATA
mondayInc	DWORD	-6							 	; it decreased by 6
tuesdayInc	DWORD	9
helloLabel  BYTE    "Gas Price", 0
prompt1     BYTE    "The gas price increased:", 0
incLbl  	BYTE    "Price increased by", 0
increase  	BYTE    11 DUP(? ), " dollars", 0

.CODE
_MainProc	PROC
        	output  helloLabel, prompt1     ; output label and sum
            mov     eax, mondayInc
			add		eax, tuesdayInc			; eax = increase on monday + increase on tuesday	
			dtoa    increase, eax			; convert to ASCII characters
			
			output  incLbl, increase 		; output label and sum

			mov     eax, 0					; exit with return code 0
			ret
_MainProc 	ENDP
END											; end of source code

