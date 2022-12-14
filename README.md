# esptemp8c
Open source, 8-channel temperature logger using esphome for Dallas DS18B20 sensors.

<img src="images/esptemp8c.png" width=50%/> <img src="images/case1.png" width=50%/>

## Tindie store
This is available for purchase via my [tindie store](https://www.tindie.com/products/gcormier/esptemp8c).

## Sensors
They can be found at various locations, including [DFRobot](https://www.dfrobot.com/product-689.html), [Adafruit](https://www.adafruit.com/product/381), Digikey or the usual suspects.

You will need to find out your sensor ID's as per the [esphome documentation](https://esphome.io/components/sensor/dallas.html).

In theory, this unit can handle more then 8 sensors if you start piggy-backing the terminals for multiple sensors.

## Powering
Only *one* power source should be used.
- USB-C Jack (5V)
- Screw terminal
    - It is designed for 24VAC. 12VAC is probably the minimum required for AC, and you might get away with up to 30VAC.
    - 9VDC will be the minimum required amount if using DC, and it has been tested up to 24VDC. 

A self-resetting polyfuse is included to protect HVAC equipment if sourcing 24VAC from these units. The polyfuse does NOT apply to power from the USB-C port, as the device supplying power should have overcurrent protection.

## Flashing
You can use any ESP32 programmer and connect the proper pins to the programming header next to the ESP32. The programmer will need to trigger GPIO0/EN pins accordingly, or you will need to wire up your own buttons to do so. The programming pinout matches the [eflashy32](https://github.com/gcormier/eflashy32) ESP32 programmer.

## Enclosure
Fits in a [Hammond 1593VBK](https://www.hammfg.com/part/1593VBK). Or you can make your own enclosure and 3D-print it (contributions welcome).
