[SECTION .text]
global _start
_start:
        jmp saveme    ; (complete) jmp to saveme
shellcode:
        pop esi       ; (complete) esi now holds address of msg
        mov eax, 4    ; (complete) opcode for write system call
        mov ebx, 1    ; (complete) 1st arg is the fd
        mov ecx, esi  ; (complete) 2nd arg is the string address
        mov edx, 15   ; 3rd arg is len
        int 0x80      ; system call interrupt

        mov eax, 1    ; opcode for exit system call
        mov ebx, 0    ; 1st arg, exit(0)
        int 0x80      ; system call interrupt
 saveme:
        call shellcode; (complete) call shellcode
        msg db "Hello, world!", 0xA, 0xD