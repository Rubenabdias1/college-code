; Name:			        Ruben Nunez
; Class and Section:	CS 245 01
; Assignment:		    Program Assignment 02
; Due Date:		        Monday, March 15, 2021
; Date Turned in:       Monday, March 15, 2021
; Program Description:	This program asks the user for three numbers and then add them adds them.
						After it displays the sum, it prompts the user for a fourth number and
						substracts it from the sum. Finally, it displays the total after the substraction.
						
.586
.MODEL FLAT

INCLUDE io.h            ; header file for input/output

.STACK 4096

.DATA
number1     DWORD   ?
number2     DWORD   ?
number3     DWORD   ?
number4     DWORD   ?
prompt1     BYTE    "Enter first number", 0
prompt2     BYTE    "Enter second number", 0
prompt3     BYTE    "Enter third number", 0
prompt4     BYTE    "Enter fourth number", 0
string      BYTE    40 DUP (?)
resultLbl   BYTE    "The sum is", 0
subsLbl     BYTE    "After substraction", 0
sumValue	DWORD	0
sum         BYTE    11 DUP (?), " total", 0
subs        BYTE    11 DUP (?), " total", 0

.CODE
_MainProc PROC
        input   prompt1, string, 40		; read ASCII characters
        atod    string					; convert to integer
        mov     number1, eax			; store in memory

        input   prompt2, string, 40     ; repeat for second number
        atod    string
        mov     number2, eax

        input   prompt3, string, 40     ; repeat for third number
        atod    string
        mov     number3, eax
        
        mov     eax, number1			; first number to EAX
        add     eax, number2			; add second number
        add     eax, number3			; add third number
		mov		sumValue, eax			; saving the sum in sumValue
        dtoa    sum, eax				; convert to ASCII characters
        output  resultLbl, sum          ; output label and sum

        input   prompt4, string, 40     ; repeat for third number
        atod    string
        mov     number4, eax

		mov		eax, sumValue
		sub		eax, number4
		dtoa    subs, eax				; convert to ASCII characters
        output  subsLbl, subs			; output label and sum

        mov     eax, 0  ; exit with return code 0
        ret
_MainProc ENDP
END                             ; end of source code

