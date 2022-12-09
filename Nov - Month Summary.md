# Design Updates

## Microcontroller
The microcontroller acts as a wireless access point. Mainly, any device, (phone or computer) can connect to the ESP32 access point.
Once, connected, redirecting to the website 192.168.4.1 will display the current photosensor reading. The LED modules can then be switched on and off,
by redirecting to 192.168.4.1/Module{#}_{ON or OFF}.
  
Our second ESP32 chip was unfortunately fried while soldering, which led to the temporary replacement by an Arduino development board.
  

## Power
 To power the LEDs, a 12V, 135W ACDC converter was used. This more than supplies enough power, even if more LED modules were potentially added in the
 future. Due to time limitations, the ESP32 was powered from the lab's power supply for the demo. However, this should be replaced by either a step down 
 voltage circuit (from 12V to 3.3V), or buying an additional wall adapter.
   
 ## Packaging
 An LED panel frame was constructed to house the LEDs. Unfortunately, there were still some drill holes that should be included in the design so as to 
 be able to properly hide the wires. Additionally, a mounting system or hanging system should be added to the design.
  
  
