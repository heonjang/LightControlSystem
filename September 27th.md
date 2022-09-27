# Design

## Changes

The changes we made to our design are as follows:

#### UV Lights
The design will use srd-05vdc-sl-c relays to switch on and off the lights. These are 5V relays, so the output from the micrcontroller 
will be stepped up from 3.3 to 5V using the L6920DC converter. After a conversation with Jack Belvins, a UIUC alum, the circuit for the UV
lights will be isolated on its own board. Additionally, an emergency shutoff will be implemented. As safety is paramount in this project, 
surge protection will be added to the design.

## Design Details
Currently the following topics are still in progress and require further discussion and thought

#### Safety
- The UV lights are hot, a method of preventing consumers from touching the light bulbs directly should be added
- The potential for fire is a concern. Surge protection would prevent fires. Ensuring the design doesn't overload the power source is crucial as well.

#### Power
- Wall outlets will be used to power the design. The current design has two major power systems, calculations on the load on these systems still needs
to be done


## Next Steps
Schematics will need to be updated and finished relatively soon. Additional research will be done to decide the best UV lights for the design.
