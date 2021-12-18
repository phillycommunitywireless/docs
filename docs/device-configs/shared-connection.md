---
title: Sharing a WiFi connection over Ethernet
---

# Sharing a WiFi connection over Ethernet

This article describes how to connect to a device to your computer via Ethernet and share your computer's existing Internet connection with that device. In other words, your computer will be acting as a gateway and the connected device will be able to send packets via your computer to the Internet.

This is useful when you need a device to be able to access the internet while networked with your computer, but you do not have access to your router. We use it as an option in our config instructions for the [Unifi Mesh AP](../configure-ap-mesh).

Choose your computer's OS:

**[Ubuntu](#ubuntu)**  
MacOS (_TBD_)  
Windows (_TBD_)

## Ubuntu

_This is the preferred environment. PCW computers will be using Ubuntu 20.04._

1.  Open your `Settings` > `Network`.
2.  Under the `Wired` section, click the plus sign to create a new settings profile. Name the profile "Shared" or whatever you want.
3.  In the **IPv4** tab, choose "Shared to other computers". Click Apply. Your computer should now be networked with the connected to device on the 10.42.0.0/24 subnet (10.42.0.\*)
4.  Open a terminal. Type the following to scan the devices in that IP range:

        nmap -sn 10.42.0.0/24 | grep report

    You should see two lines beginning with "`nmap scan report`". Find the line with an IP address that does not end with "`.1`", and copy that IP address.

5.  In the same terminal window, type the following:

        ssh <username>@<IP you just copied>

    You'll be prompted for a password.

Once you've connected to the device, you can type the following to test whether it has a route to the Internet:

    ping 1.1.1.1

If you see packets start to appear (`64 bytes from...`), you got it!

## Details

10.42.0.0/24 is the default subnet used by Ubuntu for this setup, but there's not necessarily a guarantee that your computer will use that subnet. If things don't seem to be working for you, run `ip address` or `ifconfig` and look for the IP of your Ethernet interface (usually `eth0`) there.
