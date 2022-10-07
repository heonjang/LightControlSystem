## Design

### Relays to Transistors

The decision to use LEDs allows for lower voltage options to switch lights on and off. The most cost effective and reliable option being transistors.
Mainly switching the transistor from saturation (on) to cutoff (off) will achieve the desired results.

#### Simulations / Proof of Concept
Below is the IV curve for a transistor. When saturated, the maximum current will flow. 
In this project's design, this maximum current will correspond to the current through the LED which has been adjusted with resistors.
In cutoff, I_C will be 0, and the LED will be switched off.

![image](https://user-images.githubusercontent.com/55333859/194380885-5f858004-563a-45f3-9f11-a8600dd6bacb.png)

Wurth Electronics provided a [library](https://www.we-online.com/catalog/en/WL-SMTW) defining model parameters for the Blue LED from the grow modules : 
- IS=48.651E-12
- N=4.7513
- RS=1.1837
- IKF=431.41E-6
- CJO=1.0000E-12
- M=.3333
- VJ=.75
- BV=5
- IBV=10.00E-6
- TT=5.0000E-9

Following these paramaters, the behavior of the Blue LED was simulated in LTSpice and an IV curve was obtained

![image](https://user-images.githubusercontent.com/55333859/194476189-213e18ab-9975-4ca8-8a38-540a1433708b.png)

The simulated IV curve is shown below

![image](https://user-images.githubusercontent.com/55333859/194475654-b6af6257-5bfa-4aec-ba8f-2c883e02cc79.png)

The actual IV curve taken from the [datasheet](https://www.we-online.com/catalog/datasheet/150141BS73130.pdf) is shown below

![image](https://user-images.githubusercontent.com/55333859/194469670-997eb19c-9e39-4dbe-bd8a-044473470bd9.png)

The Base−Emitter Saturation voltage for the transistor has a minimum of 0.6V and maximum of 1.2V.
The minimum V_high of the GPIO pins of the microcontroller is 2.64V, and typically will be below 3.3V.
As such, the design aims for a voltage drop of 2V across the resistor to the base of the NPN transistor.

Referring to the desired LED currents as described [here](https://github.com/heonjang/LightControlSystem/blob/main/October%205th.md) and 
beta being 100, the following values were calculated

| LED      | I_C | I_B | Corresponding Resistor |
| ----------- | ----------- |  ----------- |  ----------- |  
| UV |   17mA | 0.17mA | 12kΩ|  
| Blue |  29mA |  0.29mA| 6.9kΩ |
| Yellow-Red | 19.3mA |  0.193mA|  10.4kΩ |  
| Green | 127mA |  1.27mA|  1.57kΩ | 

The circuit was designed and simulated in LTSpice. The transistor remains biased in cutoff mode until it receives a high signal from the
microcontroller. At which point, the transistor is saturation and the LED is switched on.

![image](https://user-images.githubusercontent.com/55333859/194475987-7121675b-d698-4ae9-ad58-abbc0cacd6d9.png)
![image](https://user-images.githubusercontent.com/55333859/194475904-6f15ac96-71a9-4022-bb3b-62e2ac78d36c.png)

From these simulations, the transistor will function properly as a switch. The modeled circuit was based on ideal components matching the 
desired properties exactly. Resistors will be selected to match the resistances as closely as possible. This will be covered in the following section.

### Grow Light Design Update
The 2N2222 NPN transistor used in simulation has a surface mount equivalent, the MMBT2222AM3T5G that will be used. Some of the resistor values are not typical, as such, the following resistors were selected.
