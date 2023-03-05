section .text
  global _start
    _start:
      ; Store the argument and the environment variable string on stack
      mov  eax, 0
      ; push eax          ; Use 0 to terminate the string

      ; For environment variable 
      push "4"
      push "=123"
      push "cccc"
      mov byte [esp+9], 0x00 ; terminated the string by a zero byte
      mov ebx, esp      ; ebx temporarily holds the address to the "cccc=1234" string

      push "8"
      push "=567"
      push "bbbb"
      mov byte [esp+9], 0x00 ; terminated the string by a zero byte
      mov ecx, esp      ; ecx temporarily holds the address to the "bbbb=5678" string

      push "4"
      push "=123"
      push "aaaa"
      mov byte [esp+9], 0x00 ; terminated the string by a zero byte
      mov edx, esp      ; edx temporarily holds the address to the "aaaa=1234" string

      push eax          ; Use 0 to terminate the string
      push ebx          ; push the address of "cccc=1234" to the stack
      push ecx          ; push the address of "bbbb=5678" to the stack
      push edx          ; push the address of "aaaa=1234" to the stack
      mov edx, esp      ; store the address of array env[] to edx before calling execve

      push eax          ; Use 0 to terminate the string
      push "//sh"
      push "/bin"
      mov  ebx, esp     ; store the address of "/bin//sh" to ebx before calling execve

      ; Construct the argument array argv[]
      push eax          ; argv[1] = 0
      push ebx          ; argv[0] points "/bin//sh"
      mov  ecx, esp     ; store the address of array argv[] to ecx before calling execve

      ; Call execve()
      mov  eax, 0     	; eax = 0x00000000
      mov  al, 0x0b     ; eax = 0x0000000b
      int  0x80