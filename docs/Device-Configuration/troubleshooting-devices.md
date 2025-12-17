---
title: Troubleshooting
---

Not every device will work perfectly. Additionally, devices deployed outdoors will be exposed to the elements, primarily heat and moisture, and degrade naturally over time. 

## Unifi AP LED Status Indicators

Each Unifi AP has an LED which indicates its current status. 

* **LED Off** - The AP is offline. 
* **Flashing White** - The AP is receiving power and booting up 
* **Steady White** - The AP has finished configuration and is ready for adoption. 
    * See [Configure Unifi Mesh AP](/Device-Configuration/configure-ap-mesh) for adoption instructions. 
* **Steady Blue** - The AP is adopted and operating normally; in our case, broadcasting the Philly Community Wireless network. 
* **Flashing White/Blue** - The AP's firmware is being updated. **Do not unplug the AP**.
* **Flashing Blue** - The AP has lost connectivity and is searching for a parent AP or uplink. 
* **Rapid Flashing Blue/Off** - The 'Locate' feature was activated via the Unifi Controller.  

Please see [this page](https://help.ui.com/hc/en-us/articles/204910134-Understanding-Device-LED-Status-Indicators) for more information on LED status indicators. 

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
* **Ensure your static IP address is correctly assigned** - Review the instructions in [Setting a static IP](/Device-Configuration/static-ip) and ensure you are using the `192.168.1.x` subnet.

### Adoption request sent, but device doesn't appear in controller
* **Observations** - Device appears online and adoption request sent via `sudo set-inform`, but adoption request does not appear in controller.

**Potential Causes and Fixes**

* **Ensure the device is connected to the Internet** - Review the instructions in [Sharing a WiFi connection over Ethernet](/Device-Configuration/shared-connection) and ensure the AP can access the Internet
* **Refresh the controller** - There can sometimes be a delay in sending the request and the request appearing in the controller.

### Device is 'isolated'
* **Observations** - Device marked as 'isolated' in Unifi controller

**Potential Causes and Fixes**

* **Device losing connectivity upstream** - An AP will become 'isolated' if it can no longer connect with the Unifi controller. Ensure that no changes have been made to the network configuration that would block the AP from communicating with the controller. First, power-cycle the AP (disconnect from PoE injector, or `ssh` remotely and run `reboot`.). If the AP is meshed, hard-wiring it without power-cycling may also get it back on the network. If unsuccessful, remove and re-adopt the AP. If the problem persists, power-cycle the ERX or clear the DHCP leases. 

## Troubleshooting ERXs
### No power on ERX
**Observations**: No lights, device is offline/missing from UISP.

**Potential Causes and Fixes**:

* **Flawed power connection/Ethernet cable if PoE** - Test the ERX with a different 9v power supply and check if the ERX comes online. Try switching to a different 9v power supply. If using PoE, ensure the voltage is correct.

## Useful Terminal Commands for Networking 
* `ipconfig` (Windows)/`ifconfig` (Unix) - display network interfaces and related information - IP address, subnet mask, and default gateway. 
* `arp -a` (Windows/Unix)- Show the Address Resolution Protocol (ARP) table - the mapping of IP addresses/MAC addresses. 
    * `ip neigh show` - Equivalent command.  
