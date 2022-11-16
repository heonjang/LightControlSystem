# Status

## Programming ESP32
Documentation showing that programming the ESP32 is successful

Basic code to set GPIO high:

![image](https://user-images.githubusercontent.com/55333859/202197368-2d39889b-c48e-42eb-8fbd-62e302d5ee30.png)

Programming:

![image](https://user-images.githubusercontent.com/55333859/202197114-ef0092f9-4222-4b7a-998e-e00d5c758c4c.png)

Multimeter:

https://user-images.githubusercontent.com/55333859/202198211-4a3e22c2-7931-42b0-9b6e-c7e3e2347f74.MOV

To program the ESP32:

![image](https://user-images.githubusercontent.com/55333859/202200597-8dd7393b-fa0b-4377-b840-20a1ca08dbae.png)


1. Set upload speed to 115200 and flash frequency to 80MHz
2. Connect the USB to serial converter to the UART wires (careful not to connect 5V or the board will fry)
3. Hold the Reset and Boot buttons together
4. Press the upload code button on the Arduino IDE while still holding both buttons
5. Once "uploading" pops up on the terminal release the Reset button
6. Once "connectinng" displays on the terminal release the Boot button
7. It may be necessary to reset the board after uploading code

