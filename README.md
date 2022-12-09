# Christelle Worklog
1. [Christelle Worklog](https://github.com/heonjang/LightControlSystem/blob/Christelle/README.md#christelle-worklog)
2. [2022_09_20 - Changes (UV Lights I)](https://github.com/heonjang/LightControlSystem/blob/Christelle/README.md#2022_09_20---changes)
3. [2022_09_27 - General Changes (UV Lights II)](https://github.com/heonjang/LightControlSystem/blob/Christelle/README.md#2022_09_27---general-changes)
4. [2022_09_28 - Safety](https://github.com/heonjang/LightControlSystem/blob/Christelle/README.md#2022_09_28---safety)
5. [2022_09_29 - LED Choice](https://github.com/heonjang/LightControlSystem/blob/Christelle/README.md#2022_09_29---led-choice)
6. [2022_10_02 - Light Intensity](https://github.com/heonjang/LightControlSystem/blob/Christelle/README.md#2022_10_02---light-intensity)
7. [2022_10_03 - Design Analysis](https://github.com/heonjang/LightControlSystem/blob/Christelle/README.md#2022_10_03---design-analysis)
8. [2022_10_05 - LED Changes](https://github.com/heonjang/LightControlSystem/blob/Christelle/README.md#2022_10_05---led-changes)
9. [2022_10_06 - Transistors](https://github.com/heonjang/LightControlSystem/blob/Christelle/README.md#2022_10_06---transistors)
10. [2022_10_07 - General](https://github.com/heonjang/LightControlSystem/blob/Christelle/README.md#2022_10_07---general)
11. [2022_10_08 - Light Intensity II](https://github.com/heonjang/LightControlSystem/blob/Christelle/README.md#2022_10_08---light-intensity-ii)
12. [2022_10_09 - Light Intensity III](https://github.com/heonjang/LightControlSystem/blob/Christelle/README.md#2022_10_09---light-intensity-iii)
13. [2022_10_10 - Board Considerations and Design Analysis](https://github.com/heonjang/LightControlSystem/blob/Christelle/README.md#2022_10_10---board-considerations-and-design-analysis)
14. [2022_10_24 - Breadboarding](https://github.com/heonjang/LightControlSystem/blob/Christelle/README.md#2022_10_24---breadboarding)
15. [December 8th - Month of November Summary](https://github.com/heonjang/LightControlSystem/blob/Christelle/README.md#december-8th---month-of-november-summary)




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

## 2022_10_09 - Light Intensity III

The [Light Intensity II](https://github.com/heonjang/LightControlSystem/blob/Christelle/October/2022_10_08%20-%20Light%20Intensity%20II.md) entry, revealed a key shortcoming from our final design, not enough lumens were provided.

Following the light standard determined previously, our design has 3 objectives, to provide:
1. between 50 (538lm) and 250 foot-candles (2690 lm) for low light plants
2. 750+ (8,070 lm) foot-candles for medium light plants
3. 1000+ (10,760) foot-candles for high light plants

The success of our design relies on at minimum attaining the first objective.

The previous selection of LEDs failed to provide enough lumens. As such these will have to be reselected.

### Reselecting LEDs
The RGB LED from before can be replaced by a white light LED. In particular, [this LED](https://www.digikey.com/en/products/detail/ams-osram-usa-inc/GW-P9LR35-PM-M2M3-XX57-1-180-R18/9641611) was selected for its high lumen output and price.

The following plot taken from the datasheet shows the relative intensity vs wavelength. Notably, the LED will provide a combination of red, green and blue light. The blue light is the dominant wavelength, followed by red then green. 

![image](https://user-images.githubusercontent.com/55333859/194781914-64680adb-7ed1-4217-987a-64310fec482a.png)

UV LEDs have shown to both be costly and emit low levels of light. As such, given budget constraints, it would be better to replace these with another more cost effective LED. In particular, the white LED alone should be sufficient. Mainly, the combination of red, green and blue are all beneficial to plant growth (see [here](https://lightsciencetech.com/visible-wavelength-range-plant-growth/#:~:text=610-700%20nm%20is%20considered,plant%20growth%20and%20optimised%20yield)). On a higher budget, UVA or far red LEDs could be added to further supplement the light to the plant.

| LED      | Cost | Intensity | Comments |
| ----------- | ----------- |  ----------- |  ----------- |
| [White](https://www.digikey.com/en/products/detail/ams-osram-usa-inc/GW-P9LR35-PM-M2M3-XX57-1-180-R18/9641611) | $1.00 | 200lm |  ----------- |
| **Total**  | $1        |  ----------- |  ----------- |


To accomodate the white LED, VDD will have to be above the forward voltage of 5.5V. When selecting the corresponding AC/DC converter, the power rating will have to be above the power consumed by the LEDs. 
To meet each objective, there must be:

|Objective |  Number of Modules      | Power|  Current| Comments |
| ----------- | ----------- |  ----------- |  ----------- | ----------- |
| Low-Light | 9 |  8.91W | 1.62A |  ----------- |
| Mid-Light | 41 |  40.59W | 7.31A |  ----------- |
| High-Light | 54 |  53.46W | 9.72A |  ----------- |

The current draw and power dissipated by the LEDs places significant restrictions on the AC/DC converter. Preliminary research has led to the possibility of using a 12V 15A 180W rated [power supply](https://www.amazon.com/ALITOVE-Transformer-Switching-Converter-Security/dp/B078RZ6C3N/ref=asc_df_B078RZ6C3N/?tag=hyprod-20&linkCode=df0&hvadid=242045434535&hvpos=&hvnetw=g&hvrand=6506752645919981557&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9022196&hvtargid=pla-418440784733&th=1).

Assuming the use of a 12V power supply, new current limiting resistors were selected as follows:

| LED      | V_on | Desired I | Corresponding Resistor |Final Resistor Choice |Cost |
| ----------- | ----------- |  ----------- |  ----------- |----------- | ----------- |
| White | 5.55V |  180mA |  35.83 ohms | [36 ohms](https://www.digikey.com/en/products/detail/te-connectivity-passive-product/352136RFT/4279934) |$0.59|
| **Total** | ----------- |  ----------- |  ----------- |----------- | $0.59 |


Due to the reduction and change of types of LEDs, the grow light module needs to be restructured. Mainly, the transistors have a maximum collector current of 600mA. This opens the door to having 3 white LEDs per module. The choice of 3 LEDs would lead to each module having 55 foot-candles, which is a decent amount of light. With no significant downside to having 3 LEDs to module, there will be 18 modules each with 3 LEDs.

The resistors to limit the base current drawn from the microcontrollers changed as follows:

| Component      |Quantity |Price|Comment|
| ----------- | ----------- |  ----------- |   ----------- |  
| [NPN transistors](https://www.digikey.com/en/products/detail/onsemi/MMBT2222AM3T5G/2050501) |1 |    $0.23| Transistors for switching |
| [374Ω resistor](https://www.digikey.com/en/products/detail/panasonic-electronic-components/ERJ-6ENF3740V/111199) | 1 |   $0.10 |  Base Resistor for switching LEDs  |  
|**Total**|-------|$0.33||

## 2022_10_10 - Board Considerations and Design Analysis

Due to restrictions on PCB orders in ECE 445, our design will shift to consist of one PCB with a single microcontroller that controls the lights, motor and photosensor. 
Connectors and wires will connect each component to the control PCB. There are a few major considerations left still.

### Power
The [recent changes](https://github.com/heonjang/LightControlSystem/blob/Christelle/October/2022_10_09%20-%20Light%20Intensity%20III.md) to the design changed this project from a low power to mid power design. As such, the power supply will have to be capable of handling the 60 Watts of power dissipated by the LEDs at full light as well as by other design components. The following [power supply 
](https://www.amazon.com/ALITOVE-100-240V-Converter-Transformer-5-5x2-1mm/dp/B07MXXXBV8/ref=sxin_15_pa_sp_search_thematic_sspa?content-id=amzn1.sym.6b029eb3-7d41-4744-b45d-69fe835e098d%3Aamzn1.sym.6b029eb3-7d41-4744-b45d-69fe835e098d&cv_ct_cx=12v+15+amp+power+supply&keywords=12v+15+amp+power+supply&pd_rd_i=B07MXXXBV8&pd_rd_r=39865509-9d64-417a-bc5e-366efbf2829f&pd_rd_w=7I11j&pd_rd_wg=hmNNq&pf_rd_p=6b029eb3-7d41-4744-b45d-69fe835e098d&pf_rd_r=CDZPZD2ZX2RHV2VJX3BZ&qid=1665428790&qu=eyJxc2MiOiI0LjE4IiwicXNhIjoiMy44MCIsInFzcCI6IjMuMDcifQ%3D%3D&sr=1-3-a73d1c8c-2fd2-4f19-aa41-2df022bcb241-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzNVJHS0xON1lYRzZDJmVuY3J5cHRlZElkPUEwMTAzNTA3MzlGSDhHRFo4WlFVNyZlbmNyeXB0ZWRBZElkPUEwMjgyMTM3MkFFNzJJQk1aMUxJWiZ3aWRnZXROYW1lPXNwX3NlYXJjaF90aGVtYXRpYyZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=) was selected as it has a high power rating as well as a nominal voltage rating of 12V. The design is well below the recommended maximum of 96W designs. 

This 12V will then be stepped down to 3.3V for the microcontroller as well as the motor. Using the TI Instruments [webench](https://webench.ti.com/) application as well as verifying the results with the schematic, the [TPS565208](https://www.digikey.com/en/products/detail/texas-instruments/TPS565208DDCR/7776393) was selected.

### Simulations
The design was simulated using [the model](https://www.osram.com/apps/downloadcenter/os/?path=%2Fos-files%2FElectrical+Simulation%2FLED%2FDURIS%2FDURIS_S%2FDURIS_S_8%2FGW_P9LR35.PM%2F) provided by OSRAM.
The LTSpice circuit and resulting simulation is shown below

![image](https://user-images.githubusercontent.com/55333859/194899698-8ca9d2c6-0268-4392-b4b9-462c2a01cac8.png)


![image](https://user-images.githubusercontent.com/55333859/194902398-2b44e802-6a90-4273-8df6-b0be4bb1b5e0.png)
 
 The collector current is not the 540mA expected from the 3 diodes. 
 The main issue being the DC current gain is not 100, instead it is around 80. 
 The datasheet confirms the simulations, right around 200mA the DC current gain begins to drop. It is crucial that the current through the LEDs is as close to 180mA as possible, otherwise the brightness of the LEDs will not be correct
 ![image](https://user-images.githubusercontent.com/55333859/194902812-cc294132-bde0-4a6b-9494-d64bdd7b60c7.png)

Consequently, it would be better to return to one transistor per LED for a more consistent current gain. Additionally, the 36 ohm resistors can be switched out for [this](https://www.digikey.com/en/products/detail/te-connectivity-passive-product/354012RJT/9926985) 12 ohm resistor. To validate these results, the new design was simulated in LTspice.

![image](https://user-images.githubusercontent.com/55333859/194919436-ddd3d25b-471e-42ef-912d-3d02eb136df2.png)


![image](https://user-images.githubusercontent.com/55333859/194919317-978ace5e-0003-4a4d-b35c-3f6287b08a57.png)

All three LEDs have a saturation current close to 180mA as expected. [Arrays](https://www.digikey.com/en/products/detail/onsemi/MBT2222ADW1T1G/1477281) of transistors will be used as they are roughly the same price as a singular transistor and share the same properties.

## 2022_10_24 - Breadboarding

### Breadboard Circuit
Since the switching circuit for the LEDs is such a significant portion of this project, a simple breadboard model was created to test the functionality.
An ADALM2000 was used to act as the microcontroller, as well as power the LED on. Due to limitations in components that were readily available, this
model was based on a blue LED with around 3.2V forward volatage and 30mA forward current. The transistor remains the 2N2222 as is used in the actual design.

### Results
Below is the setup for the OFF signal from the microcontroller. 3.4V are provided to the collector branch of the NPN, and a low signal is output from
the ADALM. The circuit behaves as expected and the light remains off for this setup.

![image](https://user-images.githubusercontent.com/55333859/197673376-ef4fc73f-4bd0-4ca2-8fe7-475310b3a890.png)


![image](https://user-images.githubusercontent.com/55333859/197673064-51d65b9e-d8e0-401f-abe4-c0127a00e843.png)

The setup for the ON signal from the microcontroller is similar to before. There is still 3.4V provided to the collector branch,but now a high signal of
3.3V is provided to the base branch. The light switches on as expected, validating our circuit design.

![image](https://user-images.githubusercontent.com/55333859/197673813-5c25b071-b9a6-4bb8-84a7-93ac5607012a.png)

![image](https://user-images.githubusercontent.com/55333859/197673946-618238b4-7f05-4991-99fc-cda636de6eb3.png)

### New Developments
One discovery made while breadboarding the circuit is that adjusting the base voltage can adjust the brightness of the LED. 
The second design iteration could then focus on adding more adjustability to the LEDs then by either adjusting the microcontroller output
or similarly, including a digital potentiometer to limit current flow through the LEDs.

![image](https://user-images.githubusercontent.com/55333859/197675358-fce7757b-4bd5-4417-b57c-09b938359839.png)


https://user-images.githubusercontent.com/55333859/197675320-b6443df9-65df-4a58-b49f-7ef106ffe3fa.mov

## December 8th - Month of November Summary

The majority of the month of November was dedicating to soldering and assembling the prototype. Below is a summary of the key changes made during this time period

### Microcontroller
The microcontroller acts as a wireless access point. Mainly, any device, (phone or computer) can connect to the ESP32 access point. Once, connected, redirecting to the website 192.168.4.1 will display the current photosensor reading. The LED modules can then be switched on and off, by redirecting to 192.168.4.1/Module{#}_{ON or OFF}.

Our second ESP32 chip was unfortunately fried while soldering, which led to the temporary replacement by an Arduino development board.

### Power
To power the LEDs, a 12V, 135W ACDC converter was used. This more than supplies enough power, even if more LED modules were potentially added in the future. Due to time limitations, the ESP32 was powered from the lab's power supply for the demo. However, this should be replaced by either a step down voltage circuit (from 12V to 3.3V), or buying an additional wall adapter.

### Packaging
An LED panel frame was constructed to house the LEDs. Unfortunately, there were still some drill holes that should be included in the design so as to be able to properly hide the wires. Additionally, a mounting system or hanging system should be added to the design.
