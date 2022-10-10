# Design Analysis

## Simulations
The design was simulated using [the model](https://www.osram.com/apps/downloadcenter/os/?path=%2Fos-files%2FElectrical+Simulation%2FLED%2FDURIS%2FDURIS_S%2FDURIS_S_8%2FGW_P9LR35.PM%2F) provided by OSRAM.
The LTSpice circuit and resulting simulation is shown below

![image](https://user-images.githubusercontent.com/55333859/194899698-8ca9d2c6-0268-4392-b4b9-462c2a01cac8.png)


![image](https://user-images.githubusercontent.com/55333859/194902398-2b44e802-6a90-4273-8df6-b0be4bb1b5e0.png)
 
 The collector current is not the 540mA expected from the 3 diodes. The main issue being the DC current gain is not 100, instead it is around 80. 
