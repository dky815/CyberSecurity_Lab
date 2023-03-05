section .text
  global _start
    _start:
      ; Store the argument string on stack
      mov  eax, 0
      ; push eax          ; Use 0 to terminate the string
      push "/sh"
      push "/bin"
      mov ebx, esp      ; ebx temporarily holds the address to the "/bin/sh" string      
                        ; store the address of "/bin/sh" to ebx before calling execve
      mov byte [ebx+7], 0x00  ; terminated the string by a zero byte

      push "-c"
      mov ecx, esp      ; ecx temporarily holds the address to the "-c" string
      mov byte [ecx+2], 0x00  ; terminated the string by a zero byte

      push "la"
      push "ls -"
      mov edx, esp      ; edx temporarily holds the address to the "ls -la" string
      mov byte [edx+6], 0x00  ; terminated the string by a zero byte

      ; Construct the argument array argv[]
      push eax          ; argv[3] = 0
      push edx          ; argv[2] points "ls -la"
      push ecx          ; argv[1] points "-c"
      push ebx          ; argv[0] points "/bin/sh"
      
      mov  ecx, esp     ; store the address of the array argv[] to ecx before calling execve

      ; For environment variable 
      mov edx, 0        ; No env variables 

      ; Call execve()
      mov  eax, 0     	; eax = 0x00000000
      mov  al, 0x0b     ; eax = 0x0000000b
      int  0x80