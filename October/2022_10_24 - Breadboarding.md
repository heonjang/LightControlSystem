# Breadboard Circuit
Since the switching circuit for the LEDs is such a significant portion of this project, a simple breadboard model was created to test the functionality.
An ADALM2000 was used to act as the microcontroller, as well as power the LED on. Due to limitations in components that were readily available, this
model was based on a blue LED with around 3.2V forward volatage and 30mA forward current. The transistor remains the 2N2222 as is used in the actual design.

## Results
Below is the setup for the OFF signal from the microcontroller. 3.4V are provided to the collector branch of the NPN, and a low signal is output from
the ADALM. The circuit behaves as expected and the light remains off for this setup.

![image](https://user-images.githubusercontent.com/55333859/197673376-ef4fc73f-4bd0-4ca2-8fe7-475310b3a890.png)


![image](https://user-images.githubusercontent.com/55333859/197673064-51d65b9e-d8e0-401f-abe4-c0127a00e843.png)

The setup for the ON signal from the microcontroller is similar to before. There is still 3.4V provided to the collector branch,but now a high signal of
3.3V is provided to the base branch. The light switches on as expected, validating our circuit design.

![image](https://user-images.githubusercontent.com/55333859/197673813-5c25b071-b9a6-4bb8-84a7-93ac5607012a.png)

![image](https://user-images.githubusercontent.com/55333859/197673946-618238b4-7f05-4991-99fc-cda636de6eb3.png)

## New Developments
One discovery made while breadboarding the circuit is that adjusting the base voltage can adjust the brightness of the LED. 
The second design iteration could then focus on adding more adjustability to the LEDs then by either adjusting the microcontroller output
or similarly, including a digital potentiometer to limit current flow through the LEDs.

![image](https://user-images.githubusercontent.com/55333859/197675358-fce7757b-4bd5-4417-b57c-09b938359839.png)


https://user-images.githubusercontent.com/55333859/197675320-b6443df9-65df-4a58-b49f-7ef106ffe3fa.mov

