; Name:			        Ruben Nunez
; Class and Section:	CS 245 01
; Assignment:		    Program Assignment 03
; Due Date:		        Wednesday, March 24, 2021
; Date Turned in:       Wednesday, March 24, 2021
; Program Description:	This program asks the user for three numbers and then computes the expression:
;						2(-num1 + num2 - 1) + num3. The result is outputted to the screen.
						
.586
.MODEL FLAT

INCLUDE io.h            ; header file for input/output

.STACK 4096

.DATA
num1     DWORD   ?
num2     DWORD   ?
num3     DWORD   ?
prompt1     BYTE    "Enter first number", 0
prompt2     BYTE    "Enter second number", 0
prompt3     BYTE    "Enter third number", 0
string      BYTE    40 DUP (?)
resultLbl   BYTE    "The result is", 0
result		DWORD	?

.CODE
_MainProc PROC
        input   prompt1, string, 40		; read ASCII characters
        atod    string					; convert to integer
        mov     num1, eax			; store in memory

        input   prompt2, string, 40     ; repeat for second number
        atod    string
        mov     num2, eax

        input   prompt3, string, 40     ; repeat for third number
        atod    string
        mov     num3, eax
        
        mov		eax, num1		; eax = num1
        neg		eax				; eax = -num1
        add		eax, num2		; eax = (-num1 + num2)
        sub		eax, 1			; eax = (-num1 + num2 - 1)
        imul	eax, eax, 2		; eax = 2(-num1 + num2 - 1)
        add		eax, num3		; eax = 2(-num1 + num2 - 1) + num3 / 2(-(-1) + 1 - 1) + 5			; saving the sum in sumValue
        dtoa    result, eax				; convert to ASCII characters
        output  resultLbl, result          ; output label and sum

        mov     eax, 0  ; exit with return code 0
        ret
_MainProc ENDP
END                             ; end of source code

