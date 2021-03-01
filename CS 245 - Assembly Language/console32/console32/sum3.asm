.586
.MODEL FLAT

.STACK 4096

.DATA
number	DWORD	0FFFFFF45h

.CODE
main1	PROC
		mov eax, number
		add eax, -45

		mov eax, 0
		ret
main1	ENDP

END
