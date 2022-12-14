## Design Changes

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

