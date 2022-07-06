---
title: Sharing a WiFi connection over Ethernet
---

# Sharing a WiFi connection over Ethernet

This article describes how to connect to a device to your computer via Ethernet and share your computer's existing Internet connection with that device. In other words, your computer will be acting as a gateway and the connected device will be able to send packets via your computer to the Internet.

This is useful when you need a device to be able to access the internet while networked with your computer, but you do not have access to your router. We use it as an option in our config instructions for the [Unifi Mesh AP](../configure-ap-mesh).

Choose your computer's OS:

**[Ubuntu](#ubuntu)**  
**[MacOS](#macos)**  
Windows (_TBD_)

## Ubuntu

_This is the preferred environment. PCW computers will be using Ubuntu 20.04._

1.  Open your `Settings` > `Network`.

2.  Under the `Wired` section, click the plus sign to create a new settings profile. Name the profile "Shared" or whatever you want.

3.  In the **IPv4** tab, choose "Shared to other computers". Click Apply. Your computer should now be networked with the AP. 10.42.0.0/24 is the default subnet used by Ubuntu for this setup, but there's not necessarily a guarantee that your computer will use that subnet. If the next step returns no results, run `ip address` or `ifconfig` and look for the IP of your Ethernet interface (usually `eth0`) there.

4.  Open a terminal. Type the following to scan the devices in that IP range:

        nmap -sn 10.42.0.0/24 | grep report

    You should see two lines beginning with "`nmap scan report`". Find the line with an IP address that does not end with "`.1`", and copy that IP address.

If the nmap command hangs, you can also try the Mac OS directions on Ubuntu Linux and it should work fine.

## MacOS

_Begin these steps with the AP not connected to your computer via an ethernet port or adapter._

1.  Open `Sharing` from your `System Preferences` menu -> select `Internet Sharing` in the list on the left -> select the interfaces you want to enable sharing for -> click the box next to `Internet Sharing` to turn it on -> a warning dialog box will come up, so click `Start`.

2.  Run `arp -a | grep -v incomplete` to show a mapping of ip address to mac address for the devices on your network.

3.  Connect the ap to your machine or adapter and run `arp -a | grep -v incomplete` again. The difference between this and the previous grep output should be the AP. Note the IP address and MAC address.

4.  To confirm that the AP has a route to the internet, you can run the same commands as specified in step 5 of the Ubuntu instructions above (ssh, ping, etc.).

Note: These instructions were developed on a MacBook running Catalina, version 10.15.7.
