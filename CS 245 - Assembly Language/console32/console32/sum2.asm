.586
.MODEL FLAT

.STACK 4096

.DATA
number	DWORD	45h

.CODE
main4	PROC
		mov eax, number
		add eax, -45

		mov eax, 0
		ret
main4	ENDP

END