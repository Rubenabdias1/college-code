.586
.MODEL FLAT
.STACK 4096

.DATA
nbrArray	DWORD	25,47,15,50,32,95 DUP (?)
nbrElts		DWORD	5

.CODE
main		PROC
			mov		eax,			0			; sum = 0
			lea		ebx,			nbrArray	; get address of nbrArray
			mov		ecx,			nbrElts		; count = nbrElts
			jecxz	quit						; quit if no numbers
forCount1:	add		eax,			[ebx]		; add number to sum
			add		ebx,			4			; get address of next element
			loop	forCount1					; repeat nbrElts times

			cdq									; extend sum to quadword
			idiv	nbrElts						; divide sum by nbr elements

			lea		ebx, 			nbrArray	; 
			mov		ecx, 			nbrElts		;
forCount2:	cmp		[ebx],			eax			;
			jnl		endIfSmall
			add		DWORD PTR [EBX],10
endIfSmall:	
			add		ebx,			4
			loop	forCount2

quit:		mov		eax,			0
			ret
main		ENDP
END