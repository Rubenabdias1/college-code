; Name:			        Ruben Nunez
; Class and Section:	CS 245 01
; Assignment:		    Program Assignment 02
; Due Date:		        Monday, March 15, 2021
; Date Turned in:       Monday, March 15, 2021
; Program Description:	This program asks the user for three numbers and then add them adds them.
;						After it displays the sum, it prompts the user for a fourth number and
;						substracts it from the sum. Finally, it displays the total after the substraction.
						
.586
.MODEL FLAT

INCLUDE io.h            ; header file for input/output

.STACK 4096

.DATA
Temp	    DWORD   -1
count		BYTE	0FCh

.CODE
_MainProc PROC
		mov		eax, 0A2h
		mov		ax, 100
        
		mov		al, 64h
		mov		al, -1

		mov		eax, 1A2h
		xchg	Temp, eax

		mov		dx, 0FF75h
		xchg	dl, dh

		mov		ebx, 0FFFFFF75h
		mov		ecx, 01A2h
		sub		ebx, ecx

		mov		eax, 0FFFFFFE4h
		mov		ebx, 2h
		mul		ebx

		mov		edx, 64h
		imul	eax, edx, 10


		mov		edx, 0FFFFFFFFh
		mov		eax, 0FFFFFF9Ah
		mov		ecx, 0FFFFFFC7h
		idiv	ecx
		mov		ax, 0FF75h
		div		count

        mov     eax, 0  ; exit with return code 0
        ret
_MainProc ENDP
END                             ; end of source code

