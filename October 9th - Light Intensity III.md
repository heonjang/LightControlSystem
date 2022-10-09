# Light Intensity III

The [Light Intensity II](https://github.com/heonjang/LightControlSystem/blob/Christelle/October%208th%20-%20Light%20Intensity%20II.md) entry, revealed a key shortcoming from our final design, not enough lumens were provided.

Following the light standard determined previously, our design has 3 objectives, to provide:
1. between 50 (538lm) and 250 foot-candles (2690 lm) for low light plants
2. 750+ (8,070 lm) foot-candles for medium light plants
3. 1000+ (10,760) foot-candles for high light plants

The success of our design relies on at minimum attaining the first objective.

The previous selection of LEDs failed to provide enough lumens. As such these will have to be reselected.

## Reselecting LEDs
The RGB LED from before can be replaced by a white light LED. In particular, the [LM301H](https://www.digikey.com/en/products/detail/samsung-semiconductor-inc/SPMWHD32AMH5XAU5SL/12083566) was selected for its high lumen output and price.

The following plot taken from the datasheet shows the relative intensity vs wavelength. Notably, the LED will provide a combination of red, green and blue light. The red light is the dominant wavelength, followed by blue then green.

![image](https://user-images.githubusercontent.com/55333859/194769328-9ac41cc9-1e05-4a55-9aa4-649f6a0ed990.png)

UV LEDs have shown to both be costly and emit low levels of light. As such, given budget constraints, it would be better to replace these with another more cost effective LED. In particular, far red light is another beneficial wavelength of light to plant growth (see [here](https://lightsciencetech.com/visible-wavelength-range-plant-growth/#:~:text=610-700%20nm%20is%20considered,plant%20growth%20and%20optimised%20yield)). Following this line of reasoning, the UV LED could be replaced with a far red LED.


![image](https://user-images.githubusercontent.com/55333859/194779626-459ce3a7-336c-4029-bf87-956f573abb37.png)

UV LEDs have shown to both be costly and emit low levels of light. As such, given budget constraints, it would be better to replace these with another more cost effective LED. In particular, far red light is another beneficial wavelength of light to plant growth (see [here](https://lightsciencetech.com/visible-wavelength-range-plant-growth/#:~:text=610-700%20nm%20is%20considered,plant%20growth%20and%20optimised%20yield)). Following this line of reasoning, the UV LED could be replaced with a far red LED.

| LED      | Cost | Intensity | Comments |
| ----------- | ----------- |  ----------- |  ----------- |
| [Red](https://www.digikey.com/en/products/detail/creeled-inc/XPEEPR-L1-0000-00901/6817679)     | $1.20      |   |  ----------- |
| [White](https://www.digikey.com/en/products/detail/creeled-inc/CLV1A-FKB-CK1VW1DE1BB7C3C3/7907693) | $0.42 | 39lm |  ----------- |
| **Total**  | $1.09        |  ----------- |  ----------- |

New current limiting resistors had to be selected as follows:

| LED      | V_on | Desired I | Corresponding Resistor |Final Resistor Choice |Cost |
| ----------- | ----------- |  ----------- |  ----------- |----------- | ----------- |
| UV | 3.3V |  20mA |  85 ohms | [100 ohm](https://www.digikey.com/en/products/detail/stackpole-electronics-inc/RMCF1210JT100R/1757185) | $0.11 |
| White | 2.75V |  65mA |  34.62 ohms | [34.8 ohms](https://www.digikey.com/en/products/detail/yageo/RC1206FR-0734R8L/728828) |$0.10|
| **Total** | ----------- |  ----------- |  ----------- |----------- | $0.21 |

The resistors to limit the base current drawn from the microcontrollers changed as follows:

| Component      |Quantity |Price|Comment|
| ----------- | ----------- |  ----------- |   ----------- |  
| [NPN transistors](https://www.digikey.com/en/products/detail/onsemi/MMBT2222AM3T5G/2050501) |1 |    $0.23| Transistors for switching |
| [2.37kΩ resistor](https://www.digikey.com/en/products/detail/stackpole-electronics-inc/RMCF1206FG2K37/1758792) | 1 |   $0.10 |  Base Resistor for switching LEDs  |  
|**Total**|-------|$0.33||
