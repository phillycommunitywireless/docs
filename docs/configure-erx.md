# Configure ERX Router

This guide will walk you through configuring a Ubiquiti EdgeRouter X.

## Required Hardware
- [ERX Router](https://store.ui.com/collections/operator-edgemax-routers/products/edgerouter-x) and power cable
- Ethernet cable
- Computer
- USB Ethernet adapter (if computer doesn't have ethernet port)

![Hardware](../assets/images/erx/hardware.jpg)

## Setup Steps

### Set static IP on computer

See [./static-ip](./static-ip.md)

### Wire up ERX

1. Plug the ERX into its power cable, and plug the power cable into an outlet.
2. Connect the `eth0` port of the ERX to your computer with an Ethernet cable, using the USB Ethernet adapter if you don't have an Ethernet port.

![Ports](../assets/images/erx/wiring.jpeg)
![Ports](../assets/images/erx/eth0.jpeg)

### Configure ERX

1. Download the [ERX config file](../assets/configs/erx-config.tar.gz)
2. Navigate to the portal at [https://192.168.1.1](https://192.168.1.1) in your browser
3. Log into the portal with username `ubnt`, password `ubnt`.
![Login](../assets/images/erx/login.jpeg)

4. On the `Use wizard?` prompt, press no.
![Login](../assets/images/erx/wizard.jpeg)

5. Press the `System` tab on the bottom of the page.
6. Under the `Restore Config` section, press `Upload a file` and select the ERX config file you downloaded.
![Login](../assets/images/erx/system.jpeg)

7. The ERX will reboot using the new configuration.
8. That's it! If you need to do more configuration, you can log back into the portal using the username `pcwadmin`, and a password that you can get from the project maintainers.
