# Antenna Installation

Philly Community Wireless has partnered with PhillyWisper to install antennas for the free wifi network on rooftops in the Norris Square Park neighborhood. PhillyWisper is a wireless internet service provider (WISP) which means our project delivers the internet the "last mile" to our customers using radio technology.

## Rooftop Installation Process

Most installations proceed in the following order:

1. Survey the building and rooftop to assess Line of Sight (LOS) to the highsite source tower for broadband signal
2. Install antenna on rooftop and run cable into building
3. Configure wifi router and mesh kits (For more info, see our [Configure AP-Mesh Guide](./configure-ap-mesh.md) and our [Configure ERX Router Guide](./configure-erx.md))
4. Potentially install wall-mounted antenna to propagate signal down the street

## Length of Time for Antenna Installations

Typically, installs take between two and four hours to complete, but in certain cases they can take longer. The full installation process, from a rooftop antenna to a wall-mounted mesh kit, can involve 2-3 visits, each involving an hour or two of work. .

# Hardware for Installation

Rooftop installs consist of a rooftop antenna, a power-over-Ethernet injector, a router, and a mesh access point. Philly Community Wireless and Philly Wisper primarily deploy Ubiquiti radios and networking equipment. As each roof is different, the installation is customized for each location to ensure the most secure placement according to industry standards.

In general, we will install a Ubiquiti LiteBeam antenna on the roof of the home, which receives signal from a PhillyWisper tower. The antenna is wired into the home via an Ethernet cable. Currently, this part of the install must be completed by a PhillyWisper technician. For installation purposes, this means PhillyWisper technicians will need to mount a small radio antenna (approx 14" x 11" x 11") at roof height and precision aim it at the closest tower.

PhillyWisper takes every effort to minimally impact buildings during installation.  They use non-invasive techniques when mounting the radio (see attached images of various mounting techniques below). They never penetrate the roofing system itself and they try and utilize preexisting structures (chimneys, vent pipes, etc) when possible.  

If preexisting structures aren't an option, they will use a non-penetrating roof mount, which is properly weighed down and rests on a rubber mat on top of your roof. They then secure an outdoor-rated, UV stabilized network cable from the radio on the roof, down along the building exterior, and inside where your WiFi router will be located.  

Both PhillyWisper and Philly Community Wireless make sure the wire run is as inconspicuous as possible and ensure there is plenty of tension on the wire so that it doesn't flap in the wind.  If there are any preexisting penetrations entering the building from previous ISPs, they will use that if possible and caulk when finished.

## Installation Examples

### Non-Penetrating Roof Mounts

We utilize non-penetrating roof mounts (NPRM). A thick rubber mat is placed below the NPRM to protect the roof. Cinder blocks are used as ballast to secure the NPRM:  

![Non-penetrating roof mount 1](../assets/images/install/image1.jpg)
![Non-penetrating roof mount 2](../assets/images/install/image2.jpg)

### Wall-Mounted Antennas

The following image displays two wall-mounted masts with radios along with an outdoor switch and junction box.

The mast on the left has a Ubiquiti AF-24 radio that operates at 24 GHz and provides a 1.4 Gbps back-haul connection to the data center.

![Wall mounted antenna 1](../assets/images/install/image6.jpg)
![Wall mounted antenna 2](../assets/images/install/image7.jpg)
![Wall mounted antenna 3](../assets/images/install/image8.jpg)
![Wall mounted antenna 4](../assets/images/install/image9.jpg)

The mast on the right has PTMP radios with symmetrical horn antennas. The radios provide service to individual customers.

The square-ish white device between and below the masts is a Ubiquiti EP-S16, an outdoor rated network switch. 54 VDC power is supplied to the EP-S16 which in turns provides power to the radios using POE (power of Ethernet).

# Mesh-kit Install for Rooftop Antenna Hosts

Hosts of rooftop installations will also host a router in the house near the window to the front of the house. In some cases we may install a wall-mounted antenna on the outside of the house to propagate the broadband signal throughout the neighborhood.

We provide a kit with a PoE injector and a bunny-ears mesh AP. Philly Community Wireless can install the kit, or the resident can install the bunny ears in any location within their home, as long as other mesh APs are within radio range (we’re planning on suggesting the entrance of the house or the porch -- the APs are weatherproof).

## Mesh Kit Overview

The Ethernet cable is passed through a Power-over-Ethernet (PoE) injector, which adds power to the signal the Ethernet cable is carrying and allows downstream devices to be powered solely through Ethernet.

![PoE Injector](../assets/images/install/image4.jpg)

The powered Ethernet cable is wired to a Ubiquiti EdgeRouter-X (or possibly another router in the future) configured to support mesh networking. The router handles traffic for each of the access points (APs) it is meshed with.

![EdgeRouter-X](../assets/images/install/image5.jpg)

Finally, a Ubiquiti Mesh AP (“bunny ears” because look at them!) is connected to the router and allows devices in its radio signal range to connect to the network. The bunny ears should be installed in a location that is radio-visible to the mesh APs at the home installs in range.

![Ubiquiti Mesh AP](../assets/images/install/image3.jpg)

For more information on the mesh kit, see our [Configure AP-Mesh Guide](./configure-ap-mesh.md)
