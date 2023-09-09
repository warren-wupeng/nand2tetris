// pop argument 2
// addr = argument + 2
  @2
  D=A
  @local
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
