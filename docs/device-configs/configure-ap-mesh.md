---
title: Configure Unifi AP
---

# Configuring Unifi APs (UAP-AC-M and UAP-AC-M-PRO)

This guide will walk you through configuring a Ubiquiti Access Point AC Mesh ("bunny ears"), which consists of a few steps:

- Connect the device to your computer, and make sure it has a route to the Internet
- Update the device's firmware to the latest stable version, 4.3.20
- Inform the device of the URL of our Unifi controller
- Adopt the device via the controller interface

## You will need

| Item                                         | Purpose                                           |
| -------------------------------------------- | ------------------------------------------------- |
| Unifi Access Point                           | Unit to be configured                             |
| Power-over-Ethernet injector (comes with AP) | Supplies power to the AP                          |
| 2 Ethernet cables                            | One powers AP, one provides data link to computer |
| USB Ethernet adapter                         | If your computer doesn't have an Ethernet port    |
| Computer running MacOS or Linux              | Perform remote configuration                      |
| Wall outlet                                  |                                                   |
| Paperclip (or other thin item)               | Performing a factory reset                        |

![Materials](../assets/images/mesh/Materials.jpeg)

## Setup Steps

### Power the device

1. Plug the PoE injector into an outlet, or power strip.
2. Connect the `POE` port of the injector to the AP Mesh Unit with an ethernet cable. You should see a white light turn on.

!!! info ""

    The light will be blue if the device has an existing configuration. Don't worry, we'll factory reset the device next.

### Factory reset

The AP Mesh Units have had unexpected behavior even out of the box, so it is recommended to factory reset it before continuing.

1. With the paperclip, press the reset button at the bottom of the AP Mesh Unit in until it clicks.
2. Hold it pressed in for 5 seconds.
3. The status light on the AP should flash, then go out as the device reboots. When it comes back on it should be solid white, indicating the reset was successful.

<img src="../../assets/images/mesh/Reset.jpeg" width="30%">
<img src="../../assets/images/mesh/Ports.jpeg" width="30%">
<img src="../../assets/images/mesh/Wiring.jpeg" width="30%">

### 1. Connect the AP to your computer

We need to connect the device to our computer and determine its IP address, while also making sure it also has a route to the Internet. The Unifi mesh aps should automatically reset to `192.168.1.20` so you can first try Step 2 and see if the ssh command works. 

If the mesh AP's IP address isn't `192.168.1.20`, there are two ways to find the IP address: a) connect to local router b) connect to your computer. We usually do option b) connect the AP directly to our computer.

#### a) If you have physical access to your WiFi router

1. Plug the `LAN` port of the PoE injector directly into an Ethernet port on your router. 
2. The AP will get the IP address `192.168.1.20` from your router. [Skip to the SSH step](#connect-to-the-ap-using-ssh).

#### b) If you don't have access to your router

1. Connect the `LAN` port of the injector to your computer, using the USB Ethernet adapter if you don't have an Ethernet port.
2. Make sure your computer is connected to WiFi.
3. Follow the directions on [Sharing a WiFi connection over Ethernet](shared-connection.md) to share your computer's wireless connection with the AP.
4. Follow the instructions here: [Setting a static IP for your computer](./static-ip.md) to set your IP address.

### 2. Connect to the AP using SSH

1. At the terminal, run the command `ssh ubnt@192.168.1.20` or replace the default IP address with the one you copied.
3. You may see "`The authenticity of host [...] can't be established`". Type "yes" and press Enter.
4. When prompted for the password, enter `ubnt`.
5. You should now be connected to the AP Mesh Unit.

   ![SSH Connection](../assets/images/mesh/SSH.png)

!!! warning ""

    If you you get a `Host key verification failed` error, you'll need to edit your `known_hosts` file.
    1. Open `~/.ssh/known_hosts` with `vim`, `nano`, or the text editor of your choice.
    2. Remove the line beginning with `192.168.1.20` (It will look something like `192.168.1.20 ssh-rsa AAAAB3NzaC1yc2E...`), and save the file.

### Set the device firmware version

We use device firmware version 4.3.20, [on the advice of the good people at NYCMesh](https://docs.nycmesh.net/hardware/unifi-ap/).

1. While connected to the device via SSH, type `upgrade https://dl.ui.com/unifi/firmware/U7PG2/4.3.20.11298/BZ.qca956x.v4.3.20.11298.200704.1347.bin`
2. You will be disconnected from the device. Wait until it reboots and the light is solid white (you can `ping` the IP address to test if it's up, or just try SSHing), then SSH back in.
3. If it hangs, try canceling out and re-running the command
4. You can verify the firmware upgrade by looking at the header to your command line input, which provides the firmware version like "UBNT-BZ.v4.3.20#".

!!! warning ""

    If the firmware upgrade hangs forever, skip this step. The firmware can also be upgraded through Hostifi after the AP is adopted.
    

### Adopt AP Mesh Unit

!!! info "" 

    You will need access to the PCW Unifi controller interface to complete this step.

1. From your `ssh` shell, run the command `set-inform http://unifi.phillycommunitywireless.org:8080/inform`. This will send a message over the internet to our controller, letting it know the device wants to be adopted.

!!! warning ""

    If your prompt hangs here, your AP probably doesn't have a route to the internet. [Return to the connection step](#connect-the-ap-to-your-computer) and make sure your setup follows those instructions.

2. Open the Hostifi portal in your browser, and navigate to the device list. The AP should appear in the list of devices awaiting adoption.
4. Press `Adopt` to adopt the AP Mesh Unit.
5. Adoption can take a while. Try refreshing the Hostifi portal and/or browser. 
6. You will be prompted to choose a Group for the AP. Choose All AP's and press save.
7. Go back to the main Dashboard to see if the device has been adopted.
8. If the device hangs during adopt, try to Forget it. Try the `set inform` command again.
10. Change the settings to add your name and a number for each device you configure. The admin team will relabel devices upon install.
11. To upgrade firmware from within the controller, go to the device and open the Settings. Under Manage, find the Location URL field, and paste the link for the firmware version (`https://dl.ui.com/unifi/firmware/U7PG2/4.3.20.11298/BZ.qca956x.v4.3.20.11298.200704.1347.bin`), then press Update.
12. Further configurations of the device can be adjusted in the settings, but it is better to leave radio settings as default until installed on the network.


## Troubleshooting

### Computer doesn't recognize AP Mesh Unit in Network settings, or `ssh` command fails.

The AP Mesh Unit can take a few minutes to boot after being plugged in, so wait until the status light is solid white and try again.

See our separate doc for more info on related problems: [Sharing a WiFi connection over Ethernet](shared-connection.md)

### What does this status light pattern mean?

Refer to this article: [LED Color Patterns for UniFi Devices](https://help.ui.com/hc/en-us/articles/204910134-UniFi-LED-Color-Patterns-for-UniFi-Devices)
