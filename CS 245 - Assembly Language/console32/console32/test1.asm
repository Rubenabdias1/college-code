; Program to add three numbers
.586
.MODEL FLAT
.STACK  4096        ; reserve 4096-byte stack

.DATA               ; reserve storage for data
number1		DWORD   85
number2		DWORD   -47
number3		DWORD   91
sum			DWORD   ?

.CODE                ; start of main pgm code
main		PROC
			mov eax, number1  ; first number to EAX
			add     eax, number2  ; add second number
			add     eax, number3  ; add third number
			mov     sum, eax      ; sum to memory
			mov     eax, 0        ; exit w/ return code 0
			ret
main		ENDP
END                           ; end of source code