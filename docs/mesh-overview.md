---
title: What is a Mesh Network?
---

## What is a Mesh Network?
Philly Community Wireless's goal, with assistance from [**PhillyWisper**](https://phillywisper.net/), is to address Philadelphia's digital divide with community-owned and -operated mesh network technologies.

In a typical home network, all 'access points' (APs) are hard-wired to your router via Ethernet cable. In a mesh network, access points can not only be hard-wired, but connect to each other wirelessly, allowing a single Internet connection to be shared with significantly less infrastructure and labor than hard-wiring every single AP. 

<figure style="display: flex; align-items: center; flex-direction: column;">
    <img src="/assets/images/device-configs/mesh/hace_wall_mesh.jpg"
         alt="Colobo AP"
         style="width: 75%;">
    <figcaption>This AP conveniently plugs directly into an outlet, and then meshes with nearby APs - meaning we don't have to run another cable!</figcaption>
</figure>


## Performance Considerations for Mesh Networks

Several factors must be considered while operating a mesh network:

* **Mesh networks should be supplemental** - Although mesh networks can operate comporably to a hard-wired network, connection quality and speed can be greatly affected by radiofrequency (RF) noise and obstructions between APs such as walls, trees, or other structures. 

* **Mesh 'hops' should be minimized** - A meshed AP should only have one 'parent' - each mesh 'hop', or mesh connection between APs, results in a significant performance decrease. Ideally, there should be a maximum of two 'hops' - e.g, a mesh AP meshes with another mesh AP, which then meshes to a hard-wired AP. 

* **Limit conncurrent connections to a 'parent'** - Similarly, meshing too many APs to the same 'parent' creates additional RF noise and performance demands on the parent, resulting in decreased performance and stability. 

* **Ensure strong signal strength between meshed APs** - Ideally, a meshed AP will have clear Line-of-Sight (LoS) to its mesh parent. A signal strength of -60dbm is recommended for ideal performance. Ensure minimal obstructions between the meshed AP and the parent, such as walls, trees, furniture, etc. 

## Additional Resources
Please visit [this page](https://help.ui.com/hc/en-us/articles/115002262328-Considerations-for-Optimal-Wireless-Mesh-Networks) for more information on mesh networks.
