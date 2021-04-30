; Name:			        Ruben Nunez
; Class and Section:	CS 245 01
; Assignment:		    Program Assignment 05
; Due Date:		        Wednesday, April 28, 2021
; Date Turned in:       Wednesday, April 28, 2021
; Program Description:	This program asks the user for two numbers that must be greater than 1. Then, it
;						calculates and outputs the greatest common divisor.
;						Please grade extra credit.
						
.586
.MODEL FLAT

INCLUDE io.h            ; header file for input/output

.STACK 4096

.DATA
number1     DWORD   ?
number2     DWORD   ?
prompt1     BYTE    "Enter first number", 0
prompt2     BYTE    "Enter second number", 0
numInvalid  BYTE    "Invalid input", 0
num1Inv     BYTE    "Number 1 is not greater than 1", 0
num2Inv     BYTE    "Number 2 is not greater than 1", 0
string      BYTE    40 DUP (?)
resultLbl   BYTE    "The Greatest Common Divisor is:", 0
gcd         BYTE    11 DUP (?), 0

.CODE
_MainProc PROC

ask1:   input   prompt1, string, 40		; read ASCII characters
        atod    string					; convert to integer
        cmp     eax, 1
        jg      cont1
        output  numInvalid, num1Inv  
        jmp     ask1
cont1:  mov     number1, eax			; store in memory
        
ask2:   input   prompt2, string, 40		; read ASCII characters
        atod    string					; convert to integer
        mov     number2, eax			; store in memory
        cmp     eax, 1
        jg      cont2
        output  numInvalid, num2Inv
        jmp     ask2
cont2:  mov     number2, eax			; store in memory

		; gcd -> ebx | remainder -> edx | dividend -> eax
        mov     ebx, number1			; number1 to EAX | gcd:= number1
        mov     edx, number2            ; number2 to ECX | remainder := number2
rep1:   mov     eax, ebx				; dividend (eax) := gcd (ebx)
        mov     ebx, edx				; gcd (ebx) := remainder (edx) <- first time is number2
        cdq								; prepare for division
        idiv    ebx						; edx = eax mod ebx | remainder = dividend (eax) mod gcd (ebx)
        mov     ecx, edx				; copying remainder(edx) to ecx to use jump if ecx is zero (jecxz)
        jecxz   done					; if ecx is zero we are done, jump to output
        jmp     rep1					; otherwise, we have to repeat the process

done:	mov		eax, ebx			    ; copying gcd (ebx) to eax for conversion
        dtoa    gcd, eax				; convert to ASCII characters
        output  resultLbl, gcd          ; output label and greatest common divisor
        mov     eax, 0                  ; exit with return code 0
        ret

_MainProc ENDP
END                             ; end of source code

