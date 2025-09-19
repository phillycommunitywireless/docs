---
title: Installation Overview
---

# Installation Overview

Philly Community Wireless has partnered with [**PhillyWisper**](https://phillywisper.net/) to install antennas for our free WiFi network on rooftops in the Norris Square, Fairhill, and Kensington neighborhoods. PhillyWisper is a wireless internet service provider (WISP) which means our project delivers the internet the "last mile" to our customers using radio technology.

## Rooftop Installation Process

Most installations proceed in the following order:

1. **LoS Check** - A new address is submitted to us. We check if the address has line of sight (LoS) to a PhillyWisper high site using Google Earth and other mapping tools, as well as in-person building assessments. For more information, please see [Building Assessments](../buildingassessment) page.

2. **Install Planning** - If there is LoS, we communicate with the resident or community organization to determine their connectivity needs. This helps us determine what sort of access points and networking equipment to bring, as well as how much cable we will need. Once the logistics for the initial install are determined, an install date is set! 

3. **Establish uplink** - On the day of the install, PCW will begin by installing the uplink radio pointing back at a PhillyWisper high site, usually a [LiteBeam](https://store.ui.com/us/en/products/litebeam-5ac). This provides the internet connection. 

4. **Deploy access points** - Once the uplink is set up, we can begin running cable on the roof or through the buliding and deploying WiFi access points as needed, either indoors or outdoors. For more info, see our [Configure AP-Mesh Guide](../../Device-Configuration/configure-ap-mesh) and our [Configure ERX Router Guide](../../Device-Configuration/configure-erx)

During residential installs, we either broadcast a private network for the resident to use from the same access points broadcasting the public PCW network, or provide an additional router for the resident to have their own private network that gets its uplink from the PCW network. 

## Length of Time for Antenna Installations

Typically, installs take between two and four hours to complete, but in certain cases they can take longer. The full installation process, from a rooftop antenna to a wall-mounted mesh kit, can involve 2-3 visits, each involving an hour or two of work.

## Hardware for Installation

Rooftop installs consist of a rooftop antenna, a power-over-Ethernet injector, a router, and a mesh access point. Philly Community Wireless and PhillyWisper primarily deploy Ubiquiti radios and networking equipment. As each roof is different, the installation is customized for each location to ensure the most secure placement according to industry standards.

In general, we will install a Ubiquiti LiteBeam antenna on the roof of the home, which receives signal from a PhillyWisper tower. The antenna is wired into the home via an Ethernet cable. Currently, this part of the install must be completed by a PhillyWisper technician. For installation purposes, this means PhillyWisper technicians will need to mount a small radio antenna (approx 14" x 11" x 11") at roof height and precision aim it at the closest tower.

PhillyWisper takes every effort to minimally impact buildings during installation. They use non-invasive techniques when mounting the radio (see attached images of various mounting techniques below). They never penetrate the roofing system itself and they try and utilize preexisting structures (chimneys, vent pipes, etc) when possible.

If preexisting structures aren't an option, they will use a non-penetrating roof mount, which is properly weighed down and rests on a rubber mat on top of your roof. They then secure an outdoor-rated, UV stabilized network cable from the radio on the roof, down along the building exterior, and inside where your WiFi router will be located.

Both PhillyWisper and Philly Community Wireless make sure the wire run is as inconspicuously as possible and ensure there is plenty of tension on the wire so that it doesn't flap in the wind. If there are any preexisting penetrations entering the building from previous ISPs, they will use that if possible and caulk when finished.

## Installation Examples

### Non-Penetrating Roof Mounts

We utilize non-penetrating roof mounts (NPRM). A thick rubber mat is placed below the NPRM to protect the roof. Cinderblocks are used as ballast to secure the NPRM:

<figure style="display: flex; justify-content: center; align-items: center; flex-direction: column;">
    <img src="../../assets/images/installations/install/image2.jpg"
         alt=""
         style="width: 80%;">
    <figcaption>A non-penetrating roof mount</figcaption>
</figure>

<figure style="display: flex; justify-content: center; align-items: center; flex-direction: column;">
    <img src="../../assets/images/installations/install/image7.jpg"
         alt=""
         style="width: 80%;">
    <figcaption>Another example of a non-penetrating roof mount</figcaption>
</figure>

### Mounting on existing roof structures

We also often use j-arm mounts or previously existing mounts from previous telecommunications installations (old TV/Satellite antennas)to mount our equipment: 

<figure style="display: flex; justify-content: center; align-items: center; flex-direction: column;">
    <div style="display: flex; justify-content: center; align-items: center; flex-direction: column;">
        <img src="../../assets/images/installations/install/image8.jpg" width="80%">
    </div>
    <figcaption>LiteBeam mounted via J-arm on a chimmney</figcaption>
</figure>

<figure style="display: flex; justify-content: center; align-items: center; flex-direction: column;">
    <div style="display: flex; justify-content: center; align-items: center; flex-direction: column;">
        <img src="../../assets/images/installations/install/image9.jpg" width="80%">
    </div>
    <figcaption>A LiteBeam mounted on a previously-installed mast on a chimmney</figcaption>
</figure>


<!-- ### Wall-Mounted Antennas

The following image displays two wall-mounted masts with radios along with an outdoor switch and junction box.

The mast on the left has a Ubiquiti AF-24 radio that operates at 24 GHz and provides a 1.4 Gbps back-haul connection to the data center.

The mast on the right has PTMP radios with symmetrical horn antennas. The radios provide service to individual customers.

The square-ish white device between and below the masts is a Ubiquiti EP-S16, an outdoor rated network switch. 54 VDC power is supplied to the EP-S16 which in turns provides power to the radios using POE (power of Ethernet). -->

## Mesh-kit Install for Rooftop Antenna Hosts

Hosts of rooftop installations will also host a router in the house near the window to the front of the house. In some cases we may install a wall-mounted antenna on the outside of the house to propagate the broadband signal throughout the neighborhood.

We provide a kit with a PoE injector and a bunny-ears mesh AP. Philly Community Wireless can install the kit, or the resident can install the bunny ears in any location within their home, as long as other mesh APs are within radio range (we’re planning on suggesting the entrance of the house or the porch -- the APs are weatherproof).

### Mesh Kit Overview

The Ethernet cable is passed through a Power-over-Ethernet (PoE) injector, which adds power to the signal the Ethernet cable is carrying and allows downstream devices to be powered solely through Ethernet.

<figure style="display: flex; justify-content: center; align-items: center; flex-direction: column;">
    <img src="../../assets/images/installations/install/image4.jpg"
         alt="" style="">
</figure>

The powered Ethernet cable is wired to a Ubiquiti EdgeRouter-X (or possibly another router in the future) configured to support mesh networking. The router handles traffic for each of the access points (APs) it is meshed with.

<figure style="display: flex; justify-content: center; align-items: center; flex-direction: column;">
    <img src="../../assets/images/installations/install/image5.jpg"
         alt=""
         style="width: 50%;">
    <figcaption>Ubiquiti EdgeRouterX</figcaption>
</figure>

Finally, a Ubiquiti Mesh AP ("bunny ears" because look at them!) is connected to the router and allows devices in its radio signal range to connect to the network. The bunny ears should be installed in a location that is radio-visible to the mesh APs at the home installs in range.

<figure style="display: flex; justify-content: center; align-items: center; flex-direction: column;">
    <img src="../../assets/images/device-configs/mesh/Materials.jpeg"
         alt=""
         style="width: 50%;">
    <figcaption>A Unifi UAP-AC-Mesh, or "bunny ears"</figcaption>
</figure>


For more information on the mesh kit, see our [Configure AP-Mesh Guide](../../Device-Configuration/configure-ap-mesh)
