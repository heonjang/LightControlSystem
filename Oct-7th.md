# First calculation

From the [Light Intensity Objective](https://github.com/heonjang/LightControlSystem/blob/Christelle/October%202nd%20-%20Light%20Intensity.md),

the maximum target amount of illumination is 1,000 foot-candles.

Therefore, the system has to be able to offer at most 1000 foot candles for each plant in the system.

<img width="581" alt="Screen Shot 2022-10-07 at 11 19 22 AM" src="https://user-images.githubusercontent.com/103418311/194600845-5981b728-a65e-4637-b0ab-d12d1428f7c9.png">

From the design document, the effective wavelength for the plant's growth is 370 ~ 500 / 600 ~ 700 nm


### LED Chart
From the [previous LED data table](https://github.com/heonjang/LightControlSystem/blob/main/October%205th.md), we can build a foot-candle per unit table.

1000 MCD = 1 CD = 1 foot-candle

| LED      | Cost | foot-candle | Cost / foot-candle |
| ----------- | ----------- |  ----------- |  ----------- |
| [UV](https://www.mouser.com/ProductDetail/Kingbright/AA3528VRVFS-A?qs=rY7msk5yxfb63mh907EyRA%3D%3D) (315-400 nm)     | $0.67      |  0.25 | $2.68 |
| [Blue](https://www.digikey.com/en/products/detail/w%C3%BCrth-elektronik/150141BS73130/13584853) (440-500 nm) | $0.40 |  1 | $0.4 |
| [Yellow-Red](https://www.digikey.com/en/products/detail/vishay-semiconductor-opto-division/VLMO233U1AA-GS08/3025492) (610-700 nm)  | $0.51  |  0.76 | $0.67 |
| [Green](https://www.digikey.com/en/products/detail/creeled-inc/XQAGRN-02-0000-000000Z01/5761845) (510-610 nm) | - excluded - |  - excluded - | - excluded - |
 
_The Green light is exclude from the consideration because it is meaningless to the plant's growth_

Therefore, if we only use the Blue LED which is the most cost-effective one, we will need to have 1000 of them at $400.
This is impossible to both buy/solder. Therefore we need to

consider one or a combination of 

1. Think of much more powerful/efficient light source
2. Reduce the distance between the light source and the plants (my current assumption was 1 foot)
3. Lower the target illumination
