# Board Considerations
Due to restrictions on PCB orders in ECE 445, our design will shift to consist of one PCB with a single microcontroller that controls the lights, motor and photosensor. 
Connectors and wires will connect each component to the control PCB. There are a few major considerations left still.

## Power
The recent changes to the design changed this project from a low power to mid power design. As such, the power supply will have to be capable of handling the 60 Watts of power dissipated by the LEDs at full light as well as by other design components. The following [power supply 
](https://www.amazon.com/ALITOVE-100-240V-Converter-Transformer-5-5x2-1mm/dp/B07MXXXBV8/ref=sxin_15_pa_sp_search_thematic_sspa?content-id=amzn1.sym.6b029eb3-7d41-4744-b45d-69fe835e098d%3Aamzn1.sym.6b029eb3-7d41-4744-b45d-69fe835e098d&cv_ct_cx=12v+15+amp+power+supply&keywords=12v+15+amp+power+supply&pd_rd_i=B07MXXXBV8&pd_rd_r=39865509-9d64-417a-bc5e-366efbf2829f&pd_rd_w=7I11j&pd_rd_wg=hmNNq&pf_rd_p=6b029eb3-7d41-4744-b45d-69fe835e098d&pf_rd_r=CDZPZD2ZX2RHV2VJX3BZ&qid=1665428790&qu=eyJxc2MiOiI0LjE4IiwicXNhIjoiMy44MCIsInFzcCI6IjMuMDcifQ%3D%3D&sr=1-3-a73d1c8c-2fd2-4f19-aa41-2df022bcb241-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzNVJHS0xON1lYRzZDJmVuY3J5cHRlZElkPUEwMTAzNTA3MzlGSDhHRFo4WlFVNyZlbmNyeXB0ZWRBZElkPUEwMjgyMTM3MkFFNzJJQk1aMUxJWiZ3aWRnZXROYW1lPXNwX3NlYXJjaF90aGVtYXRpYyZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=) was selected as it has a high power rating as well as a nominal voltage rating of 12V. The design is well beyond the recommended maximum of 96W designs. 

This 12V will then be stepped down to 3.3V for the microcontroller as well as the motor.
