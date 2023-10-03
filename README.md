# 16-bit-RISC-architecture
*A homebrew 16 bit RISC processor.*

This is my design for my own homebrew 16-bit RISC machine, inspired by the Amiga 500, the nand2tetris HACK computer,
and the IJERT 'Design of a 16-bit RISC Processor' paper.

## Specifications
This computer will use 16-bit words for all data. It will allow for a RAM and ROM capacity of 65,536 16-bit words.
The computer will contain 64 registers (each being one word long) for modifying and manipulating data:
(in progress)

## Machine Language and Assembly
The machine language consists of 16-bit instruction words that appear as follows:
```
o1 o2 o3 o4  d1 d2 d3 d4  d5 d6 s1 s2  s3 s4 s5 s6
```
Where:
- o1-o4 refers to the opcode
- d1-d6 refers to the destination register for computation (referred to below as ry)
- s1-s6 refers to one register operand of a computation (referred to below as rx)

The opcodes consist of the following instructions (indexed by decimal opcode value):
0) HALT: stops the program clock
1) ADD: ry = ry + rx
2) SUB: ry = ry - rx
3) MUL: ry = ry * rx
4) AND: ry = ry & rx
5) OR: ry = ry | rx
6) XOR: ry = ry ^ rx
7) NOT: ry = ~rx
8) SHL: ry = rx << 1
9) SHR: ry = rx >> 1 (arithmetic right shift) <!-- or should i use logical right shift? -->
10) CPY: ry = rx
11) MVI: ry = number between 0 and 63
12) LOAD: ry = RAM[rx]
13) STORE: RAM[rx] = ry
14) JUMP: unconditionally set program counter to ry <!-- may change because then im not using s1-s6 -->
15) JZRO: set program counter to ry if rx = 0

## Progress
- [x] Machine Language Specification
- [x] Assembly Language Specification
- [ ] Assembler
- [ ] Emulator
- [ ] Compiled Language
- [ ] Logisim Evolution simulation
(more to be planned later)
