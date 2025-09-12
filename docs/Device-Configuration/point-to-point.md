---
title: Point-to-Point (PtP)
---

# Point-to-Point (PtP)

In addition to utilizing [PhillyWisper's](https://www.phillywisper.net) high sites, PCW also installs our own Point-to-Point (PtP) and Point-to-Multipoint (PtMP) wireless infrastructure. We utilize both 5 Ghz and 60 Ghz equipment. 

## 5 Ghz - airMAX 
PtP/PtMP use the terms "access point" and "station" to delineate between the source of the uplink and the remote end. 

### Configure the access point 
* Log in to the access point's management page via web browser - this will either be available over WiFi or Ethernet. 
* Set a static IP address for the access point. 
* Set a SSID and password for the PtP network. 
 
### Configure the station 
* Log in to the station's management page via web browser - this will either be available over WiFi or Ethernet. 
* Set a static IP address for the station in the same subnet as the access point.
* Enter the previously set SSID and password for the PtP network set on the AP. 
* Test connectivity - the access point and station should now be able to communicate with each other. 

During installation, adjust mounting and alignment as needed. 

## 60 Ghz - Unifi Building Bridges (UBBs)
* Adopt the devices - see the [Configure Unifi Mesh AP](configure-ap-mesh.md) for information on how to adopt devices. UBBs come as a pre-configured pair.
* Install the AP. 
* Install the station pointing at the AP. 
* If necessary, further align the devices - the LEDs will change color based off of alignment (blue = aligned, red/green = misaligned).  
* **If you need to reset the UBBs, ensure you reset BOTH the access point and station. Reset the station first. If you do not do this, re-adoption will fail!** 
