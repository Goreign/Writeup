# escription
This program has constructed the flag using hex ascii values. Identify the flag text by disassembling the program.
You can download the file from here.

# Solution
```x86asm
(gdb) disassemble main
Dump of assembler code for function main:
   0x0000000000001169 <+0>:     endbr64 
   0x000000000000116d <+4>:     push   %rbp
   0x000000000000116e <+5>:     mov    %rsp,%rbp
   0x0000000000001171 <+8>:     sub    $0x30,%rsp
   0x0000000000001175 <+12>:    mov    %fs:0x28,%rax
   0x000000000000117e <+21>:    mov    %rax,-0x8(%rbp)
   0x0000000000001182 <+25>:    xor    %eax,%eax
   0x0000000000001184 <+27>:    movb   $0x70,-0x30(%rbp)
   0x0000000000001188 <+31>:    movb   $0x69,-0x2f(%rbp)
   0x000000000000118c <+35>:    movb   $0x63,-0x2e(%rbp)
   0x0000000000001190 <+39>:    movb   $0x6f,-0x2d(%rbp)
   0x0000000000001194 <+43>:    movb   $0x43,-0x2c(%rbp)
   0x0000000000001198 <+47>:    movb   $0x54,-0x2b(%rbp)
   0x000000000000119c <+51>:    movb   $0x46,-0x2a(%rbp)
   0x00000000000011a0 <+55>:    movb   $0x7b,-0x29(%rbp)
   0x00000000000011a4 <+59>:    movb   $0x41,-0x28(%rbp)
   0x00000000000011a8 <+63>:    movb   $0x53,-0x27(%rbp)
   0x00000000000011ac <+67>:    movb   $0x43,-0x26(%rbp)
   0x00000000000011b0 <+71>:    movb   $0x49,-0x25(%rbp)
   0x00000000000011b4 <+75>:    movb   $0x49,-0x24(%rbp)
   0x00000000000011b8 <+79>:    movb   $0x5f,-0x23(%rbp)
   0x00000000000011bc <+83>:    movb   $0x49,-0x22(%rbp)
   0x00000000000011c0 <+87>:    movb   $0x53,-0x21(%rbp)
   0x00000000000011c4 <+91>:    movb   $0x5f,-0x20(%rbp)
   0x00000000000011c8 <+95>:    movb   $0x45,-0x1f(%rbp)
   0x00000000000011cc <+99>:    movb   $0x41,-0x1e(%rbp)
   0x00000000000011d0 <+103>:   movb   $0x53,-0x1d(%rbp)
   0x00000000000011d4 <+107>:   movb   $0x59,-0x1c(%rbp)
   0x00000000000011d8 <+111>:   movb   $0x5f,-0x1b(%rbp)
   0x00000000000011dc <+115>:   movb   $0x37,-0x1a(%rbp)
   0x00000000000011e0 <+119>:   movb   $0x42,-0x19(%rbp)
   0x00000000000011e4 <+123>:   movb   $0x43,-0x18(%rbp)
   0x00000000000011e8 <+127>:   movb   $0x44,-0x17(%rbp)
--Type <RET> for more, q to quit, c to continue without paging--ret
   0x00000000000011ec <+131>:   movb   $0x39,-0x16(%rbp)
   0x00000000000011f0 <+135>:   movb   $0x37,-0x15(%rbp)
   0x00000000000011f4 <+139>:   movb   $0x31,-0x14(%rbp)
   0x00000000000011f8 <+143>:   movb   $0x44,-0x13(%rbp)
   0x00000000000011fc <+147>:   movb   $0x7d,-0x12(%rbp)
   0x0000000000001200 <+151>:   movzbl -0x30(%rbp),%eax
   0x0000000000001204 <+155>:   movsbl %al,%eax
   0x0000000000001207 <+158>:   mov    %eax,%esi
   0x0000000000001209 <+160>:   lea    0xdf4(%rip),%rdi        # 0x2004
   0x0000000000001210 <+167>:   mov    $0x0,%eax
   0x0000000000001215 <+172>:   callq  0x1070 <printf@plt>
   0x000000000000121a <+177>:   nop
   0x000000000000121b <+178>:   mov    -0x8(%rbp),%rax
   0x000000000000121f <+182>:   xor    %fs:0x28,%rax
   0x0000000000001228 <+191>:   je     0x122f <main+198>
   0x000000000000122a <+193>:   callq  0x1060 <__stack_chk_fail@plt>
   0x000000000000122f <+198>:   leaveq 
   0x0000000000001230 <+199>:   retq

(gdb) info registers rbp
rbp            0x7fffffffdd50      0x7fffffffdd50

(gdb) x/80b 0x7fffffffdd50-0x30
0x7fffffffdd20: 112     105     99      111     67      84      70      123
0x7fffffffdd28: 65      83      67      73      73      95      73      83
0x7fffffffdd30: 95      69      65      83      89      95      55      66
0x7fffffffdd38: 67      68      57      55      49      68      125     0
```

```python
s = "112     105     99      111     67      84      70      123 65      83      67      73      73      95      73      83 95      69      65      83      89      95      55      66 67      68      57      55      49      68      125"

numbers = map(int, s.split())
flag =  ''.join(chr(num) for num in numbers)
print(flag)
```
  

or
```x86asm
(gdb) x/s $rbp-0x30
```
`x`: Examine memory.  
`/s`: Display the memory as a string (stopping at the null byte \0 which marks the end of the string).