; Name:						Ruben Nunez
; Class and Section:		CS 245 01
; Assignment:				Programming Assignment Additional Chapter 04
; Due Date : 				Wednesday, April 21, 2021 
; Date Turned in :			Wednesday, April 21, 2021 
; Program Description :		On Monday at the county fair, Jared played a game and won 75 
;							tickets. On Tuesday, he won 105 tickets; on Wednesday, he won
;							127 tickets, but then spent 250 of them on a prize. This program
;							outputs how many more tickets does Jared need to win to get a 
;							prize that costs 150 tickets. 

.586
.MODEL FLAT

INCLUDE io.h; header file for input / output

.STACK 4096

.DATA
mondayWin	DWORD	150
tuesdayWin	DWORD	75
wedWin	    DWORD	127
spent	    DWORD	250
available	DWORD	?
helloLabel  BYTE    "Fair Tickets", 0
prompt1     BYTE    "Jared needs:", 0
neededLbl  	BYTE    "Jared needs:", 0
needed    	BYTE    11 DUP(? ), " dollars", 0

.CODE
_MainProc	PROC
        	output  helloLabel, prompt1     ; output starting prompt
            mov     eax, mondayWin			
            add     eax, tuesdayWin
            add     eax, wedWin             ; eax has the total tickets earned
            
			sub		eax, spent				; eax = the balance after spending 250 tickets
			mov		available, eax
			mov		eax, 150				; eax = 150 needed to buy the prize
			sub		eax, available			; eax = 150 - available = needed money to buy
			dtoa    needed, eax				; convert to ASCII characters
			
			output  neededLbl, needed 		; output result

			mov     eax, 0					; exit with return code 0
			ret
_MainProc 	ENDP
END											; end of source code

