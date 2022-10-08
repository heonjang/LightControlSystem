## General Design Updates

### LEDs
Since each grow light module has one red, one green and one blue LED, it would be beneficial to consolidate these and buy one RGB LED. The main
benefits being cost and design simplicity. Additionally, this will greatly reduce the amount of soldering and further modularize the design.

| LED      | Cost | Intensity | Comments |
| ----------- | ----------- |  ----------- |  ----------- |
| [UV](https://www.mouser.com/ProductDetail/Kingbright/AA3528VRVFS-A?qs=rY7msk5yxfb63mh907EyRA%3D%3D) (315-400 nm)     | $0.67      |  250mcd |  ----------- |
| [RGB](https://www.digikey.com/en/products/detail/creeled-inc/CLV1A-FKB-CK1VW1DE1BB7C3C3/7907693) | $0.42 |  710mcd Red, 1450mcd Green, 310mcd Blue |  ----------- |
| **Total**  | $1.09        |  ----------- |  ----------- |


| LED      | V_on | Desired I | Corresponding Resistor |Final Resistor Choice |Cost |
| ----------- | ----------- |  ----------- |  ----------- |----------- | ----------- |
| UV | 3.3V |  20mA |  85 ohms | [100 ohm](https://www.digikey.com/en/products/detail/stackpole-electronics-inc/RMCF1210JT100R/1757185) | $0.11 |
| Blue | 3.2V |  20mA |  90 ohms | [90.9 ohms](https://www.digikey.com/en/products/detail/stackpole-electronics-inc/RMCF0603FT90R9/1760976) |$0.10|
| Yellow-Red | 2V |  20mA |  150 ohms | [150 ohms](https://www.digikey.com/en/products/detail/stackpole-electronics-inc/RMCF0805FT150R/1760641) |$0.10 |
| Green | 3.2V |  20mA |  90 ohms| [90.9 ohms](https://www.digikey.com/en/products/detail/stackpole-electronics-inc/RMCF0603FT90R9/1760976) | $0.10 |
| **Total** | ----------- |  ----------- |  ----------- |----------- | $0.41 |
