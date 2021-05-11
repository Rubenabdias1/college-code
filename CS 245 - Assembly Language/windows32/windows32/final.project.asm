; Name:			        Ruben Nunez
; Class and Section:	CS 245 01
; Assignment:		    Program Final Project
; Due Date:		        Tuesday, May 11, 2021
; Date Turned in:       Tuesday, May 11, 2021
; Program Description:	This program asks the user for numbers until he/she inputs -9999. Then, it prints
;						the count of entries, the sum of all numbers, the average, the count of the array 
;						entries that are greater than or equal to the average value, and the difference of
;						the sums of the differences.
						
.586
.MODEL FLAT

INCLUDE io.h            ; header file for input/output

.STACK 4096

.DATA
nbrArray	DWORD	100 DUP (?)
nbrElts		DWORD	0
sentinel	DWORD	-9999
prompt1     BYTE    "Enter a number", 0
string      BYTE    40 DUP (?)
eltsLbl     BYTE    "Elements added:", 0
elts        BYTE    11 DUP (?), " elements added", 0
resultLbl   BYTE    "The sum is", 0
sum         BYTE    11 DUP (?), " total", 0
averageVal	DWORD	0
averageLbl  BYTE    "The average is", 0
average     BYTE    11 DUP (?), " average", 0
lesserLbl	BYTE    "The count of entries less than the average is", 0
lesserEntrs	BYTE    11 DUP (?), " number(s) are greater than or equal to the average", 0
dsdLbl		BYTE    "The difference of the sums of the differences is", 0
dsd			BYTE    11 DUP (?), 0

.CODE
_MainProc PROC
			mov		nbrElts, 0				; nbrElts := 0
			lea		ebx, nbrArray			; get address of array
			input   prompt1, string, 40		; prompt for and input number
			atod    string					; convert to integer
whileNEQ:	cmp		eax, sentinel			; check condition, compare the input with the sentinel value
			je		endWhileNEQ				; break if the input is -9999 (sentinel value)
body:		inc		nbrElts					; add 1 to nbrElts
			mov		DWORD PTR [ebx], eax	; store number at address
			add		ebx, 4					; add 4 to address
			input   prompt1, string, 40		; prompt for and input number
			atod    string					; convert to integer
			jmp		whileNEQ

endWhileNEQ: 
			mov		eax, 0					; accumulator for sum
			lea		ebx, nbrArray			; get address of array
			mov		ecx, nbrElts			; ecx = length of the array
			jecxz	outputSum				; continue, if there is no items, go output 0
nextElt:	add		eax, [ebx]				; add the each element to eax (sum)
			add		ebx, 4					; change address to next element
			loop	nextElt					; repeat n times | n = length of array |  until ecx is 0

outputSum:	dtoa	elts, nbrElts			; 
			output  eltsLbl, elts			; output number of elements
			dtoa	sum, eax				; 
			output	resultLbl, sum			; output sum of numbers

			cdq								; prepare for division
			idiv	nbrElts					; average = sum / number of elements | eax = eax / nbrElts
			mov		averageVal, eax			; storing the average value calculated to a more stable location in memory
			dtoa	average, eax			; 
			output	averageLbl, average		; output average
			
			mov		eax, 0					; accumulator for count of items > average
			lea		ebx, nbrArray			; get address of array
			mov		ecx, nbrElts			; ecx = length of the array
			jecxz	outputLess				; continue, output 0 if no items
			mov		edx, averageVal			; save average to a register
nextElt2:	cmp		[ebx], edx				; compare the current number being iterated over with the average
			jnge	cont1					; if number !>= average jump to get the next one
			inc		eax						; if it is then increment count
cont1:		add		ebx, 4					; ebx = next address
			loop	nextElt2				; continue n time | n = length of array
			
outputLess:	dtoa	lesserEntrs, eax		
			output	lesserLbl, lesserEntrs	; output count of the array entries that are greater than or equal to the average value

			mov		edx, 0					;
			mov		eax, 0					; accumulator for the difference of the sums of the differences 
			lea		ebx, nbrArray			; get address of array
			mov		ecx, nbrElts			; ecx = length of the array
			jecxz	outputDSD				; same thing, output if empty
nextElt3:	mov		edx, [ebx]				; edx = current item
			sub		edx, averageVal			; edx = difference
			add		eax, edx				; eax = sum of differences
			add		ebx, 4					; ebx = next address 
			loop	nextElt3				; continue n time | n = length of array
			
outputDSD:	dtoa	dsd, edx
			output	dsdLbl, dsd				; output difference of the sums of the differences

quit:		mov     eax, 0					; exit with return code 0
			ret
_MainProc ENDP
END                             ; end of source code

