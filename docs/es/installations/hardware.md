---
title: Hardware
---

<!-- TODO: machine-drafted Spanish translation — needs review by a fluent speaker. -->
!!! note "Traducción preliminar"
    Esta página es una traducción preliminar y está pendiente de revisión. Si encuentra un error, la [versión en inglés](../../../installations/hardware/) es la referencia.

# Hardware

Los siguientes materiales se usan en las [instalaciones](installations.md). Puede encontrar más información sobre cómo configurar muchos de estos dispositivos en las guías de instalación de esta documentación.

Consulte los documentos de NYCMesh [Networking Hardware](https://wiki.nycmesh.net/books/3-hardware-firmware) (equipos de red) e [Installation Equipment](https://wiki.nycmesh.net/books/2-install-maintenance-guides/page/install-tools-and-equipment) (equipos de instalación), en inglés, para ver más detalles e información sobre el hardware y las herramientas que aparecen a continuación.

## Equipos de red

### Puntos de acceso

#### Instalaciones en interiores y exteriores

<div class="device-grid" style="--cols: 2">
  <figure>
    <img class="device-art" src="../../../assets/images/equipment/unifi-ap-ac-mesh.svg"
         alt="Dibujo lineal de un punto de acceso Ubiquiti UAP-AC-M, un cuerpo delgado con dos antenas verticales.">
    <figcaption><a href="https://store.ui.com/products/unifi-ac-mesh-ap">UAP-AC-M</a><br>'Bunny Ears' (orejas de conejo)</figcaption>
  </figure>
  <figure>
    <img class="device-art" src="../../../assets/images/equipment/uma-d.svg"
         alt="Dibujo lineal de una antena direccional Ubiquiti UMA-D, un panel rectangular plano sobre un soporte.">
    <figcaption><a href="https://store.ui.com/collections/operator-airmax-and-ltu-antennas/products/directional-dual-band-antenna-for-uap-ac-m">UMA-D</a><br>Antena direccional, 'Panel Antenna' (antena de panel)</figcaption>
  </figure>
</div>

La UMA-D se acopla a un UAP-AC-M en lugar de sus antenas, para dirigir la cobertura hacia una sola dirección
en vez de repartirla de manera uniforme.

- [Ubiquiti UAP-Flex-HD](https://store.ui.com/us/en/products/uap-flexhd)
- [Ubiquiti U6 Mesh](https://store.ui.com/us/en/products/u6-mesh)
- [Ubiquiti U6 Mesh Pro](https://store.ui.com/us/en/products/u6-mesh-pro)
- [Ubiquiti U6 LR](https://store.ui.com/us/en/products/u6-lr)
- [Ubiquiti UAP-AC-M-Pro](https://store.ui.com/us/en/products/uap-ac-mesh-pro)
- [Ubiquiti U7 Outdoor](https://store.ui.com/us/en/products/u7-outdoor)
- [Ubiquiti Swiss Army Knife](https://store.ui.com/us/en/products/uk-ultra)

#### Instalaciones en interiores

Los puntos de acceso para interiores vienen en tres formas. Cuál le conviene depende principalmente de dónde
se puede montar en el sitio.

<div class="device-grid" style="--cols: 3">
  <figure>
    <img class="device-art" src="../../../assets/images/equipment/indoor-ap-round.svg"
         alt="Dibujo lineal de un punto de acceso redondo para montar en el techo, visto de frente como un disco liso con un anillo interior estrecho.">
    <figcaption><strong>Redondo, de techo o pared</strong><br><a href="https://store.ui.com/us/en/products/uap-nanohd">nanoHD</a>, <a href="https://store.ui.com/us/en/products/u6-lite">U6 Lite</a>, <a href="https://store.ui.com/us/en/products/u6-plus">U6+</a>, <a href="https://store.ui.com/us/en/category/wifi-flagship/products/u6-pro">U6 Pro</a>, <a href="https://store.ui.com/us/en/products/u7-lite">U7 Lite</a>, <a href="https://store.ui.com/us/en/products/u7-pro">U7 Pro</a></figcaption>
  </figure>
  <figure>
    <img class="device-art" src="../../../assets/images/equipment/u6-in-wall.svg"
         alt="Dibujo lineal de un punto de acceso empotrado en la pared, una pequeña placa rectangular con un puerto Ethernet en su borde inferior.">
    <figcaption><strong>Placa empotrada en la pared</strong><br><a href="https://store.ui.com/us/en/products/uap-ac-iw">UAP-AC-IW</a>, <a href="https://store.ui.com/us/en/products/u7-iw">U7 In-Wall</a></figcaption>
  </figure>
  <figure>
    <img class="device-art" src="../../../assets/images/equipment/beacon-hd.svg"
         alt="Dibujo lineal de un UAP-BeaconHD, una unidad redondeada que se enchufa directamente en un tomacorriente de pared.">
    <figcaption><strong>Se enchufa al tomacorriente</strong><br><a href="https://store.ui.com/us/en/products/uap-beaconhd">UAP-BeaconHD</a></figcaption>
  </figure>
</div>

También se usan en interiores: [Ubiquiti U6 Extender](https://store.ui.com/us/en/products/u6-extender), [Ubiquiti U7 Pro Max](https://store.ui.com/us/en/products/u7-pro-max), [Ubiquiti U7 Long Range](https://store.ui.com/us/en/products/u7-lr).

### Conmutadores (switches)
- [Ubiquiti USW Flex Mini](https://store.ui.com/us/en/products/usw-flex-mini)
- [Ubiquiti USW Flex](https://store.ui.com/us/en/category/switching-utility/products/usw-flex)
- [Ubiquiti NanoSwitch](https://store.ui.com/us/en/products/n-sw) - un switch de exterior de cuatro puertos; tres de sus puertos suministran PoE pasivo de 24 V. Se usa de vez en cuando.

<figure class="device-diagram">
    <img class="device-art" src="../../../assets/images/equipment/flex-mini-ports.svg"
         alt="Dibujo lineal de la cara de puertos del USW Flex Mini, que muestra sus cinco puertos Ethernet en fila, con el puerto de entrada PoE en un extremo.">
    <figcaption>Puertos del USW Flex Mini. El puerto 1 recibe la entrada PoE (alimentación a través de Ethernet) y alimenta el switch, así que es el que va de regreso hacia el router.</figcaption>
</figure>

<div class="device-grid" style="--cols: 2">
  <figure>
    <img class="device-art" src="../../../assets/images/equipment/nanoswitch.svg"
         alt="Dibujo lineal de un Ubiquiti NanoSwitch, una carcasa plana y rectangular de esquinas redondeadas, con un punto de montaje redondo y una pequeña luz de estado.">
    <figcaption><a href="https://store.ui.com/us/en/products/n-sw">NanoSwitch</a><br>Carcasa para exteriores</figcaption>
  </figure>
  <figure>
    <img class="device-art" src="../../../assets/images/equipment/nanoswitch-ports.svg"
         alt="Dibujo lineal de la cara de puertos del NanoSwitch, que muestra cuatro puertos Ethernet en fila, cada uno con una luz de estado verde y una roja.">
    <figcaption>Puertos del NanoSwitch</figcaption>
  </figure>
</div>

### Routers
- [Ubiquiti EdgeRouter X](https://store.ui.com/collections/operator-edgemax-routers/products/edgerouter-x)
- [Ubiquiti EdgePoint R6](https://store.ui.com/collections/operator-edgemax-control-points/products/edgepoint-r6) - consulte el [documento de NYC Mesh](https://wiki.nycmesh.net/books/3-hardware-firmware/page/ubiquiti-edgepoint-r6) (en inglés) sobre esta alternativa al ER-X.

<figure class="device-diagram">
    <img class="device-art" src="../../../assets/images/equipment/edgerouter-x.svg"
         alt="Dibujo lineal del panel frontal del EdgeRouter X, con los cinco puertos Ethernet rotulados de izquierda a derecha: eth0/PoE IN, eth 1, eth 2, eth 3 y eth4/PoE OUT.">
    <figcaption>Puertos del ERX. Consulte <a href="../../device-configuration/configure-edgerouter-x/">Configurar EdgeRouter X</a> para saber qué se conecta en cada uno.</figcaption>
</figure>

### Radios PtP y PtMP

<div class="device-grid" style="--cols: 2">
  <figure>
    <img class="device-art" src="../../../assets/images/equipment/litebeam-ac.svg"
         alt="Dibujo lineal de una airMAX LiteBeam AC Gen2, una antena parabólica sobre un soporte de rótula.">
    <figcaption><a href="https://store.ui.com/collections/wireless/products/litebeam-5ac-gen2">LiteBeam AC Gen2</a></figcaption>
  </figure>
  <figure>
    <img class="device-art" src="../../../assets/images/equipment/powerbeam.svg"
         alt="Dibujo lineal de una airMAX PowerBeam 5AC, una antena parabólica sólida y más profunda sobre un soporte.">
    <figcaption><a href="https://techspecs.ui.com/uisp/wireless/pbe-5ac-500">PowerBeam 5ac 500</a></figcaption>
  </figure>
</div>

- [airMAX LiteBeam AC 5 GHz Bridge](https://store.ui.com/collections/wireless/products/litebeam-5ac-gen2)
- [airMAX PowerBeam 5ac 500](https://techspecs.ui.com/uisp/wireless/pbe-5ac-500)
- [airMAX NanoBeam M5](https://store.ui.com/us/en/products/nbe-m5-16)
- [airMAX NanoStation M5 loco](https://store.ui.com/us/en/category/wireless-airmax-5ghz/products/locom5)

<!-- Ideas to note, 2026-09-27, from the retired Drive doc "Installation Overview - Public Docs". Unverified; staff to confirm before use.
4. Equipment per install type, as that doc listed it: hub = 1 EdgeRouter X, 1 UAP-AC-Mesh, 1 J-arm and mounting hardware (it also listed a clamshell for an outdoor ER-X, dropped: the ERX stays indoors); mesh node = 1 UAP-AC-Mesh, 1 J-arm and mounting hardware; mesh node + indoor AP = "Same as Mesh node, plus:" (the list was never finished). Check: which APs now (U6 Mesh, U6 LR, U7 Outdoor, AC-M-Pro are listed above); add an outdoor switch when a hub has more than one AP? The hub list is missing the LiteBeam, the PoE injector and the cable.
6. Cable: that doc said the LiteBeam "is powered via passive PoE through a single Cat 5 cable". Check what is run now (Cat 5e / Cat 6, outdoor-rated).
-->

### Soportes

- [Soporte universal de brazo en J (Universal J-Arm Mount)](https://store.ui.com/collections/operator-airmax-and-ltu-accessories/products/universal-antenna-mount)
- [Soporte para ventana (Window Mount)](https://store.ui.com/collections/operator-airmax-and-ltu-accessories/products/nanostation-window-mount)
- [Soporte de techo no penetrante](https://www.data-alliance.net/roof-mounts/)
- Caja(s) protectora(s)

### Accesorios

<figure class="device-diagram">
    <img class="device-art" src="../../../assets/images/equipment/poe-injector.svg"
         alt="Dibujo lineal de un inyector PoE (alimentación a través de Ethernet) con dos cables Ethernet que van de él a un punto de acceso.">
    <figcaption>Un inyector PoE alimenta un AP a través de su cable Ethernet, así que el AP no necesita un tomacorriente propio.</figcaption>
</figure>

Identifique qué voltaje y potencia de PoE (alimentación a través de Ethernet) necesitará el equipo. Notas sobre el voltaje:

- Los ERX (y, por extensión, las LiteBeam) son de 24 V
- Casi todos los puntos de acceso son de 48 V
    - El UAP-AC-Mesh (conocido coloquialmente como "Bunny Ears", orejas de conejo) acepta 48 V o 24 V

- Cable(s) Ethernet de largo corto a mediano
- Regleta(s) eléctrica(s) apta(s) para exteriores
- Extensión(es) eléctrica(s) apta(s) para exteriores
- Divisor(es) de corriente apto(s) para exteriores
- [Extensiones eléctricas](https://www.newegg.com/black-monoprice-6-00-ft-others/p/0N6-01B8-002D6)
- [Inyector/divisor PoE](https://www.newegg.com/p/2WG-00DK-00004)
- [Adaptador/acoplador de Ethernet a Ethernet](https://www.newegg.com/p/0Y3-02J6-00001)
- Conectores Ethernet (RJ45) de paso (*pass-through*)
- [Adaptador de USB tipo C a Ethernet](https://www.ebay.com/itm/132225990432)

## Herramientas

### Redes

- [Crimpadora (ponchadora) para cable Ethernet](https://www.homedepot.com/p/Klein-Tools-Compact-Ratcheting-Modular-Crimper-VDV226-107/204732347)
- Pelacables para cable CAT5e
- [Probador de cable Ethernet](https://www.lowes.com/pd/Klein-Tools-Cable-Tester-Kit-with-Scout-Pro-3-Tester-Remotes-Adapter-Battery/5014306081)
- Hotspot móvil
- Analizador de espectro Unifi WifiMan

### Herramientas manuales y eléctricas

- Taladro(s): taladro atornillador, taladro percutor
- Atornillador de impacto
- Juego de brocas
- Broca de cobalto / titanio (1/4")
- Broca para mampostería con punta de carburo (5/32")
- Puntas de dado hexagonal para taladro (3/8" para abrazaderas de manguera y 1/4" para tornillos de mampostería)
- Brocas para mortero y para madera
- Martillo
- Tijeras
- Tijeras para lámina (*snips*)
- Alicates de punta
- Destornilladores: Phillips (de cruz), plano, Torx
- Llaves de dado
- Cinta métrica
- Medidor láser
- Guía pasacables (*fish tape*) / varilla de empuje
- Limas: triangular, plana, redonda
- Llave ajustable (perico) de 6"
- Bolsa adicional para cargar o subir el equipo
- Soga
- Cuchilla multiuso
- Llaves Allen
- Pelador de cables eléctricos

### Materiales consumibles
- Clavos para concreto
- Tornillos para concreto (cabeza hexagonal de 3/16", CSH316134)
- Tornillos
- Clavos
- Grapas de sujeción para cables
- Abrazaderas de manguera
- Amarracables (*zip ties*)
- Cinta aislante
- Tiras de velcro
- Amarres de velcro para cables
- Calcomanías (*stickers*) de PCW
- Sellador impermeable de goma
- Pegamento instantáneo (*superglue*)

### Equipo de protección personal
- Gafas de seguridad
- Guantes de trabajo
- Mascarillas KN95
- Botiquín de primeros auxilios
