"""A little script to make pwn easier for me

Use it like:
python python-rop-template.py
python python-rop-template.py REMOTE
python python-rop-template.py GDB

If you love verbose add DEBUG flag
"""

from pwn import *

# Some data to change
file = "./bin"
host = "challs.io"
port = 1337
until = b">>> "

# Parsing args
if args['REMOTE']:
    p = remote(host, port)
else:
    p = process(file)

# Attaching if wanted
if args["GDB"]:
    gdb.attach(p)

# Payload crafting
pay = cyclic(100)

# Sending payload
p.sendlineafter(until, pay)
p.interactive()
