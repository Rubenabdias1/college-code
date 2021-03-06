; Name:			Ruben Nunez
; Class and Section:	CS 245 01
; Assignment:		Program Assignment 01
; Due Date:		Wednesday, March 3, 2021
; Date Turned in:	Wednesday, March 3, 2021
; Program Description:	This program adds numbers -105 and 158 together and save the result in a location identified by sum. 
;			Finally, it will subtract 1000 from the sum and will save the result in a location identified by diff.

.586
.MODEL FLAT

.STACK 4096

.DATA
number1		DWORD	-105
number2		DWORD	158
sum			DWORD	?
diff		DWORD	?


.CODE
main233		PROC
			;number1	number2		sum			diff		eax
			;FFFF FF97	0000 009E	0000 0000	0000 0000	undefined (random)
			
			mov eax, number1	; copies the value located at memory location identified by number1 in the register eax
			;number1	number2		sum			diff		eax
			;FFFF FF97	0000 009E	0000 0000	0000 0000	FFFF FF97
			
			add eax, number2	; The value located at memory location identified by number2 is added to eax. The result is now stored in eax.
			;number1	number2		sum			diff		eax
			;FFFF FF97	0000 009E	0000 0000	0000 0000	0000 0035
			; Flags:	CF = 1 (There was a carry)
			;		ZF = 0 (The result is not 0)
			;		SF = 0 (The result is unsigned/positive)
			;		OF = 0 (There was no overflow)
			mov sum, eax		; The value located in eax is copied in the memory location identified by sum.
			;number1	number2		sum			diff		eax
			;FFFF FF97	0000 009E	0000 0035	0000 0000	0000 0035

			add eax, -1000		; The value -1000 (FFFF FC18) is added to the value stored in eax. The result gets assigned to eax.
			;number1	number2		sum			diff		eax
			;FFFF FF97	0000 009E	0000 0035	0000 0000	FFFF FC4D
			; Flags:	CF = 0 (There was a carry)
			;		ZF = 0 (The result is not 0)
			;		SF = 1 (The result is signed/negative)
			;		OF = 0 (There was no overflow)
			mov diff, eax		; The value stored in eax is copied into the memory location identified by diff.
			;number1	number2		sum			diff		eax
			;FFFF FF97	0000 009E	0000 0035	FFFF FC4D	FFFF FC4D

			mov eax, 0			; Eax gets cleaned up by copying the value 0000 0000 into it.
			;number1	number2		sum			diff		eax
			;FFFF FF97	0000 009E	0000 0035	FFFF FC4D	0000 0000

			ret					; Returns from the procedure.
main233		ENDP

END
