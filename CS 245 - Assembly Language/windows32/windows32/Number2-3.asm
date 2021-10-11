; Name:						Ruben Nunez
; Class and Section:		CS 245 01
; Assignment:				Programming Assignment Additional Chapter 04
; Due Date : 				Wednesday, April 21, 2021 
; Date Turned in :			Wednesday, April 21, 2021 
; Program Description :		This program outputs how much money does Jay now have in his account. 
;							He had $256 in his savings account. He took $78 from the account to 
;							buy some running shoes. 

.586
.MODEL FLAT

INCLUDE io.h; header file for input / output

.STACK 4096

.DATA
balance		DWORD	256
withdrawal	DWORD	78
helloLabel  BYTE    "Jay Savings", 0
prompt1     BYTE    "Jay's Balance:", 0
availLbl  	BYTE    "Jay has", 0
available  	BYTE    11 DUP(? ), " dollars", 0

.CODE
_MainProc	PROC
        	output  helloLabel, prompt1     ; output starting prompt
            mov     eax, balance			; eax = 256
			sub		eax, withdrawal			; eax = balance - withdrawal = 256 - 78
			dtoa    available, eax			; convert to ASCII characters
			
			output  availLbl, available 	; output result

			mov     eax, 0					; exit with return code 0
			ret
_MainProc 	ENDP
END											; end of source code

