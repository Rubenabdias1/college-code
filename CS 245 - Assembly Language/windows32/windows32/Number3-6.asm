; Name:						Ruben Nunez
; Class and Section:		CS 245 01
; Assignment:				Programming Assignment Additional Chapter 04
; Due Date : 				Wednesday, April 21, 2021 
; Date Turned in :			Wednesday, April 21, 2021 
; Program Description :		89 people have been invited to a banquet. The caterer is arranging tables. 
;							Each table can seat 12 people. This program outputs how many tables are needed.

.586
.MODEL FLAT

INCLUDE io.h; header file for input / output

.STACK 4096

.DATA
people		DWORD	89
tCapacity	DWORD	12
helloLabel  BYTE    "Table Arrangement", 0
prompt1     BYTE    "Tables needed:", 0
tablesLbl  	BYTE    "Tables needed", 0
tables		BYTE    11 DUP(? ), " tables", 0

.CODE
_MainProc	PROC
        	output  helloLabel, prompt1     ; output label and sum
            mov     eax, people				; eax = people = 89
			mov 	edx, 0					; empty edx for division
			idiv	tCapacity				; eax = people / table capacity = 89 / 12
			inc		eax						; increasing eax to seat remainder of people
			dtoa    tables, eax				; convert to ASCII characters
			
			output  tablesLbl, tables 		; output result

			mov     eax, 0					; exit with return code 0
			ret
_MainProc 	ENDP
END											; end of source code

