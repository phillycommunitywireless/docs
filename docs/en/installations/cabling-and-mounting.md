# Cabling and Mounting

Follow the order of operations: don’t pin cables until it’s fully run and tested; don’t secure mounts until cables have been run.

## Run Ethernet cable end-to-end

- Run cable along the intended route, measuring out the length needed.
- If the cable run passes between inside and outside, determine where.
    - Look for pre-existing holes that we can use to avoid drilling where possible.
    - Look for previous cable runs to potentially drill next to, keeping the cabling around the building consistent.
    - If drilling is necessary, see [When drilling inside](handbook/risks-rooftop-ladder-drill.md#when-drilling-inside).
- While running cable, temporarily secure the cable to existing objects to help guide the cable where necessary.
- Snip cable once length has been determined, leaving additional slack on both ends.

## Crimp and Test Ethernet

- PCW crimps Ethernet cable according to the T568B crimping pattern, which is the most commonly used. See [NYC Mesh’s Book section on Ethernet](https://wiki.nycmesh.net/books/3-hardware-firmware/page/ethernet-cable) for more.
- When finished ordering the cable’s wires, push them through pass-thru RJ45s with the window side facing you. Ensure the RJ45 is pulled over the cable’s rubber sheath as much as possible.
- Test Ethernet using the Klein Tools tester and make sure the cable passes.
    - Note: The top row visible on the tester screen shows the Ethernet end that is plugged into the main tester end. The bottom row shows the Ethernet end plugged into the remote end (the piece that separates).

## Test devices

- Plug devices into crimped cable. Ensure that they are receiving the correct amount of power via PoE.
- Test to make sure the device is receiving data and Wi-Fi is working.
    - White and/or blue lights are usually a good sign.
    - Phones can be used to ensure that a device is broadcasting Wi-Fi.
    - Devices will come up in PCW’s UniFi controller and should say “Adopted.”

## Mount access points and pin cable

- Install the access point mount, if using a J-arm or a mounting plate.
    - We never drill into a roof for mounting. If using a non-penetrating roof mount, this mount should be built before or while running Ethernet cable.
- Add access points to their mounts.
    - We always aim to leave extra slack for the Ethernet cable. This slack should be coiled neatly and attached to the mount (or nearby) using zip ties or electrical tape.
    - In some cases, cables should be positioned to create a “drip loop” right before the Ethernet enters a device. [Learn more about drip loops here](https://support.huawei.com/enterprise/en/doc/EDOC1100278610/f5d86b9c/guide-to-making-drip-loops).
- Secure the Ethernet cable as best as possible to avoid damage (via wind, etc.) over time. Here are some best practices about cable clipping:
    - Clip cables as inconspicuously as possible. Indoors, that often means running cables next to baseboards, door frames, or where walls meet ceilings.
    - Use screw clips in outdoor scenarios. Clip every 1-2 feet.
        - For brick, concrete, and other harder materials, pre-drill using Tapcon drillbits and then add Tapcons (blue screws) to the black plastic clips, removing the existing screws.
    - For indoor installs, using “plastic staples” (ie. nails with plastic cable holders) is preferable, due to its ease and creation of smaller holes. Use black pins with black cable, and white pins with white cable.
