# Christelle Worklog
1. [Christelle Worklog](https://github.com/heonjang/LightControlSystem/edit/Christelle/README.md#christelle-worklog)
2. [2022_09_20 - Changes (UV Lights I)](https://github.com/heonjang/LightControlSystem/edit/Christelle/README.md#2022_09_20---changes)
3. [2022_09_27 - General Changes (UV Lights II)](https://github.com/heonjang/LightControlSystem/edit/Christelle/README.md#2022_09_27---general-changes)
4. [2022_09_28 - Safety](https://github.com/heonjang/LightControlSystem/edit/Christelle/README.md#2022_09_28---safety)
5. [2022_09_29 - LED Choice](https://github.com/heonjang/LightControlSystem/edit/Christelle/README.md#2022_09_29---led-choice)
6. [2022_10_02 - Light Intensity](https://github.com/heonjang/LightControlSystem/edit/Christelle/README.md#2022_10_02---light-intensity)
7. [2022_10_03 - Design Analysis](https://github.com/heonjang/LightControlSystem/edit/Christelle/README.md#2022_10_03---design-analysis)
8. [2022_10_05 - LED Changes](https://github.com/heonjang/LightControlSystem/edit/Christelle/README.md#2022_10_05---led-changes)
9. [2022_10_06 - Transistors](https://github.com/heonjang/LightControlSystem/edit/Christelle/README.md#2022_10_06---transistors)
10. [2022_10_07 - General](https://github.com/heonjang/LightControlSystem/edit/Christelle/README.md#2022_10_07---general)
11. [2022_10_08 - Light Intensity II](https://github.com/heonjang/LightControlSystem/edit/Christelle/README.md#2022_10_08---light-intensity-ii)




## 2022_09_20 - Changes

### UV Lights
Due to a lack of available adjustable UV lights, the project will now have 6 individual 5W UV light bulbs.
These will be switched on and off accordingly to adjust the light to the plant.
The microcontroller will control how many of these bulbs are turned on at a time by flipping switches.

### Powering Considerations
The ESP32's consume non-negligible amounts of power. As a result, instead of 3 ESP32's, our design will only have 2.
The light sensor will be connected to the same ESP32 as the UV lights to cut down on power consumption.

## 2022_09_27 - General Changes

#### UV Lights
The design will use srd-05vdc-sl-c relays to switch on and off the lights. These are 5V relays, so the output from the micrcontroller 
will be stepped up from 3.3 to 5V using the L6920DC converter. After a conversation with Jack Belvins, a UIUC alum, the circuit for the UV
lights will be isolated on its own board. Additionally, an emergency shutoff will be implemented. As safety is paramount in this project, 
surge protection will be added to the design.

### Design Details
Currently the following topics are still in progress and require further discussion and thought

#### Safety
- The UV lights are hot, a method of preventing consumers from touching the light bulbs directly should be added
- The potential for fire is a concern. Surge protection would prevent fires. Ensuring the design doesn't overload the power source is crucial as well.

#### Power
- Wall outlets will be used to power the design. The current design has two major power systems, calculations on the load on these systems still needs
to be done


### Next Steps
Schematics will need to be updated and finished relatively soon. Additional research will be done to decide the best UV lights for the design.

## 2022_09_28 - Safety

### Safety Updates

#### Emergency Shutoff
One of the main concerns of this project is the potential for safety failures. Primarily, it is a concern that the lights might possibly overheat and start a fire.
As such, an emergency shutoff is implemented. This will be a dual sided approach: both through software as well as hardware.


For the hardware implementation, a relay circuit will be implemented so that the power to the UV light circuit is usually on. 
The application will have an emergency shutoff setting, which when selected, the app will send a signal to the UV light microcontroller
to switch off the relay and power to the UV light circuit. Additionally, as another failsafe, there will be a manual switch ([RE111C1021-116](https://www.digikey.com/en/products/detail/e-switch/RE111C1021-116/4331944))
) which when pressed will shut down the
entire UV light circuit.

The circuit will be powered using an 311013-01 plug which connect to both the relay and switch.

## 2022_09_29 - LED Choice

###  LED Component Selection (Preliminary)

UVA LED: [XZVS54S-9C](https://www.digikey.com/en/products/detail/sunled/XZVS54S-9C/9920862)
3.3 V Forward
1.5A

Blue LED: [XQABLU-02-0000-000000U01](https://www.digikey.com/en/products/detail/creeled-inc/XPCBLU-L1-0000-00W01/2442517)
3.3 V Forward

Yellow-Red: [710-150080SG54050](https://www.mouser.com/ProductDetail/Wurth-Elektronik/150080SG54050?qs=sGAEpiMZZMusoohG2hS%252B13XB79dZiCCbHkvBdSuOsbMbCoO%2FAYKQfw%3D%3D)
3.3V 20mA

Green [AA3528ZGSK](https://www.mouser.com/ProductDetail/Kingbright/AA3528ZGSK?qs=sGAEpiMZZMusoohG2hS%252B10BkqeXx1odDDXmYTeDmVc3Gq1YsCYNLGQ%3D%3D)
3.3V 20mA

## 2022_10_02 - Light Intensity

### Light Intensity Objectives
The protoype will be designed to provide light for various types of plants: low, medium and high-light plants.

To best accomodate as many types of plants as possible, the design should produce 1,000+ foot-candles of light.

| Type      | Lumens |
| ----------- | ----------- |
| Low-light plants  | 50 and 250 foot-candles     |
| Medium-light plants   | 250 to 1,000 foot-candles (Best above 750 foot-candles)   |
| High-light plants   | 1,000 foot-candles mininmum|

Information summarized from _[Lighting Indoor Houseplants](https://extension.missouri.edu/publications/g6515)_

As described in the design document, there will be a number of grow light modules. These grow light modules are sets of 4 different types of LEDs: blue, 
red, green, and UVA leds as a combination of these was determined to provide optimal wavelengths of light for plant growth.

Referring to the datasheets each of the LEDs will provide the following light intensity:

|LED | Intensity  | Viewing Angle | |
| ----------- | ----------- | ----------- | ----------- |
| UVA  |  40mcd| 30 degrees| |
| [Blue](https://www.we-online.com/catalog/datasheet/150141BS73140.pdf)| --- | 125 degrees|27 lm |
| Yellow-Red  | 100mcd| 130 degrees| |
| Green  | 500mcd | 120 degrees| |

* The UVA LED used is changed to [MT0380-UV-A](https://www.digikey.com/en/products/detail/marktech-optoelectronics/MT0380-UV-A/4214613)

## 2022_10_03 - Design Analysis

### Design Limitations and Considerations

One of the current limitations the prototype faces is price. Mainly, the number of grow light modules is limited by their cost. 

One module based on the circuit from the design document costs $6.37. The most costly components being the UV LED at 2.77, the relays at 1.26 and the 
Blue LED at 1.10.

As identified in the journal entry from [October 2nd](https://github.com/heonjang/LightControlSystem/blob/Christelle/October/2022_10_02%20-%20Light%20Intensity.md), 1000+ foot-candles of light or 10,0000 lumens should be provided to accomodate High-light plants. 10,000 Lumens is a substantial amount of light.
Due to budget limitations, it is not feasible to expect to provide 10000 lumens reliably. As such our prototype will be specifically for low and medium light plants. 

## 2022_10_05 - LED Changes

### Cost Reduction
To bring down the costs of the grow light module, cheaper components are reselected as shown below: 

| LED      | Cost | Intensity | Comments |
| ----------- | ----------- |  ----------- |  ----------- |
| [UV](https://www.mouser.com/ProductDetail/Kingbright/AA3528VRVFS-A?qs=rY7msk5yxfb63mh907EyRA%3D%3D) (315-400 nm)     | $0.67      |  250mcd |  ----------- |
| [Blue](https://www.digikey.com/en/products/detail/w%C3%BCrth-elektronik/150141BS73130/13584853) (440-500 nm) | $0.40 |  1000mcd (max) |  decently high mcd rating, to avoid burn out might opt for lower intensity |
| [Yellow-Red](https://www.digikey.com/en/products/detail/vishay-semiconductor-opto-division/VLMO233U1AA-GS08/3025492) (610-700 nm)  | $0.51        |  760mcd |  ----------- |
| [Green](https://www.digikey.com/en/products/detail/creeled-inc/XQAGRN-02-0000-000000Z01/5761845) (510-610 nm) | $0.60        |  64lm/W |  Viewing angle is 110, min PPF of 0.48, no units in mcd |
| **Total**  | $2.18        |  ----------- |  ----------- |


### Addons to Design
To accomodate these LEDs, 5V will be provided to each module instead of 3.3V

| LED      | V_on | Desired I | Corresponding Resistor |Final Resistor Choice |Cost |
| ----------- | ----------- |  ----------- |  ----------- |----------- | ----------- |
| UV | 3.3V |  20mA |  85 ohms | [100 ohm](https://www.digikey.com/en/products/detail/stackpole-electronics-inc/RMCF1210JT100R/1757185) | $0.11 |
| Blue | 3.2V |  30mA |  60 ohms | [62 ohm](https://www.digikey.com/en/products/detail/stackpole-electronics-inc/RMCF1210JT62R0/1757232) |$0.11|
| Yellow-Red | 2.1V |  20mA |  145 ohms | [150 ohms](https://www.digikey.com/en/products/detail/stackpole-electronics-inc/RMCF0805FT150R/1760641) |$0.10 |
| Green | 3.1V |  175mA |  10 ohms| [15 ohms](https://www.digikey.com/en/products/detail/stackpole-electronics-inc/RMCF2512JT15R0/1716289) | $0.28 |
| **Total** | ----------- |  ----------- |  ----------- |----------- | $0.60 |

Took Desired_I values from graphs of datasheet with relative luminosity intensity vs Forward Current and chose values of forward current at 1 relative luminosity intensity.

When choosing resistor values, just to ensure LED life, we purposefully chose higher resistor values so that current going through the LEDs will be smaller.

Things to consider in future: Green LED seem to be much brither than its counterpart. Might want to adjust the number of LEDs so that one wavelength is not dominant, thus minimizing the growth effects that each wavelenghts have on plants.


**_This notebook entry was a joint effort between Sungjoo and Christelle_**

## 2022_10_06 - Transistors

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

#### Grow Light Design Update
The 2N2222 NPN transistor used in simulation has a surface mount equivalent, the MMBT2222AM3T5G that will be used. Some of the resistor values are not typical, as such, the following components were selected.
| Component      |Quantity |Price|Comment|
| ----------- | ----------- |  ----------- |   ----------- |  
| [NPN transistors](https://www.digikey.com/en/products/detail/onsemi/MMBT2222AM3T5G/2050501) |4 |    $0.23| Transistors for switching |
| [12kΩ resistor](https://www.digikey.com/en/products/detail/te-connectivity-passive-product/CRGCQ0603F12K/8576303) | 1 |   $0.10 |  Resistor for switching UV LED  |  
| [6.98kΩ resistor](https://www.digikey.com/en/products/detail/stackpole-electronics-inc/RMCF0402FT6K98/1761682) | 1|  $0.10 |  Resistor for switching blue LED |  
| [10.5kΩ resistor](https://www.digikey.com/en/products/detail/panasonic-electronic-components/ERJ-1GNF1052C/2036228) | 1 |  $0.10 |  Resistor for switching yellow-red LED |  
|[1.58kΩ resistor](https://www.digikey.com/en/products/detail/stackpole-electronics-inc/RMCF0402FT1K58/1761782)|1| $0.10 | Resistor for switching green LED |
|**Total**|-------|$1.32||

_The overall cost of one grow module has been reduced from $6.37 to $4.1_ 

The design can now include over 1.5 times the number grow light modules at the original price.

## 2022_10_07 - General

### LEDs
Since each grow light module has one red, one green and one blue LED, it would be beneficial to consolidate these and buy one RGB LED. The main
benefits being cost and design simplicity. Additionally, this will greatly reduce the amount of soldering and further modularize the design.

| LED      | Cost | Intensity | Comments |
| ----------- | ----------- |  ----------- |  ----------- |
| [UV](https://www.mouser.com/ProductDetail/Kingbright/AA3528VRVFS-A?qs=rY7msk5yxfb63mh907EyRA%3D%3D) (315-400 nm)     | $0.67      |  250mcd |  ----------- |
| [RGB](https://www.digikey.com/en/products/detail/creeled-inc/CLV1A-FKB-CK1VW1DE1BB7C3C3/7907693) | $0.42 |  710mcd Red, 1450mcd Green, 310mcd Blue |  ----------- |
| **Total**  | $1.09        |  ----------- |  ----------- |

New current limiting resistors had to be selected as follows:

| LED      | V_on | Desired I | Corresponding Resistor |Final Resistor Choice |Cost |
| ----------- | ----------- |  ----------- |  ----------- |----------- | ----------- |
| UV | 3.3V |  20mA |  85 ohms | [100 ohm](https://www.digikey.com/en/products/detail/stackpole-electronics-inc/RMCF1210JT100R/1757185) | $0.11 |
| Blue | 3.2V |  20mA |  90 ohms | [90.9 ohms](https://www.digikey.com/en/products/detail/stackpole-electronics-inc/RMCF0603FT90R9/1760976) |$0.10|
| Yellow-Red | 2V |  20mA |  150 ohms | [150 ohms](https://www.digikey.com/en/products/detail/stackpole-electronics-inc/RMCF0805FT150R/1760641) |$0.10 |
| Green | 3.2V |  20mA |  90 ohms| [90.9 ohms](https://www.digikey.com/en/products/detail/stackpole-electronics-inc/RMCF0603FT90R9/1760976) | $0.10 |
| **Total** | ----------- |  ----------- |  ----------- |----------- | $0.41 |

After further analysis, having four npn transistors was redundant. One npn transistor could readily handle switching all the LEDs as they only draw
80mA of current total. Verifying simulations are shown belown. The simulations are using an LED model which is expected to draw 30mA.


![image](https://user-images.githubusercontent.com/55333859/194727519-c38282bb-ff42-4c5b-b185-d36dfa78882e.png)

![image](https://user-images.githubusercontent.com/55333859/194726919-bf076c71-2adc-4629-890d-5e17434ef0d6.png)




Since the LEDs have been changed, the resistors to limit the base current drawn from the microcontrollers also had to be changed as follows:

| Component      |Quantity |Price|Comment|
| ----------- | ----------- |  ----------- |   ----------- |  
| [NPN transistors](https://www.digikey.com/en/products/detail/onsemi/MMBT2222AM3T5G/2050501) |1 |    $0.23| Transistors for switching |
| [2.55kΩ resistor](https://www.digikey.com/en/products/detail/stackpole-electronics-inc/RMCF1206FT2K55/1759883) | 1 |   $0.10 |  Base Resistor for switching LEDs  |  
|**Total**|-------|$0.33||

The total cost of a grow light module has been further reduced from $4.10 to $1.83. Additionally, these changes allows for us to easily breadboard and test the circuit before ordering the PCB.

## 2022_10_08 - Light Intensity II
 
Currently the fundamental design question needs to be answered: _How much light can and should be provided by our design?_

### Design Analysis
Referring to the final LED choice described in [the journal entry from October 7th](https://github.com/heonjang/LightControlSystem/blob/Christelle/October/2022_10_07%20-%20General.md), each grow light module will provide 2.72 cd. Candela is the intensity illuminated along a line 0 degrees from the LED. Since our main concern is how much light our design for an area of plants, the candela unit is not sufficient. The following page will walk through using the units of candela to determine the illuminance on a square foot of area.

[Previously](https://github.com/heonjang/LightControlSystem/blob/Christelle/October/2022_10_02%20-%20Light%20Intensity.md), it was determined that to best accomodate all types of plants, our prototype should provide 1000+ foot-candles of light.

### Units of Light Intensity
A foot-candle is [defined as](https://www.studiobinder.com/blog/what-is-a-foot-candle-definition/) "the amount of light that falls on a surface that is 1 foot away from a singular candle". The following diagrams illustrate common standards of light illuminance

![image](https://user-images.githubusercontent.com/55333859/194730908-116e3e4a-2e16-4787-ba59-fbaf1263e4f0.png)

![image](https://user-images.githubusercontent.com/55333859/194732442-00fbd7e8-c797-4137-8e7d-c01b31bc6764.png)
![image](https://user-images.githubusercontent.com/55333859/194734009-bbb474cf-b0e2-4b99-9c32-05ac9f8f09c7.png)


### Converting Candela to Lumens
The datasheet of the both the RGB and UV LEDs, provide graphs of luminous intensity versus angle from the LED. In both the apex angle, the angle where luminous intensity is 50% is 120 degrees (±60  degrees). These plots are provided below.

![image](https://user-images.githubusercontent.com/55333859/194732379-a41d7f7c-9434-43a0-a963-6f38e6b423af.png)

![image](https://user-images.githubusercontent.com/55333859/194732904-75807c24-6e40-408b-958c-d50f1a10466f.png)

The folllowing equation can be used to convert candela to lumens: 1cd = 1lm / sr

Following this [tutorial](https://actionservicesgroup.com/blog/lighting-measurements-an-in-depth-guide-part-1/#:~:text=The%20full%20equation%20to%20find,cos%20(apex%20angle%2F2)):
Ω = 2π(1−cos(α/2)) where α is the viewing angle
Ω = π steradians

Then 2.72 cd * π steradians = 8.55 lumens per grow light.

For $100, we will provide 462 lumens of light. This is not enough light for our implementation.


**_To be continued in [Light Intensity III](https://github.com/heonjang/LightControlSystem/blob/Christelle/October/2022_10_09%20-%20Light%20Intensity%20III.md)_**

