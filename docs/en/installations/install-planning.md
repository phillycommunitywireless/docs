# Install Planning

## Building Assessment

PCW regularly installs WiFi at a wide range of building types, such as rowhomes, multi-dwelling units (MDUs), community centers, and public spaces such as parks and gardens. 

Assessments generally take 15-30 minutes. Be sure to take lots of pictures for reference or planning.

To assess a building for installation, we have to ask the following questions:

* **Does the building have line-of-sight (LoS) to a PhillyWisper high site or close proximity to a current PCW mesh node?**
    * Without direct LoS to a high site or existing node, the uplink radio's performance will be significantly degraded (if it can connect at all).
    * Google Earth can be a useful tool for determining potential LoS, but in many cases a site visit may be necessary.
    * Foliage from trees can cause significant interference - sites that are viable in the winter may be blocked by foliage in the summer.
    * New construction also pops up suddenly. It is important to verify the conditions of the location in person, as Google maps etc may not have the latest surroundings up to date.

* **Does the building have easy, safe, and simple roof/top floor access?**
    * Are ladders required? Are there stairs/a roof access hatch? 
    * LiteBeams are ideally installed on the roof, either via pre-existing roof structure, j-arm mount on the wall, or non-penetrating roof mount. 
    * Do we have permission to mount on the building or on structures on the roof?
    * PCW only installs on flat roofs, with rare exceptions. 
 
* **Is there access to power?**
    * If outdoors, is the power source protected? 
    * Will the power source need to be used by something else? Is it accessible to others who could unplug our equipment? 
    * Are there pre-existing penetrations we can reuse to run power-over-Ethernet from indoors?
    * PCW does not drill through roofs as they are too difficult to waterproof. 

* **Are there easy ways to mount access points?**
    * eg: existing poles we could simply ziptie APs to VS bringing a non-penetrating roof mount or j-arm.
    * How much cable will we have to run? 
    * What sort of access points will be necessary? Some are not weatherproof and can only be used indoors. 
    * Is there a chance mounting access points could damage the roof or walls?
    * Is there pre-existing Internet infrastructure (previous coaxial or fiber installations) we need to be mindful of? Cables running in parallel can interfere with each other, degrading performance for both connections 

* **If maintenance is required, will we be able to return in the future?**

Here are some considerations when thinking about outdoor vs. indoor power:

* PCW prefers to use indoor power where possible, especially in residential homes. Using outdoor power creates higher risk for water-related issues with our equipment.
* Using indoor power requires us to run cable into a building. In most cases where we use outdoor power, this is because the cable run indoors is significantly more complicated.
* If there is existing outdoor power that we hope to use, it’s important to determine if it’s available for our usage, or needed for other outdoor equipment.
* Any outdoor power under consideration must have an outdoor-rated outlet cover.

As an example, this is an ideal install site: 

<figure style="display: flex; align-items: center; flex-direction: column;">
    <img src="../../assets/images/installations/install/nkcdc_roof.png"
         alt="An ideal roof install location"
         style="width: 80%; ">
    <figcaption>An ideal roof install location in Kensington</figcaption>
</figure>

* The roof is clear of debris and is flat, with plenty of space for non-penetrating roof mounts. 
* The building is taller than almost every other building in the area, giving it free LoS to both PhillyWisper high sites and other potential PtP/PtMP sites.
* There is power on the roof, in this case covered GFCIs.

## Access Point Placement

Where an access point goes matters as much as which access point it is. This page covers how PCW
decides where to put APs — the difference between a hub and a node, and what to consider when a
node meshes wirelessly rather than being wired in.

### Hubs and nodes

Mesh nodes are installations where we do not use a Litebeam, but instead set up a wireless access
point that meshes from a nearby access point wired to a router and Litebeam at a local hub.

Whether a site can be a hub is decided during the [building assessment](#building-assessment) —
a hub needs line-of-sight to a PhillyWisper high site. A node does not, but it does need a good
wireless link back to a hub, which is what the rest of this page is about.

See also NYC Mesh's [typical installs](https://wiki.nycmesh.net/books/2-install-maintenance-guides/page/typical-installs) page for how a similar network describes its install types.

### Considerations when installing a mesh node

Ubiquiti's [Considerations for Optimal Wireless Mesh Networks](https://help.ui.com/hc/en-us/articles/115002262328-Considerations-for-Optimal-Wireless-Mesh-Networks)
is the reference we work from. The points that come up most often on PCW installs:

* **Mesh networks should be supplemental** - Although mesh networks can operate comparably to a hard-wired network, connection quality and speed can be greatly affected by radiofrequency (RF) noise and obstructions between APs such as walls, trees, or other structures.
* **Mesh 'hops' should be minimized** - A meshed AP should only have one 'parent' - each mesh 'hop', or mesh connection between APs, results in a significant performance decrease. Ideally, there should be a maximum of two 'hops' - e.g, a mesh AP meshes with another mesh AP, which then meshes to a hard-wired AP.
* **Limit concurrent connections to a 'parent'** - Similarly, meshing too many APs to the same 'parent' creates additional RF noise and performance demands on the parent, resulting in decreased performance and stability.
* **Ensure strong signal strength between meshed APs** - Ideally, a meshed AP will have clear line-of-sight (LoS) to its mesh parent. A signal strength of -60 dBm is recommended for ideal performance. Ensure minimal obstructions between the meshed AP and the parent, such as walls, trees, furniture, etc.

### Outdoor placement

Outdoor APs should be mounted where they are radio-visible to the mesh APs at the home installs in
range, and high enough to clear whatever is around them. On [solar nodes](green-tech/solar-mesh-node.md), that usually
means the AP sits at the top of the mast with the panel and enclosure mounted below it.

For how to configure an AP once it is placed, see the
[Configure Unifi APs](../device-configuration/configure-ap-mesh.md) guide.
