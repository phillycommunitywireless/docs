---
title: Solar Mesh Nodes
---
# Solar Mesh Node Overview

Philly Community Wireless is actively supporting sustainable green spaces focused on environmental conservation and resource efficiency. Using off-the-grid solar nodes designed by [Holobiont Lab](https://holobiontlab.org/), we have installed solar-powered WiFi access points at gardens and other spaces where electricity is costly and/or not readily available. Philly Community Wireless is also in the process of powering smart sensors such as the [PurpleAir air monitor](https://www.purpleair.com/products/classic-plus-air-quality-monitor) with modified solar nodes to track environmental health.

## Hardware Specs

* Weather-proof outdoor enclosure
* 25-50W solar panel
* Any assortment of appropriate repurposed batteries at nominal 12V
* A charge controller
* A low-temp disconnect (depending on the battery)
* A 12V to 24V 3A boost converter
* A mesh node: starting with the 24V Ubiquity mesh access point

## Deployments

PCW installed a solar mesh node in Norris Square Neighborhood Projects Colobo Gardens in 2021, and it only recently needed to be fixed with a replacement battery. The access point sits at the top of a bamboo mast, high enough to clear the garden's structures, with the solar panel and enclosure mounted below it.

<figure style="display: flex; align-items: center; flex-direction: column;">
    <img src="/assets/images/installations/solar/ap_install.jpg"
         alt="Mounting the access point on the bamboo mast at Colobo Gardens"
         style="width: 50%; height: 50%;">
    <figcaption>Mounting the access point on the bamboo mast at Colobo Gardens</figcaption>
</figure>

## The Solar Battery Enclosure

The weather-proof enclosure holds everything that is not the panel or the access point: the battery, the charge controller, and the PoE injector that carries power up to the AP over a single Ethernet run.

<figure style="display: flex; align-items: center; flex-direction: column;">
    <img src="/assets/images/installations/solar/solar_with_info.jpg"
         alt="The open enclosure, with the battery, charge controller and PoE injector labelled"
         style="width: 50%; height: 50%;">
    <figcaption>Inside the enclosure at Colobo Gardens</figcaption>
</figure>

## Troubleshooting Solar Mesh Nodes

For additional troubleshooting help, check out the 'Troubleshooting' section (pg. 12) of  the [Meshbox Documentation](https://holobiontlab.org/docs/meshBoxDocumentation.pdf). Holobiont Lab's [meshbox docs](https://holobiontlab.org/r&d/meshbox) cover the design these nodes are based on in more detail.

Common issues include:

* Battery Discharge - the LiFePo4 battery should read between 12.5V to 14.6V.
  * Anything less than 12.5v and the battery management system will shut off to save power.
* Connections between the enclosure and the charge controller, as well as the connections between the charge controller and AP.
  * There should be a **red** light on the charge controller, and a **green** light on the PoE injector.
* Low temperature or bad weather conditions

## Further resources

See [Green Technology Resources](green-technology.md) for solar programs, urban agriculture organizations, and environmental monitoring initiatives in Philadelphia.
