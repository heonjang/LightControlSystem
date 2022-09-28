# LightControlSystem

## Sep 27th

From Design Document meeting, we will be using relays for the UV light source. We'll be using the SRD-05VDC-SL-C 5V relay. Since this requires a 5V power supply, 
we'll use the L6920DC (https://www.st.com/resource/en/datasheet/l6920dc.pdf) step-up converter to do so. We have yet to figure out how to wire these components and
program them so that appropriate number of LEDs light up depending on the light intensity.

(https://electronics.stackexchange.com/questions/18570/stepping-up-3v-to-5v)


### Research for lights needed for optimal plant growth

(https://lightsciencetech.com/visible-wavelength-range-plant-growth/#:~:text=610%2D700%20nm%20is%20considered,plant%20growth%20and%20optimised%20yield.)

From the above article, we can learn that lights of wavelenghts ranging 400-800nm are greatly beneficial for plant growth, which overlaps the range of LEDs. 
This article also mentions that using light sources of different wavelenghts within this range can be even better for plant growth. 

(https://www.amazon.com/VIPARSPECTRA-Reflector-Spectrum-Indoor-Plants/dp/B01B4GQ6MO/ref=as_li_ss_tl?tag=plantcaretoday-20&th=1)

This a product that uses LED like we do to provide artifical lighting. It uses a variety of LED colors, thus wavelength, and also provides amount of PPFD 
(photosynthetic photon flux density), most suitable measurement of light when it comes to plant growth, depending on the distance. Could be a good reference product. 
Might be a good idea to consider the following, if possible.

Three important questions you should look to be answered when researching LED grow lights are:

Question 1: How much instantaneous PAR from the fixture is available to plants (measured as PPFD)? 
Question 2: How much PAR is being distributed across the entire canopy? 
Question 3: How much wattage is used by the fixture to make PAR available to your plants?
