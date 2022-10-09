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


