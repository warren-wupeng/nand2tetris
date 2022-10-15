
```puml
!pragma layout smetana
class Pin {
 
}
class Bit
class Bus {

    __init__(size: int)

}

class Chip {
    
    ins: tuple[PinOrBus]
    outs: tuple[PinOrBus]
    
    __init__(ins, outs)
    wire_pins(start_pins: tuple[Pin], end_pins: tuple[Pin])
    set_pins(pin)

}
```