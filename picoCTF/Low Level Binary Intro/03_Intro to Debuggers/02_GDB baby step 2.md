# Description
Can you figure out what is in the eax register at the end of the main function? Put your answer in the picoCTF flag format: picoCTF{n} where n is the contents of the eax register in the decimal number base. If the answer was 0x11 your flag would be picoCTF{17}.
Debug this.

# Solution
1. Download the artifact from the next challenge.
2. Disassemble it like you did for the previous challenge.
3. Statically analyze it; read it, try to understand what is happening.  
   
Notice how the code jumps backwards! The same block of code is executed multiple times. This is how a loop looks in assembly language. To statically figure out what is in `eax` at `main+56` we’d have to precisely calculate how many times this loop runs. This is possible, but in this case, we can easily set a breakpoint to pause program execution after the loop. To set a breakpoint and examine `eax`, follow these steps:

1. `(gdb) break *main+59` This sets a breakpoint at the instruction immediately after the one in question. This guarantees that the instruction in question has actually been executed.
2. `(gdb) run` This lets the program run until it tries to execute the instruction at our breakpoint.
3. `(gdb) info registers eax` This prints out our answer in hexadecimal and decimal.