## Design Changes

The changes we made to our design are as follows:

#### UV Lights
Due to a lack of available adjustable UV lights, the project will now have 6 individual 5W UV light bulbs.
These will be switched on and off accordingly to adjust the light to the plant.
The microcontroller will control how many of these bulbs are turned on at a time by flipping switches.

#### Powering Considerations
The ESP32's consume non-negligible amounts of power. As a result, instead of 3 ESP32's, our design will only have 2.
The light sensor will be connected to the same ESP32 as the UV lights to cut down on power consumption.

