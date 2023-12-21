// pop this 2
// addr = this + 2
  @2
  D=A
  @this
  D=D+M
  @addr
  M=D
// SP--
  @SP
  M=M-1
// RAM[addr]=RAM[SP]
  A=M
  D=M
  @addr
  A=M
  M=D
