In this note, I am going to talk about the DecisionMaker


In the DecisionMaker, it will compare the target illumination and the current intensity store in the database.

<img width="700" alt="Screen Shot 2022-12-08 at 3 59 22 PM" src="https://user-images.githubusercontent.com/103418311/206576257-dad9ea9e-a605-4650-aa80-c2d57b638d85.png">

Since the goal of this project is to maximize the electricity efficiency, it needs to prioritize the natural light source, Sun.

Therefore,

## 1. Target Illumination > Current Illumination
The system requires more light
> First tries to open the blind, use LEDs only if blinds are fully open
  
## 2. Target Illumination < Current Illumination
The system receive too much light
> First tries to turn off lights.



This algorithm runs periodically in a thread and the decision will be stored in the database.


The reason why decisions are stored in the database is because then the system can keep track of activity history

Which will be good metrics to analyze the performance of the system



