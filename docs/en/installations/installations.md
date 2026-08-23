---
title: Installation Overview
---
# Installation Overview

Philly Community Wireless has partnered with [**PhillyWisper**](https://phillywisper.net/) to install antennas for our free WiFi network on rooftops in the Norris Square, Fairhill, and Kensington neighborhoods. PhillyWisper is a wireless internet service provider (WISP) which means our project delivers the internet the "last mile" to our customers using radio technology.

Philly Community Wireless seeks to build community-owned and community-operated wireless mesh network technologies. This page describes our process for installation and the type of network we are trying to build over a large expanse of the city. In a typical home network, all ['access points' (APs)](https://en.wikipedia.org/wiki/Wireless_access_point) are hard-wired to your router via Ethernet cable to create a wireless local area network. In a mesh network, access points can not only be hard-wired, but also connect to each other wirelessly, allowing a single Internet connection to be shared with significantly less infrastructure and labor than hard-wiring every single AP.

!!! info "Mesh"
    A mesh network is a type of local area network (LAN) composed of multiple nodes that work together to broadcast a WiFi signal over a large area. "Meshing" refers to the ability for multiple nodes to be linked together within the same network, expanding service range.

!!! info "Wi-Fi Access Point (AP)"
    A wireless network device that acts as a portal for devices to connect to a local area network. Access points are used for extending the wireless coverage of an existing network and for increasing the number of users that can connect to it.

## Rooftop Installation Process

Most installations proceed in the following order:

1. **Building Assessment** - A new address is submitted to us. We check if the address has [line of sight (LoS)](https://en.wikipedia.org/wiki/Line-of-sight_propagation) to a PhillyWisper high site using Google Earth and other mapping tools, and we conduct both remote and in-person building assessments as part of developing an install plan. For more information, please see [Building Assessments](buildingassessment.md) page.
2. **Install Planning** - If there is LoS, we communicate with the resident or community organization to determine their connectivity needs, as well as needs of neighbors and the general area. This helps us determine what sort of access points and networking equipment to bring, as well as how much cable we will need. Once the logistics for the initial install are determined, an install date is set!
3. **Establish uplink** - On the day of the install, PCW will begin by installing the uplink radio pointing back at a PhillyWisper high site, usually a [LiteBeam](https://store.ui.com/us/en/products/litebeam-5ac). This provides the internet connection.
4. **Deploy access points** - Once the uplink is set up, we can begin running cable on the roof or through the buliding and deploying WiFi access points as needed, either indoors or outdoors. For more info, see our [Configure AP-Mesh Guide](../device-configuration/configure-ap-mesh.md) and our [Configure ERX Router Guide](../device-configuration/configure-edgerouter-x.md)

!!! info "Line-of-sight (LoS)"
    Our wifi relies on "line of sight" between PhillyWisper sector antennas on high points and a rooftop (or otherwise) where we can install a radio to "draw in" wireless connectivity.

    [More on line-of-sight propagation](https://www.techtarget.com/whatis/definition/line-of-sight-LOS)

During residential installs, we either broadcast a private network for the resident to use from the same access points broadcasting the public PCW network, or provide an additional router for the resident to have their own private network that gets its uplink from the PCW network.

Below is a diagram of the resulting system. Attached to and inside the residential house silhouette are the outdoor and indoor devices PCW will install for you. The following sections describe our installation methods further in detail.

<figure style="display: flex; justify-content: center; align-items: center; flex-direction: column;">
    <img src="../../assets/images/installations/install/diagram.png"
         alt=""
         style="width: 85%;">
    <figcaption>Installation overview diagram</figcaption>
</figure>

## Length of Time for Antenna Installations

Typically, installs take between two and four hours to complete, but in certain cases they can take longer. The full installation process, from a rooftop antenna to a wall-mounted mesh kit, can involve 2-3 visits, each involving an hour or two of work.

## Hardware for Installation

<figure style="display: flex; justify-content: center; align-items: center; flex-direction: column;">
    <div style="display: flex; justify-content: center; align-items: center; flex-direction: column;">
        <img src="../../assets/images/installations/install/image8.jpg" width="80%">
    </div>
    <figcaption>LiteBeam (approx 14" x 11" x 11") mounted via J-arm on a chimmney</figcaption>
</figure>

Internet installations typically consist of a rooftop antenna, a power-over-Ethernet injector, a router, and a WiFi access point (all of which are typically Ubiquiti networking equipment). During installation, PhillyWisper and Philly Community Wireless take every effort to minimally impact buildings. At any given install site, our installation work will be customized to ensure the least invasive and most secure placement of networking equipment, according to industry standards.

For most locations, we first install a Ubiquiti LiteBeam radio antenna on the roof of the home, which receives signal from a nearby high site managed by PhillyWisper. To install the rooftop antenna, PhillyWisper technicians will access a high point and mount the small radio antenna (see attached images of various mounting techniques below) that they precision aim at the closest source tower. We never penetrate the roofing system itself when mounting the antenna, and wherever possible we utilize preexisting structures (chimneys, vent pipes, etc). If preexisting structures aren't an option, we use a non-penetrating roof mount, which is properly weighed down and rests on a rubber mat on top of your roof.

The rooftop radio is powered via outdoor-rated Ethernet cable that runs down the building exterior and into the home (our equipment uses Power over Ethernet, so we can power outdoor devices with Ethernet from an indoor outlet). We make sure the wire run is as inconspicuously as possible and ensure there is plenty of tension on the wire so that it doesn't flap in the wind. If there are any preexisting penetrations entering the building from previous ISPs, they will use that if possible and caulk when finished.

## Installation Examples

### Non-Penetrating Roof Mounts

We utilize non-penetrating roof mounts (NPRM). A thick rubber mat is placed below the NPRM to protect the roof. 4 cinderblocks are used as ballast to secure the NPRM.

!!! info "Non-penetrating roof mount (NPRM / Non-Pen)"
    Mounts used for larger radios and wifi devices so that we do not drill into any roofs, using rubber mats and cinderblocks.

<figure style="display: flex; justify-content: center; align-items: center; flex-direction: column;">
    <img src="../../assets/images/installations/install/image7.jpg"
         alt=""
         style="width: 80%;">
    <figcaption>A  non-penetrating roof mount with a Litebeam attached</figcaption>
</figure>

### Mounting on existing roof structures

We also often use J-arm mounts or pre-existing mounts from prior telecommunications installations (old Satellite dishes) to mount our equipment.

<figure style="display: flex; justify-content: center; align-items: center; flex-direction: column;">
    <div style="display: flex; justify-content: center; align-items: center; flex-direction: column;">
        <img src="../../assets/images/installations/install/image9.jpg" width="80%">
    </div>
    <figcaption>A LiteBeam mounted on a previously-installed mast on a chimmney</figcaption>
</figure>

## WiFi Access Points Overview

### Outdoor Wifi APs

Hosts of rooftop installations will also host a router in the house near the window to the front of the house. In some cases we may install a wall-mounted access point on the outside of the house to propagate the broadband signal throughout the neighborhood.

### Indoor Router and Access Points Overview

The Ethernet cable is passed through a Power-over-Ethernet (PoE) injector, which adds power to the signal the Ethernet cable is carrying and allows downstream devices to be powered solely through Ethernet.

!!! info "Power over Ethernet (PoE)"
    Devices that pass electric power along with data on Ethernet cabling.

    [PoE injector product page](https://store.ui.com/us/en/pro/products/poe-24)

<figure style="display: flex; justify-content: center; align-items: center; flex-direction: column;">
    <img src="../../assets/images/installations/install/image4.jpg"
         alt="" style="">
</figure>

The powered Ethernet cable is wired to a Ubiquiti EdgeRouter-X (or possibly another router in the future) configured to support mesh networking. The router handles traffic for each of the access points (APs) it is meshed with.

!!! info "EdgeRouter-X (ERX)"
    Router that PCW uses as a switch; a switch moves data between devices.

    [EdgeRouter X product page](https://store.ui.com/us/en/pro/category/wired-edge-max-routing/products/er-x)

<figure style="display: flex; justify-content: center; align-items: center; flex-direction: column;">
    <img src="../../assets/images/installations/install/image5.jpg"
         alt=""
         style="width: 50%;">
    <figcaption>Ubiquiti EdgeRouterX</figcaption>
</figure>

Finally, a Ubiquiti Mesh AP ("bunny ears" because look at them!) is connected to the router and allows devices in its radio signal range to connect to the network. The bunny ears should be installed in a location that is radio-visible to the mesh APs at the home installs in range.

!!! info "Bunny ears"
    A type of access point antenna — PCW's nickname for the Ubiquiti UAP-AC-Mesh.

    [UAP-AC-Mesh product page](https://store.ui.com/us/en/collections/unifi-wifi-outdoor-long-range/products/uap-ac-mesh)

<figure style="display: flex; justify-content: center; align-items: center; flex-direction: column;">
    <img src="../../assets/images/device-configs/mesh/Materials.jpeg"
         alt=""
         style="width: 50%;">
    <figcaption>A Unifi UAP-AC-Mesh, or "bunny ears"</figcaption>
</figure>

For more information on configuring our access points, see our [Configure AP-Mesh Guide](../device-configuration/configure-ap-mesh.md)

## Considerations When Installing a Mesh Node

!!! info "Hub"
    For PCW purposes, a hub refers to an install where we use a radio to "draw in" wireless connectivity. When we do hub installations, they include PhillyWisper.

!!! info "Node"
    A node is a mesh install that does not require a radio/router; it acts as a relay zone that expands wifi connectivity from a hub.

Mesh nodes are installations where we do not use a Litebeam, but instead set up a wireless access point that meshes from a nearby access point wired to a router and Litebeam at a local hub. As documented by [Unifi](https://help.ui.com/hc/en-us/articles/115002262328-Considerations-for-Optimal-Wireless-Mesh-Networks), several factors must be considered when building a mesh network:

* **Mesh networks should be supplemental** - Although mesh networks can operate comporably to a hard-wired network, connection quality and speed can be greatly affected by radiofrequency (RF) noise and obstructions between APs such as walls, trees, or other structures.
* **Mesh 'hops' should be minimized** - A meshed AP should only have one 'parent' - each mesh 'hop', or mesh connection between APs, results in a significant performance decrease. Ideally, there should be a maximum of two 'hops' - e.g, a mesh AP meshes with another mesh AP, which then meshes to a hard-wired AP.
* **Limit conncurrent connections to a 'parent'** - Similarly, meshing too many APs to the same 'parent' creates additional RF noise and performance demands on the parent, resulting in decreased performance and stability.
* **Ensure strong signal strength between meshed APs** - Ideally, a meshed AP will have clear Line-of-Sight (LoS) to its mesh parent. A signal strength of -60dbm is recommended for ideal performance. Ensure minimal obstructions between the meshed AP and the parent, such as walls, trees, furniture, etc.
