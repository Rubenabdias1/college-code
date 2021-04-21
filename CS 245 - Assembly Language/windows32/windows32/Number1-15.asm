; Name:						Ruben Nunez
; Class and Section:		CS 245 01
; Assignment:				Programming Assignment Additional Chapter 04
; Due Date : 				Wednesday, April 21, 2021 
; Date Turned in :			Wednesday, April 21, 2021 
; Program Description :		This program outputs how much money will Sonny need to borrow if he 
;							wants to make a purchase that requires $93 but he only has $75 available.

.586
.MODEL FLAT

INCLUDE io.h; header file for input / output

.STACK 4096

.DATA
available	DWORD	75
price		DWORD	93
helloLabel  BYTE    "Sonny's problem", 0
prompt1     BYTE    "Sonny needs to borrow:", 0
borrowLbl  	BYTE    "Sonny needs to borrow:", 0
needed    	BYTE    11 DUP(? ), " dollars", 0

.CODE
_MainProc	PROC
        	output  helloLabel, prompt1     ; output starting prompt
			mov		eax, price				; eax = 93
			sub		eax, available			; eax = eax - available = 93 - 75
			dtoa    needed, eax				; convert to ASCII characters
			
			output  borrowLbl, needed 		; output result

			mov     eax, 0					; exit with return code 0
			ret
_MainProc 	ENDP
END											; end of source code

