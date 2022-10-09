# Light Intensity

Currently the fundamental design question needs to be answered: _How much light can and should be provided by our design?_

## Design Analysis
Referring to the final LED choice described in [the journal entry from October 7th](https://github.com/heonjang/LightControlSystem/blob/Christelle/October%207th%20-%20General.md), each grow light module will provide 2.72 cd. Candela is the intensity illuminated along a line 0 degrees from the LED. Since our main concern is how much light our design for an area of plants, the candela unit is not sufficient. The following page will walk through using the units of candela to determine the illuminance on a square foot of area.

[Previously](https://github.com/heonjang/LightControlSystem/blob/Christelle/October%202nd%20-%20Light%20Intensity.md), it was determined that to best accomodate all types of plants, our prototype should provide 1000+ foot-candles of light.

### Units of Light Intensity
A foot-candle is [defined as](https://www.studiobinder.com/blog/what-is-a-foot-candle-definition/) "the amount of light that falls on a surface that is 1 foot away from a singular candle". The following diagrams illustrate common standards of light illuminance

![image](https://user-images.githubusercontent.com/55333859/194730908-116e3e4a-2e16-4787-ba59-fbaf1263e4f0.png)

![image](https://user-images.githubusercontent.com/55333859/194732442-00fbd7e8-c797-4137-8e7d-c01b31bc6764.png)

### Converting Candela to Lumens
The datasheet of the both the RGB and UV LEDs, provide graphs of luminous intensity versus angle from the LED. In both the apex angle, the angle where luminous intensity is 50% is 60 degrees. These plots are provided below.

![image](https://user-images.githubusercontent.com/55333859/194732379-a41d7f7c-9434-43a0-a963-6f38e6b423af.png)

![image](https://user-images.githubusercontent.com/55333859/194732904-75807c24-6e40-408b-958c-d50f1a10466f.png)
