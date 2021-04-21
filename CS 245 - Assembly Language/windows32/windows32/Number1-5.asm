; Name:						Ruben Nunez
; Class and Section:		CS 245 01
; Assignment:				Programming Assignment Additional Chapter 04
; Due Date : 				Wednesday, April 21, 2021 
; Date Turned in :			Wednesday, April 21, 2021 
; Program Description :		This program outputs Josie's balance if she has left on her checking account, then
;							writes a check for $55.

.586
.MODEL FLAT

INCLUDE io.h; header file for input / output

.STACK 4096

.DATA
initialBal  DWORD	47
check		DWORD	55
helloLabel  BYTE    "Josie's Balance", 0
prompt1     BYTE    "Josie's balance is:", 0
balanceLbl  BYTE    "Josie's balance", 0
finalBal    BYTE    11 DUP(? ), " dollars", 0

.CODE
_MainProc	PROC
        	output  helloLabel, prompt1     ; output starting prompt
			mov		eax, initialBal			; eax = initial balance = 47
			sub		eax, check				; eax = eax - check = 47 - 55
			dtoa    finalBal, eax			; convert to ASCII characters
			
			output  balanceLbl, finalBal 	; output the result

			mov     eax, 0					; exit with return code 0
			ret
_MainProc 	ENDP
END											; end of source code

