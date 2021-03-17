; Example assembly language program -- adds two numbers
; Author:  R. Detmer
; Date:    1/2008

.586
.MODEL FLAT

INCLUDE io.h            ; header file for input/output

.STACK 4096

.DATA
value1			DWORD	0FFFFFF1Ah
sum			BYTE	“The result is”, 0j
result1			BYTE	11 DUP(?), “ total”, 0

.CODE
_MainProc PROC
        dtoa	result1, value1
        ret
_MainProc ENDP
END                             ; end of source code

