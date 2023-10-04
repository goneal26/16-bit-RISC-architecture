; swap contents of RAM[0] and RAM[1]
mvi r0 0;
load r2 r0; put RAM[0] into r2
mvi r1 1;
load r3 r1; put RAM[1] into r3
store r3 r0; store RAM[1] to RAM[0]
store r2 r1; store RAM[0] to RAM[1]