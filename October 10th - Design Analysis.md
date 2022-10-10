# Design Analysis

## Simulations
The design was simulated using [the model](https://www.osram.com/apps/downloadcenter/os/?path=%2Fos-files%2FElectrical+Simulation%2FLED%2FDURIS%2FDURIS_S%2FDURIS_S_8%2FGW_P9LR35.PM%2F) provided by OSRAM.
The LTSpice circuit and resulting simulation is shown below

![image](https://user-images.githubusercontent.com/55333859/194899698-8ca9d2c6-0268-4392-b4b9-462c2a01cac8.png)


![image](https://user-images.githubusercontent.com/55333859/194902398-2b44e802-6a90-4273-8df6-b0be4bb1b5e0.png)
 
 The collector current is not the 540mA expected from the 3 diodes. 
 The main issue being the DC current gain is not 100, instead it is around 80. 
 The datasheet confirms the simulations, right around 200mA the DC current gain begins to drop. It is crucial that the current through the LEDs is as close to 180mA as possible, otherwise the brightness of the LEDs will not be t
 ![image](https://user-images.githubusercontent.com/55333859/194902812-cc294132-bde0-4a6b-9494-d64bdd7b60c7.png)

Consequently, it would be better to return to one transistor per LED for a more consistent current gain. Additionally, the 36 ohm resistors can be switched out for [this](https://www.digikey.com/en/products/detail/te-connectivity-passive-product/354012RJT/9926985) 12 ohm resistor. To validate these results, the new design was simulated in LTspice.

![image](https://user-images.githubusercontent.com/55333859/194919436-ddd3d25b-471e-42ef-912d-3d02eb136df2.png)


![image](https://user-images.githubusercontent.com/55333859/194919317-978ace5e-0003-4a4d-b35c-3f6287b08a57.png)

All three LEDs have a saturation current close to 180mA as expected. [Arrays](https://www.digikey.com/en/products/detail/onsemi/MBT2222ADW1T1G/1477281) of transistor will be used as they are roughly the same price as a singular transistor.
