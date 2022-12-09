# Christelle Worklog
1. [Christelle Worklog](https://github.com/heonjang/LightControlSystem/edit/Christelle/README.md#christelle-worklog)
2. [2022_09_20 - Changes (UV Lights I)](https://github.com/heonjang/LightControlSystem/edit/Christelle/README.md#2022_09_20---changes)
3. [2022_09_27 - General Changes (UV Lights II)](https://github.com/heonjang/LightControlSystem/edit/Christelle/README.md#2022_09_27---general-changes)
4. [2022_09_28 - Safety](https://github.com/heonjang/LightControlSystem/edit/Christelle/README.md#2022_09_28---safety)
5. [2022_09_29 - LED Choice](https://github.com/heonjang/LightControlSystem/edit/Christelle/README.md#2022_09_29---led-choice)




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

