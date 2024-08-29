---
title: Configure EdgeRouter X
---

# Configure EdgeRouter X

This guide will walk you through configuring a Ubiquiti EdgeRouter X.

## Required Hardware

- [ERX Router](https://store.ui.com/collections/operator-edgemax-routers/products/edgerouter-x) and power cable
- Ethernet cable
- Computer
- USB Ethernet adapter (if computer doesn't have ethernet port)

<img src="../../assets/images/device-configs/erx/hardware.jpg" width="50%">

## Setup Steps

### Wire up ERX

1. Plug the ERX into its power cable, and plug the power cable into an outlet.
2. Connect the `eth0` port of the ERX to your computer with an Ethernet cable, using the USB Ethernet adapter if you don't have an Ethernet port.

<img src="../../assets/images/device-configs/erx/wiring.jpeg" width="50%">
<img src="../../assets/images/device-configs/erx/eth0.jpeg" width="50%">

### Configure your network settings

Follow the instructions here: [Setting a static IP for your computer](./static-ip.md)

### Configure ER-X using Wizard

1. Navigate to the portal at [https://192.168.1.1](https://192.168.1.1) in your browser
2. Log into the portal with username `ubnt`, password `ubnt`.
   <img src="../../assets/images/device-configs/erx/login.jpeg" width="50%">
4. On the `Use wizard?` prompt, press yes.
   <img src="../../assets/images/device-configs/erx/wizard.jpeg" width="50%">
5. Change the `Port` from `eth0` to `eth4.` This configures the port to serve as the WAN for the Litebeam antenna. 
6. Under `User Setup` create a new user and set the PCW username and password.
7. Press `Apply` and follow the instructions to Reboot the device.
8. Return to the portal and log in with the PCW username and password (contact project maintainers for this info).
9. At the `Dashboard,` click on `Actions` for `eth4` to turn on POE.
10. Finally, Click on the `System` tab at the bottom left of the console.
11. Input the host name for the device.
12. Set up the DNS address as 1.1.1.1.

To double check if a device is properly configured, check the settings under the `Dashboard` and `System` tabs. To verify WAN is set to `eth4,` visit the `Firewall/Nat` section. Under the NAT tab, see if `Masquerade` is set to `eth4` for the WAN masquerade.

### Configure ER-X using Config File

1. Download the [ERX config file](../assets/configs/erx-config.tar.gz)
2. Navigate to the portal at [https://192.168.1.1](https://192.168.1.1) in your browser
3. Log into the portal with username `ubnt`, password `ubnt` as above.
4. On the `Use wizard?` prompt, press no.
5. Press the `System` tab on the bottom of the page.
6. Under the `Restore Config` section, press `Upload a file` and select the ERX config file you downloaded.
   <img src="../../assets/images/device-configs/erx/system.jpeg" width="50%">
7. The ERX will reboot using the new configuration.
8. To do more configuration, you can log back into the portal using the PCW username and password.
9. Make sure to follow instructions (steps 11 and 12) to update the host name and DNS address in the `System` tab.

## Installation Setup

When installing the ER-X at a house with a rooftop Litebeam and a Mesh AP, remember the typical setup is:

1. Port `eth0` serves as the passthrough for POE from an adaptor plugged into an outlet.
2. Port `eth1` serves for the LAN port of the adapter powering the first PCW Mesh AP. Ports `eth2` and `eth3` can function for wired connections to additional Mesh APs, each of which need to be powered through separate POE adaptors.
4. Port `eth4`  serves as the WAN port with passthrough POE to communicate and provide power to the rooftop Litebeam. 
