; Name:						Ruben Nunez
; Class and Section:		CS 245 01
; Assignment:				Programming Assignment Additional Chapter 04
; Due Date : 				Wednesday, April 21, 2021 
; Date Turned in :			Wednesday, April 21, 2021 
; Program Description :		This program outputs the balance as a result of having a credit
; 							of $84 and a debit of $29


.586
.MODEL FLAT

INCLUDE io.h; header file for input / output

.STACK 4096

.DATA
credit		DWORD	84
debit		DWORD	29
helloLabel  BYTE    "Credit and Debit", 0
prompt1     BYTE    "The balance is:", 0
balanceLbl  BYTE    "The balance result is:", 0
balance    	BYTE    11 DUP(? ), " dollars", 0

.CODE
_MainProc	PROC
        	output  helloLabel, prompt1     ; output starting prompt
			mov		eax, credit				; eax = 84
			sub		eax, debit				; eax = eax - debit = credit - debit = 84 - 29
			dtoa    balance, eax			; convert to ASCII characters
			
			output  balanceLbl, balance 	; result

			mov     eax, 0					; exit with return code 0
			ret
_MainProc 	ENDP
END											; end of source code

