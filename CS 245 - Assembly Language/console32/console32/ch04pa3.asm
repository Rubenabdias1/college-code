; Name:					Ruben Nunez
; Class and Section:	CS 245 01
; Assignment:			Program Assignment 03
; Due Date:				Wednesday, March 24, 2021
; Date Turned in:		Wednesday, March 24, 2021
; Program Description:	This program computes in eax the result of this expression: 2(-num1 + num2 - 1) + num3. 
;						The values stored in num1, num2 and num3 are -1, 1, and five respectively. Therefore,
;						the result in eax will be 7;
.586
.MODEL FLAT
.STACK  4096        ; reserve 4096-byte stack

.DATA               ; reserve storage for data
num1		DWORD   -1
num2		DWORD   1
num3		DWORD   5
result		DWORD   ?

.CODE                ; start of main pgm code
main		PROC
			mov		eax, num1		; eax = num1
			neg		eax				; eax = -num1
			add		eax, num2		; eax = (-num1 + num2)
			sub		eax, 1			; eax = (-num1 + num2 - 1)
			imul	eax, eax, 2		; eax = 2(-num1 + num2 - 1)
			add		eax, num3		; eax = 2(-num1 + num2 - 1) + num3 / 2(-(-1) + 1 - 1) + 5
			; eax = 2(1 + 1 - 1) + 5
			; eax = 2(1) + 5
			; eax = 2 + 5
			; eax = 7
			mov     eax, 0        ; exit w/ return code 0
			ret
main		ENDP
END                           ; end of source code