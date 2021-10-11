; Name:			        Ruben Nunez
; Class and Section:	CS 245 01
; Assignment:		    Extra Credit Program Assignment 04
; Due Date:		        Monday, April 12, 2021
; Date Turned in:       Monday, April 12, 2021
; Program Description:	This program asks the user for the length, width and 
;						height of a box and computes and displays its volume.

.586
.MODEL FLAT

INCLUDE io.h            ; header file for input/output

.STACK 4096

.DATA
len         DWORD   ?
wid         DWORD   ?
height      DWORD   ?
prompt1     BYTE    "Enter the lenght", 0
prompt2     BYTE    "Enter the width", 0
prompt3     BYTE    "Enter the height", 0
string      BYTE    40 DUP (?)
resultLbl   BYTE    "The volume is", 0
result      BYTE    11 DUP (?), " total", 0

.CODE
_MainProc PROC
        input   prompt1, string, 40		; read ASCII characters
        atod    string					; convert to integer
        mov     len, eax			    ; store in memory

        input   prompt2, string, 40     ; repeat for width
        atod    string
        mov     wid, eax

        input   prompt3, string, 40     ; repeat for height
        atod    string
        mov     height, eax
       
        mov     eax, len			    ; length to EAX
        mov     ebx, wid			    ; width to EBX
        mul     ebx			            ; length * width
		mov		ebx, height			    ; height to ebx
        mul     ebx	                    ; length * width * height
        dtoa    result, eax				; convert to ASCII characters
        output  resultLbl, result       ; output label and sum

        mov     eax, 0					; exit with return code 0
        ret
_MainProc ENDP
END										; end of source code

