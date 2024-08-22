---
title: Troubleshooting Devices
---

Not every device will work perfectly. Additionally, devices deployed outdoors will be exposed to the elements, primarily heat and moisture, and degrade naturally over time. 

## Troubleshooting Access Points
### No power on access point; device power cycles but doesn't stay online 
**Observations**: No lights, device is offline/missing from controller.

**Potential Causes and Fixes**:

* **Inadequate power supply** - Check the PoE injector connected to the device and ensure the light is on, and that the voltage is correct.
* **Flawed power connection/Ethernet cable if PoE** - Test if a different Ethernet cable delivers power to check the PoE injector is working correctly. Re-test the flawed cable.

### Cannot SSH into AP to adopt
* **Observations** - Lights are on and device appears online, but is unreachable via SSH.

**Potential Causes and Fixes**

* **Assigned a non-default IP address** - The factory configuration of most Unifi devices sets their IP to `192.168.1.20` pre-adoption; however, if that address is already taken, the device may be assigned another IP address. Try using `arp -a` to find the AP.
* **Ensure your static IP address is correctly assigned** - Review the instructions in [Setting a static IP](/device-configs/static-ip) and ensure you are using the `192.168.1.x` subnet.

### Adoption request sent, but device doesn't appear in controller
* **Observations** - Device appears online and adoption request sent via `sudo set-inform`, but adoption request does not appear in controller.

**Potential Causes and Fixes**

* **Ensure the device is connected to the Internet** - Review the instructions in [Sharing a WiFi connection over Ethernet](/device-configs/shared-connection) and ensure the AP can access the Internet
* **Refresh the controller** - There can sometimes be a delay in sending the request and the request appearing in the controller.

## Troubleshooting ERXs
### No power on ERX
**Observations**: No lights, device is offline/missing from UISP.

**Potential Causes and Fixes**:

* **Flawed power connection/Ethernet cable if PoE** - Test the ERX with a different 9v power supply and check if the ERX comes online. Try switching to a different 9v power supply. If using PoE, ensure the voltage is correct.
