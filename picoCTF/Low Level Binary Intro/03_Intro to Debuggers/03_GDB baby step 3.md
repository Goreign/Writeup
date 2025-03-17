# Description
Now for something a little different. 0x2262c96b is loaded into memory in the main function. Examine byte-wise the memory that the constant is loaded in by using the GDB command x/4xb addr. The flag is the four bytes as they are stored in memory. If you find the bytes 0x11 0x22 0x33 0x44 in the memory location, your flag would be: picoCTF{0x11223344}.
Debug this.

# Solution
```x86asm
(gdb) disassemble main
Dump of assembler code for function main:
   0x0000000000401106 <+0>:     endbr64 
   0x000000000040110a <+4>:     push   %rbp
   0x000000000040110b <+5>:     mov    %rsp,%rbp
   0x000000000040110e <+8>:     mov    %edi,-0x14(%rbp)
   0x0000000000401111 <+11>:    mov    %rsi,-0x20(%rbp)
   0x0000000000401115 <+15>:    movl   $0x2262c96b,-0x4(%rbp)
   0x000000000040111c <+22>:    mov    -0x4(%rbp),%eax
   0x000000000040111f <+25>:    pop    %rbp
   0x0000000000401120 <+26>:    retq   
End of assembler dump.

(gdb) x/4xb 0x0000000000401118
0x401118 <main+18>:     0x6b    0xc9    0x62    0x22
```
{0x6bc96222}