---
title: Access Point Placement
---

# Access Point Placement

Where an access point goes matters as much as which access point it is. This page covers how PCW
decides where to put APs — the difference between a hub and a node, and what to consider when a
node meshes wirelessly rather than being wired in.

## Hubs and nodes

Mesh nodes are installations where we do not use a Litebeam, but instead set up a wireless access
point that meshes from a nearby access point wired to a router and Litebeam at a local hub.

Whether a site can be a hub is decided during the [building assessment](buildingassessment.md) —
a hub needs line-of-sight to a PhillyWisper high site. A node does not, but it does need a good
wireless link back to a hub, which is what the rest of this page is about.

See also NYC Mesh's [typical installs](https://wiki.nycmesh.net/books/2-install-maintenance-guides/page/typical-installs) page for how a similar network describes its install types.

<!-- Ideas to note, 2026-09-27, from the retired Drive doc "Installation Overview - Public Docs" (its "Extra Notes on PCW install types"). Unverified; staff to confirm or rewrite before any of it goes visible.
1. Mesh node uses (doc's words): "Used for 1) relaying a signal to another mesh AP, and/or 2) providing a WiFi access point to a public, outdoor space. May provide a signal inside the building it is installed on, depending on placement and building construction."
2. A third type, mesh node + indoor AP (doc's words): "Same as a Mesh node, plus an additional access point installed inside the building to provide a home with stronger and more consistent signal indoors. The indoor AP may be another bunny ears, or any other home router." "PCW mounts a single Unifi Mesh AP with LOS to another Mesh AP, and runs an Ethernet cable into the home for a home router to be connected." Check: still offered? "any other home router" right?
3. Hubs (doc's words): "An indoor AP may also be installed if stronger and more consistent signal is required inside the house." "sometimes we use a 60ghz alternative" to the LiteBeam. Check: is 60 GHz still used?
5. PTMP installs are not described anywhere yet (Leanne, July 2026: "i'd add the newer PTMP to this too"). Needs a sentence or two from staff.
-->

## Considerations when installing a mesh node

Ubiquiti's [Considerations for Optimal Wireless Mesh Networks](https://help.ui.com/hc/en-us/articles/115002262328-Considerations-for-Optimal-Wireless-Mesh-Networks)
is the reference we work from. The points that come up most often on PCW installs:

* **Mesh networks should be supplemental** - Although mesh networks can operate comparably to a hard-wired network, connection quality and speed can be greatly affected by radiofrequency (RF) noise and obstructions between APs such as walls, trees, or other structures.
* **Mesh 'hops' should be minimized** - A meshed AP should only have one 'parent' - each mesh 'hop', or mesh connection between APs, results in a significant performance decrease. Ideally, there should be a maximum of two 'hops' - e.g, a mesh AP meshes with another mesh AP, which then meshes to a hard-wired AP.
* **Limit concurrent connections to a 'parent'** - Similarly, meshing too many APs to the same 'parent' creates additional RF noise and performance demands on the parent, resulting in decreased performance and stability.
* **Ensure strong signal strength between meshed APs** - Ideally, a meshed AP will have clear line-of-sight (LoS) to its mesh parent. A signal strength of -60 dBm is recommended for ideal performance. Ensure minimal obstructions between the meshed AP and the parent, such as walls, trees, furniture, etc.

## Outdoor placement

Outdoor APs should be mounted where they are radio-visible to the mesh APs at the home installs in
range, and high enough to clear whatever is around them. On [solar nodes](solar.md), that usually
means the AP sits at the top of the mast with the panel and enclosure mounted below it.

For how to configure an AP once it is placed, see the
[Configure Unifi APs](../device-configuration/configure-ap-mesh.md) guide.
