; Name:						Ruben Nunez
; Class and Section:		CS 245 01
; Assignment:				Programming Assignment Additional Chapter 04
; Due Date : 				Wednesday, April 21, 2021 
; Date Turned in :			Wednesday, April 21, 2021 
; Program Description :		$5,876 are distributed equally among 26 men. 
;							This program outputs how much money each person will get.

.586
.MODEL FLAT

INCLUDE io.h; header file for input / output

.STACK 4096

.DATA
money		DWORD	5876
people		DWORD	26
helloLabel  BYTE    "Distributing Money", 0
prompt1     BYTE    "Each person will get:", 0
eachLbl  	BYTE    "Dollars per person", 0
perPerson	BYTE    11 DUP(? ), " dollars/person", 0

.CODE
_MainProc	PROC
        	output  helloLabel, prompt1     ; output label and sum
            mov     eax, money				; eax = money to be distributed = 5876
			mov 	edx, 0					; emptying edx for division
			idiv	people					; eax = money to be distributed / amount of people = 5876 / 26
			dtoa    perPerson, eax			; convert to ASCII characters
			
			output  eachLbl, perPerson 		; output result

			mov     eax, 0					; exit with return code 0
			ret
_MainProc 	ENDP
END											; end of source code

