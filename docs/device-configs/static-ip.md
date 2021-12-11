---
title: Sharing a WiFi connection over Ethernet

---
# Sharing a WiFi connection over Ethernet

This article contains instructions for connecting to a device over Ethernet and sharing your computer's existing WiFi Internet connection with that device. In other words, your computer will be acting as a gateway for the device you connect to it, and that device will be able to send packets to the Internet through your computer.

This is useful when you cannot connect the device directly to your router. We use it as an option in our config instructions for the [EdgeRouter X](../configure-erx) and the [Unifi Mesh AP](../configure-ap-mesh).

Choose your computer's OS:

[Ubuntu](#ubuntu) <br>  
[MacOS](#macos) (_TBD_) <br>  
Windows (_TBD_)

## Ubuntu

_This is the preferred environment. PCW computers will be using Ubuntu 20.04._

1. Open your `Settings` > `Network`.
2. Under the `Wired` section, click the plus sign to create a new settings profile. Name the profile "Shared" or whatever you want. ![Ubuntu Network Settings 1](../assets/images/shared-connection/ubuntu1.png)
3. In the **IPv4** tab, choose "Shared to other computers". Click Apply. Your computer should now be networked with the connected to device on the 10.42.0.0/24 subnet (10.42.0.*)
4. Open a terminal. Type the following to scan the devices in that IP range:

       nmap -sn 10.42.0.0/24 | grep report

   You should see two lines beginning with "`nmap scan report`". Find the line with an IP address that does not end with "`.1`", and copy that IP address.
5. In the same terminal window, type the following:

       ssh <username>@<IP you just copied>

   You'll be prompted for a password.

Once you've connected to the device, you can type the following to test whether it has a route to the Internet:

    ping 1.1.1.1

If you see packets start to appear (`64 bytes from...`), you got it!

## MacOS

1. Open up `System Preferences` > `Network`.
2. Select the Ethernet connection you have with the device you'd like to configure.
   ![Mac Network Settings 1](../assets/images/shared-connection/mac1.png)
3. Change the value of `Configure IPv4` to `Manually`.
   ![Mac Network Settings 2](../assets/images/shared-connection/mac2.png)
4. Set the IP Address to `192.168.1.2`.
5. Set the Subnet Mask to `255.255.255.0`
   ![Mac Network Settings 3](../assets/images/shared-connection/mac3.png)
6. Click `Apply`

## Details

These steps use `192.168.1.2` as the static IP, but it can be anything within the `192.168.1.0/24` range (`.0-.255`) except for `.0` (network), `.1` (gateway), `.20` (the mesh AP's default IP), and `.255` (broadcast).