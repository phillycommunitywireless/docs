# Building & Electrical Safety

## Notes on Pre-Installed Internet Infrastructure

PCW often works in environments that have pre-existing Internet infrastructure. When doing our installations, we may be in proximity to existing cabling/networking infrastructure/etc that could be impacted or damaged by the work of our install.

<!-- Residential notes: still a placeholder in the Drive guide as of 2026-09-24; add when written. -->

### Commercial

In commercial buildings that already have Internet installed, you might see something like this:

![A fiber-optic splice enclosure mounted on a wall above a grey line amplifier, with coaxial cables running out of it.](../../../assets/images/installations/handbook/fiber-enclosure-and-line-amplifier.jpg)

Pictured above is a fiber-optic enclosure, used with a hybrid fiber-coax system. The black box on the top contains fiber from the fiber provider, and the line amplifier converts fiber-optic signals (beams of light) to electrical radio frequency signals to be carried over coaxial cable downstream. It will probably be connected to something like this:

![An open metal utility box holding a coaxial tap and splitters, with labelled coaxial cables leading out to subscribers.](../../../assets/images/installations/handbook/coax-tap-and-splitter-box.jpg)

Pictured above is a coaxial tap and splitter(s) – this is like a switch, but for coax. It gets its uplink internet connection through the large coaxial cables on the bottom, and then the devices that each labelled coaxial cable is plugged into goes to each individual subscriber.

## Roofs and Roofing

As a guiding principle, we never drill into parts of roofs that we can stand on.

The most important aspect of our roof work is to not allow moisture ingress, which can accumulate and damage a building from the inside-out without being visible until a leak or other damage appears. Learning about roof anatomy can help us understand the best way to mount our equipment without implicating the integrity of the roof. Learn more about the parts of a roof edge (flashing, drip edge, fascia, soffit) in [this guide](https://roofs.wiki/Roof_Anatomy_and_Parts_Explained).

## Fire Safety/Suppression Systems

Working in telecommunications or mechanical closets, we often are in close proximity to fire alarms and suppression systems. Generally, if a cable/conduit is colored red, it’s likely to be related to a fire suppression system or fire alarm, although this is not a hard and fast rule.

### Fireblocking Foam (AKA “Fireblock” or “Firestop”)

Fireblocking foam is often installed on/in conduit to assist with preventing fire spreading between floors of a building. The foam expands and hardens when exposed to high heat, creating a seal. In order to be compliant, the foam/firestop must be a complete seal around the penetration.

Generally, installed on conduits like so: firestop on the top, then insulation or mineral wool to also act as a backing/filler, while the firestop prevents the actual spread of smoke and fire.

![Orange firestop foam sealing the top of a metal conduit, with yellow insulation visible inside.](../../../assets/images/installations/handbook/firestop-on-conduit.jpg)

In this image, the firestop is the orange foam on the top of the conduit; see the yellow insulation visible below inside the actual conduit.

### Fire Doors

We never drill through or immediately next to fire doors as this violates their fireblocking integrity.

## Electrical

Although PCW primarily works with low-voltage (50V or less) cable and devices, we are often in environments where we are in close proximity to higher voltages/amperages.

### Common Electrical Cable Types

Romex - indoor power is often carried via this flat, non-metallic (NM) cable. Romex is color-coded based on the gauge and the amperage. Learn more about the color code in [this NEMA bulletin](https://www.nema.org/docs/default-source/technical-document-library/type-nm-b-cable-jacket-color-coding-for-conductor-size-idenification.pdf).

<!-- image held: third-party NM cable colour chart (The Spruce) and outlet-types photo; images to be sorted out later -->

### Conduit and You

Outdoors, electrical cable is usually encased in a conduit of some sort. We often see flexible conduit made of PVC, or straight conduit made of steel.

<!-- image held: third-party conduit-types photo grid; images to be sorted out later -->

### Avoiding Radio Frequency Interference Between Electrical Wires

Avoid running telecom and electrical cables through the same penetrations (have at least 2 inches of separation). If telecom and electrical cables must cross, cross them perpendicular to each other to minimize interference (only contact point is where they cross vs running in parallel). Ethernet is in twisted pairs to help deal with interference as well. Using shielded cable (FTP) helps reduce interference even more.

See also: [Applicable codes | Department of Licenses and Inspections | City of Philadelphia](https://www.phila.gov/departments/department-of-licenses-and-inspections/resources/applicable-codes/)
