.586
.MODEL FLAT

.STACK 4096

.DATA
byte1	BYTE	10110111b
byte2	BYTE	0B7h
byte3	BYTE	253

.CODE
main5	PROC
		add eax, -45

		mov eax, 0
		ret
main5	ENDP

END
