# Todo Update

## Components

### Connectors

Using 01x08 connectors (WM17450-ND but schematic / footprint is TSW-104-07-S-D-LL due to SNAPEDA not having desired schematic / footprint. Is twice cheaper) for J1&J3, J2&J4 (UART and JTAG to program ESP32)
Also using the same connector for J5 and J7 (Photosensor and Motor)

Using 01x16 connectors (WM17462-ND but schematic / footprint is TSW-108-01-L-DV-M-TR due to SNAPEDA not having desired schematic / footprint. Is 30 cents cheaper) for LED modules. 

### Barrel Jack


### Switches

Using TL3305AF160QG for all 4 switches

### Wall Adapter

The main problem with the adapters is price. A simple search in digikeys for AC/DC wall adapters at 120W minimum gives us a minimum price of $68 (https://www.digikey.com/en/products/filter/ac-dc-desktop-wall-adapters/130?s=N4IgjCBcoExgHAdiqADgFyiAqgOwJboDyAZgLICmAhgM4CuAThSADQh1YDqrIAtvrixgYABhABfcWwBsKEPgAmWALQAWHhiw90AT1TNIIWgGMJ4oA)
I am not entirely sure how we would go about resovling this issue (maybe some implementation of amplifiers??)

### Motor Driver

Double checked, in the video 5V is for their microcontroller, A4988 operates between 3-5.5V, so can operate with both 3.3 or 5. In the video, they operate it with 3.3V.

## Others

Based on my calculations, 3.3V provides enough power to circuit (in safe range, below 80%)
