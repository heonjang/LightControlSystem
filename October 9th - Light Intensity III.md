# Light Intensity III

The [Light Intensity II](https://github.com/heonjang/LightControlSystem/blob/Christelle/October%208th%20-%20Light%20Intensity%20II.md) entry, revealed a key shortcoming from our final design, not enough lumens were provided.

Following the light standard determined previously, our design has 3 objectives, to provide:
1. between 50 (538lm) and 250 foot-candles (2690 lm) for low light plants
2. 750+ (8,070 lm) foot-candles for medium light plants
3. 1000+ (10,760) foot-candles for high light plants

The success of our design relies on at minimum attaining the first objective.

The previous selection of LEDs failed to provide enough lumens. As such these will have to be reselected.

## Reselecting LEDs
The RGB LED from before can be replaced by a white light LED. In particular, [this LED](https://www.digikey.com/en/products/detail/ams-osram-usa-inc/GW-P9LR35-PM-M2M3-XX57-1-180-R18/9641611) was selected for its high lumen output and price.

The following plot taken from the datasheet shows the relative intensity vs wavelength. Notably, the LED will provide a combination of red, green and blue light. The blue light is the dominant wavelength, followed by red then green.

![image](https://user-images.githubusercontent.com/55333859/194781914-64680adb-7ed1-4217-987a-64310fec482a.png)

UV LEDs have shown to both be costly and emit low levels of light. As such, given budget constraints, it would be better to replace these with another more cost effective LED. In particular, the white LED alone should be sufficient. Mainly, the combination of red, green and blue are all beneficial to plant growth (see [here](https://lightsciencetech.com/visible-wavelength-range-plant-growth/#:~:text=610-700%20nm%20is%20considered,plant%20growth%20and%20optimised%20yield)). On a higher budget, UVA or far red LEDs could be added to further supplement the light to the plant.

| LED      | Cost | Intensity | Comments |
| ----------- | ----------- |  ----------- |  ----------- |
| [White](https://www.digikey.com/en/products/detail/ams-osram-usa-inc/GW-P9LR35-PM-M2M3-XX57-1-180-R18/9641611) | $1.00 | 200lm |  ----------- |
| **Total**  | $0.42        |  ----------- |  ----------- |

New current limiting resistors had to be selected as follows:

| LED      | V_on | Desired I | Corresponding Resistor |Final Resistor Choice |Cost |
| ----------- | ----------- |  ----------- |  ----------- |----------- | ----------- |
| White | 2.75V |  65mA |  34.62 ohms | [34.8 ohms](https://www.digikey.com/en/products/detail/yageo/RC1206FR-0734R8L/728828) |$0.10|
| **Total** | ----------- |  ----------- |  ----------- |----------- | $0.10 |


Due to the reduction and change of types of LEDs, the grow light module needs to be restructured. Mainly, the transistors have a maximum collector current of 600mA. This opens the door to having up to 9 white LEDs per module. For the sake of adjustability, each module should be moderately bright or even low brightness. This led to the design choice of 8 LEDs per module. As a result, each module would have approximately 320 lumens of light, 
The resistors to limit the base current drawn from the microcontrollers changed as follows:

| Component      |Quantity |Price|Comment|
| ----------- | ----------- |  ----------- |   ----------- |  
| [NPN transistors](https://www.digikey.com/en/products/detail/onsemi/MMBT2222AM3T5G/2050501) |1 |    $0.23| Transistors for switching |
| [2.37kΩ resistor](https://www.digikey.com/en/products/detail/stackpole-electronics-inc/RMCF1206FG2K37/1758792) | 1 |   $0.10 |  Base Resistor for switching LEDs  |  
|**Total**|-------|$0.33||
