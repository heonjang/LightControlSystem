## Safety Updates

### Emergency Shutoff
One of the main concerns of this project is the potential for safety failures. Primarily, it is a concern that the lights might possibly overheat and start a fire.
As such, an emergency shutoff is implemented. This will be a dual sided approach: both through software as well as hardware.


For the hardware implementation, a relay circuit will be implemented so that the power to the UV light circuit is usually on. 
The application will have an emergency shutoff setting, which when selected, the app will send a signal to the UV light microcontroller
to switch off the relay and power to the UV light circuit. Additionally, as another failsafe, there will be a manual switch ([RE111C1021-116](https://www.digikey.com/en/products/detail/e-switch/RE111C1021-116/4331944))
) which when pressed will shut down the
entire UV light circuit.

The circuit will be powered using an 311013-01 plug which connect to both the relay and switch.

