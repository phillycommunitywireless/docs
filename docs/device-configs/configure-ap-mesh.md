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

![Reset Button](../assets/images/mesh/Reset.jpeg)
![Ports](../assets/images/mesh/Ports.jpeg)
![Wiring](../assets/images/mesh/Wiring.jpeg)

### Connect the AP to your computer

We need to connect the device to our computer and determine its IP address, while also making sure it also has a route to the Internet. There are two ways to do this:

#### If you have physical access to your WiFi router

1. Plug the `LAN` port of the PoE injector directly into an Ethernet port on your router. 
2. The AP will get the IP address `192.168.1.20` from your router. [Skip to the SSH step](#connect-to-the-ap-using-ssh).

#### If you don't have access to your router

1. Connect the `LAN` port of the injector to your computer, using the USB Ethernet adapter if you don't have an Ethernet port.
2. Make sure your computer is connected to WiFi.
3. Follow these instructions to configure your Ethernet adapter and obtain an IP for the device: [Sharing a WiFi connection over Ethernet](./shared-connection.md)

### Connect to the AP using SSH

1. Open a command line prompt.
2. Run the command `ssh ubnt@192.168.1.20`
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

### Adopt AP Mesh Unit

!!! info "" 

    You will need access to the PCW Unifi controller interface to complete this step.

1. From your `ssh` shell, run the command `set-inform http://unifi.phillycommunitywireless.org:8080/inform`. This will send a message over the internet to our controller, letting it know the device wants to be adopted.

!!! warning ""

    If your prompt hangs here, your AP probably doesn't have a route to the internet. [Return to the connection step](#connect-the-ap-to-your-computer) and make sure your setup follows those instructions.

2. Open the Unifi portal in your browser, and navigate to the device list. The AP should appear in the list of devices awaiting adoption.
4. Press `Adopt` to adopt the AP Mesh Unit.

## Troubleshooting

### Computer doesn't recognize AP Mesh Unit in Network settings, or `ssh` command fails.

The AP Mesh Unit can take a few minutes to boot after being plugged in, so wait until the status light is solid white and try again.

### What does this status light pattern mean?

Refer to this article: [LED Color Patterns for UniFi Devices](https://help.ui.com/hc/en-us/articles/204910134-UniFi-LED-Color-Patterns-for-UniFi-Devices)
