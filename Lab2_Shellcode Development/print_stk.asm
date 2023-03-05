[SECTION .text]
global _start
_start:
        mov eax, 0
        push eax        ; Use 0 to terminate the string
        
        push 0x000a0d21 ; push the string "!\r\n" to the stack
        ; equivalent to these two instructions below:
        ; sub esp, 4
        ; mov dword [esp], 0x000a0d21

        push "orld"     ; push the string "Hello, world" to the stack
        push "o, w"     ; (complete)
        push "Hell"     ; (complete)

        mov eax, 4      ; (complete) opcode for write system call
        mov ebx, 1      ; (complete) 1st arg is the fd
        mov ecx, esp    ; (complete) 2nd arg is the string address
	mov edx, 15     ; 3rd arg, len
        int 0x80        ; system call interrupt

        mov eax, 1      ; opcode for exit system call
        mov ebx, 0      ; 1st arg, exit(0)
        int 0x80        ; system call interrupt