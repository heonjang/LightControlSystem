## General Design Updates

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


![image](https://user-images.githubusercontent.com/55333859/194726884-4acb0d2f-5c94-4a49-a9f2-5ccd89aeefde.png)

![image](https://user-images.githubusercontent.com/55333859/194726919-bf076c71-2adc-4629-890d-5e17434ef0d6.png)




Since the LEDs have been changed, the resistors to limit the base current drawn from the microcontrollers also had to be changed as follows:

| Component      |Quantity |Price|Comment|
| ----------- | ----------- |  ----------- |   ----------- |  
| [NPN transistors](https://www.digikey.com/en/products/detail/onsemi/MMBT2222AM3T5G/2050501) |1 |    $0.23| Transistors for switching |
| [12kΩ resistor](https://www.digikey.com/en/products/detail/te-connectivity-passive-product/CRGCQ0603F12K/8576303) | 1 |   $0.10 |  Resistor for switching UV LED  |  
| [2.55kΩ resistor](https://www.digikey.com/en/products/detail/stackpole-electronics-inc/RMCF1206FT2K55/1759883) | 1 |   $0.10 |  Resistor for limiting current from GPIO pin  |  
 | [10.5kΩ resistor](https://www.digikey.com/en/products/detail/panasonic-electronic-components/ERJ-1GNF1052C/2036228) | 3 |  $0.10 |  Resistor for switching red, blue and green LEDs |  
|**Total**|-------|$0.73||

The total cost of a grow light module has been further reduced from $4.10 to $2.23. Additionally, these changes allows for us to easily breadboard and test the circuit before ordering the PCB.
