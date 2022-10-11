## TO DO

Don't feel obligated to do everything in the list, just do whatever you reasonably can. More important items are starred.

- [ ] Identify connectors and barrel jack connector *
- [ ] Double check if motor needs 3.3 or 5V
- [ ] Check if switching regulator to 3.3V provides enough power for the circuit *
- [ ] Identify a wall adapter (or possibly 2, see note below) *
- [ ] Develop a preliminary board design *
- [ ] Take a look at starboards for the LEDs (Maybe? lower priority than rest of the list)

For the LEDs, in simulation they draw 6.275W of power per module. Current drawn from microcontroller is 5.4mA per module. 
Current drawn from the 12V is 540mA per module. 

Since the total power across 16 modules is 100W, and it is recommended to only use 80% of available power from a wall adapter. 
It would be smart to add another wall plug solely for the LEDs rated at 120W. 

Then there would likely be two wall adapters:
1. highly rated at 120W, with 10A current, 12V output
2. one lower rated (at whatever power is necessary for the rest of the board)
