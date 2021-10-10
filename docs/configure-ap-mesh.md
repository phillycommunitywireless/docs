# Configure AP Mesh

This guide will walk you through configuring a Ubiquiti Access Point Mesh so it can be adopted by the PCW network.

## Required Hardware

- AP Mesh Unit - [Ubiquiti Mesh Dual-Band Access Point](https://store.ui.com/products/unifi-ac-mesh-ap) (white Ubiquiti antenna with bunny ears)
- PoE injector
- Ethernet cable
- Computer
- USB Ethernet adapter (if computer doesn't have ethernet port)
- Power strip/extension cord
- Paperclip

![Materials](assets/images/mesh/Materials.jpeg)

## Setup Steps

### Set static IP on computer

See [./static-ip](./static-ip.md)

### Wire up your AP Mesh Unit.

1. Plug the PoE injector into an outlet, or power strip.
2. Connect the `POE` port of the injector to the AP Mesh Unit with an ethernet cable.
3. Connect the `LAN` port of the injector to your computer, using the USB Ethernet adapter if you don't have an Ethernet port.
   ![Ports](../assets/images/mesh/Ports.jpeg)
   ![Wiring](../assets/images/mesh/Wiring.jpeg)

### Factory reset AP Mesh Unit.

The AP Mesh Units have had unexpected behavior even out of the box, so it is recommended to factory reset it before continuing.

1. With the paperclip, press the reset button at the bottom of the AP Mesh Unit in until it clicks. ![Reset Button](../../assets/images/mesh/Reset.jpeg)
2. Hold it pressed in for 15 seconds.
3. Once the status light on the AP Mesh Unit has flashed and then gone out, the device has been reset.

### Connect to the AP Mesh Unit.

1. Open a command line prompt.
2. If you have previously connected to an AP Mesh Unit, you will need to edit your `known_hosts` file, or you will get an `Host key verification failed` error.
   1. Open `~/.ssh/known_hosts` with `vim`, `nano`, or the text editor of your choice.
   2. Remove the line beginning with `192.168.1.20` (It will look something like `192.168.1.20 ssh-rsa AAAAB3NzaC1yc2E...`), and save the file.
3. Run the command `ssh ubnt@192.168.1.20`
4. You may see the alert:

   ```
   The authenticity of host '192.168.1.20 (192.168.1.20)' can't be established.
   RSA key fingerprint is SHA256:oUG6ABM3uor6lfBpJFcnHWyhhPnCrIx2Jf0U1+UAg4g.
   Are you sure you want to continue connecting (yes/no/[fingerprint])?
   ```

   Press yes to continue.

5. When prompted for the password, enter `ubnt`.
6. You should now be connected to the AP Mesh Unit.
   ![SSH Connection](../../assets/images/mesh/SSH.png)

### Adopt AP Mesh Unit

You will need access to the Philly Community Wireless HostiFi portal to complete this step.

1. From your `ssh` shell, run the command `set-inform http://unifi.phillycommunitywireless.org:8080/inform`.
   - This will alert the HostiFi controller that the AP Mesh Unit wants to be adopted.
2. Open the HostiFi portal in your browser, and navigate to the device list.
3. The AP Mesh Unit should appear in the list of devices awaiting adoption.
4. Press `Adopt` to adopt the AP Mesh Unit.

## Troubleshooting

1. Computer doesn't recognize AP Mesh Unit in Network settings, or `ssh` command fails.
   - The AP Mesh Unit can take a few minutes to boot after being plugged in, so wait until the status light is solid white and try again.
2. What does this status light pattern mean?
   - [LED Color Patterns for UniFi Devices](https://help.ui.com/hc/en-us/articles/204910134-UniFi-LED-Color-Patterns-for-UniFi-Devices)
