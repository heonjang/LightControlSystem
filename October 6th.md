## Design

#### Relays to Transistors

The decision to use LEDs allows for lower voltage options to switch lights on and off. The most cost effective and reliable option being transistors.
Mainly switching the transistor from saturation (on) to cutoff (off) will achieve the desired results.

![image](https://user-images.githubusercontent.com/55333859/194380885-5f858004-563a-45f3-9f11-a8600dd6bacb.png)

![image](https://user-images.githubusercontent.com/55333859/194440451-07d14b07-0c53-4258-8596-1031ad2374b0.png)

![image](https://user-images.githubusercontent.com/55333859/194440346-0d90a380-8ebf-44c0-81f7-620ca4dfba6b.png)


The Base−Emitter Saturation voltage for the transistor has a minimum of 0.6V and maximum of 1.2V.
The minimum V_high of the GPIO pins of the microcontroller is 2.64V, and typically will be below 3.3V.
As such, the design aims for a voltage drop of 2V across the resistor to the base of the NPN transistor.

Referring to the desired LED currents as described [here](https://github.com/heonjang/LightControlSystem/blob/main/October%205th.md) and 
beta being 100, the following values were calculated

| LED      | I_C | I_B | Corresponding Resistor |Final Resistor Choice |
| ----------- | ----------- |  ----------- |  ----------- |  ----------- | 
| UV |   17mA | 0.17mA | 12Ω|  |
| Blue |  29mA |  0.29mA| 6.9kΩ ||
| Yellow-Red | 19.3mA |  0.193mA|  10.4kΩ ohms |  |
| Green | 127mA |  1.27mA|  1.57kΩ | |
