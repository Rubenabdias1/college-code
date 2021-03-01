; Calculate the perimeter of a Rectangle

.586
.MODEL FLAT
.STACK 4096

.DATA
wide		DWORD	15
height		DWORD	27
perimeter	DWORD	?

.CODE
main		PROC
			mov eax, wide
			add eax, wide
			mov ebx, height
			add ebx, height
			add eax, ebx
			mov perimeter, eax

			mov eax, 0
			ret
main		ENDP
END