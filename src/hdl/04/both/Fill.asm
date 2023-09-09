// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.
// LOOP1:
(LOOP)
// i = 0
@i
M=0

@8192
D=A
@c
M=D
//   if (KBD > 0): goto black
@KBD
D=M

@BLACK
D;JGT


(WHITE)
//   if i = 8192: goto LOOP
@i
D=M
@c
D=D-M
@LOOP
D;JEQ

//   RAM[SCREEN+i] = color
@i
D=M
@SCREEN
A=A+D
M=0

// i = i + 1
@i
M=M+1

// goto LW
@WHITE
0;JMP

(BLACK)
//   if i = 8191: goto LOOP
@i
D=M
@c
D=D-M
@LOOP
D;JEQ

//   RAM[SCREEN+i] = color
@i
D=M
@SCREEN
A=A+D
M=-1

// i = i + 1
@i
M=M+1

// goto LW
@BLACK
0;JMP

