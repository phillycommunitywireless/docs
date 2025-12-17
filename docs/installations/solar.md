---
title: Solar Mesh Nodes
---

# Solar Mesh Node Overview

Designed by [Holobiont Lab](https://holobiontlab.org/), we install solar-powered wifi access points at gardens and other spaces where electricity is not available. For more information, see Holobiont' [meshbox docs](https://holobiontlab.org/r&d/meshbox).

# Hardware Specs

* An enclosure
* 25 -50W solar panel
* Any assortment of appropriate repurposed batteries nominal 24v
* A charge controller
* A low-temp disconnect (depending on the battery)
* A mesh node : starting with the Ubiquity mesh access point

# Deployments

PCW installed a solar mesh node in Norris Square Neighborhood Projects Colobo Gardens in 2021, and it only recently needed to be fixed with a replacement battery. Here are a few photos of what the setup looks like.

<figure style="display: flex; align-items: center; flex-direction: column;">
    <img src="../../assets/images/installations/solar/colobo_ap.jpg"
         alt="Colobo AP"
         style="width: 50%; height: 50%;">
    <figcaption>A photo of the AP at Colobo.</figcaption>
</figure>


<figure style="display: flex; align-items: center; flex-direction: column;">
    <img src="../../assets/images/installations/solar/ap_install.jpg"
         alt="Installing the AP at Colobo"
         style="width: 50%; height: 50%;">
    <figcaption>Installing the AP!</figcaption>
</figure>


<figure style="display: flex; align-items: center; flex-direction: column;">
    <img src="../../assets/images/installations/solar/solar_with_info.jpg"
         alt="Installing the AP at Colobo"
         style="width: 50%; height: 50%;">
    <figcaption>The meshbox's contents</figcaption>
</figure>

# Troubleshooting Solar Mesh Nodes
For additional troubleshooting help, check out the 'Troubleshooting' section (pg. 12) of  the [Meshbox Documentation](https://holobiontlab.org/docs/meshBoxDocumentation.pdf).

Common issues include: 

* Battery Discharge - the battery should read between 12.5V > 14.6V. 
    * Anything less than 12.5v and the battery management system will shut off to save power. 
* Connections between the enclosure and the charge controller, as well as the connections between the charge controller and AP.
    * There should be a **red** light on the charge controller, and a **green** light on the PoE injector. 
* Low temperature or bad weather conditions
