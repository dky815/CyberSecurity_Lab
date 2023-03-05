## 1. Prerequisites

```
(a) Disable address space randomization
$ sudo sysctl -w kernel.randomize_va_space=
```

```
(b) Building the vulnerable C program
$ gcc -o prog -z noexecstack -fno-stack-protector prog.c
```

```
(c) Running the program
$ ./prog payload
```

## 2. Tasks

Your task is to build three ROP chains to perform specific operations. Recall that ROP chains are useful when the stack region is not executable, and thus, the attacker cannot run shellcode from the stack. In this lab, you can search for the ROP gadgets in the generated binary and its dependencies.
You should set the BUF_SIZE to be 300+x, where x is the least significant two digits in your SFU ID. If these two digits are zeros, choose the next significant two digits.

Note 1: You should not use any automation tools to generate the ROP chains, but you may use tools to search for gadgets.

Note 2: You need to explain in detail how you generate the ROP chains. Specifically, your lab report should include all steps you performed to generate the ROP chains with sufficient explanations and screenshots. For every generated chain, you need to list the gadgets you used in the right order. You also need to explicitly mention the used tools to complete the lab tasks.

Note 3: None of the generated ROP chains should include zero bytes.

### Task 1: Setting eax Value

Your task is to create a ROP chain file called chain_1 to set the eax value to 21 (0x15). Notice that you need to zero out eax first.

Note: You should not use inc eax;

### Task 2: Open a Shell

Your task is to generate a ROP chain file, called chain_2, to open a shell using the execve system call with “/bin/sh” as an argument. Recall the steps you need to perform to invoke execve:

1. ebx = address of null-terminated string
2. ecx = NULL
3. edx = NULL
4. eax = 0x0b
5. Invoke “int 0x80” or “call gs:[0x10]”

Hint: Recall that a ROP chain should not push items to the stack. So, you need to think of another segment to insert a string into without changing the stack!

### Task 3: Open a Reverse Shell (ROP + Shellcode)

Assume that the binary is running at a victim machine. Your task is to generate a payload called chain_3 to start a reverse shell at the victim machine. The reverse shell should execute from a shellcode injected to the stack. However, recall that we enabled the NX bit for the vulnerable binary!

Hint 1: You need to think of a way to bypass the NX bit using ROP. Then, the following shellcode should start the reverse shell.

Hint 2: Recall that the execution model of ROP is different from that of Shellcode. So, after the ROP chain is done, you need to find a way to move the eip to the beginning of the shellcode.

Note: To create a reverse shell, you may use an existing shellcode from online resources or other tools.

