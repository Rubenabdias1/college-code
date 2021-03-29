; Program to add three numbers
.586
.MODEL FLAT
.STACK  4096        ; reserve 4096-byte stack

.DATA               ; reserve storage for data
x			DWORD   250
y			DWORD   300
z			DWORD   100
b			DWORD	1
divisor		DWORD	?
result		DWORD   ?

.CODE                ; start of main pgm code
main		PROC
			mov		ecx, 0BF7Ah
			mov		ecx, -1

			mov		eax, 0ABh
			sub		eax, 40

			mov		edx, 2E9h
			inc		edx

			mov		eax, 14h
			mov		ebx, 7
			mov		edx, 0FFAC02h
			mul		ebx
			
			mov		eax, 0CAh
			mov		ecx, 0Dh
			mov		edx, 0
			div		ecx
			
			mov		eax, x
			add		eax, y
			sub		eax, z
			mov		ecx, b
			inc		ecx
			mov		edx, 0
			div		ecx
			mov		result, eax

			mov     eax, 0        ; exit w/ return code 0
			ret
main		ENDP
END                           ; end of source code