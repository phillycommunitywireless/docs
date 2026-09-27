<!-- TODO: machine-drafted Spanish translation — needs review by a fluent speaker. -->
!!! note "Traducción preliminar"
    Esta página es una traducción preliminar y está pendiente de revisión. Si encuentra un error, la [versión en inglés](../../../installations/cabling-and-mounting/) es la referencia.

# Cableado y montaje

Siga el orden de las operaciones: no fije los cables hasta que el tendido esté completo y probado; no asegure los soportes hasta que los cables se hayan tendido.

## Tienda el cable Ethernet de extremo a extremo

- Tienda el cable a lo largo de la ruta prevista, midiendo la longitud necesaria.
- Si el tendido del cable pasa entre el interior y el exterior, determine por dónde.
    - Busque agujeros preexistentes que podamos usar para evitar taladrar cuando sea posible.
    - Busque tendidos de cable anteriores junto a los que se pueda taladrar, manteniendo uniforme el cableado alrededor del edificio.
    - Si es necesario taladrar, consulte [Al taladrar en interiores](handbook/risks-rooftop-ladder-drill.md#al-taladrar-en-interiores).
- Mientras tiende el cable, sujételo temporalmente a objetos existentes para ayudar a guiarlo donde sea necesario.
- Corte el cable una vez determinada la longitud, dejando holgura adicional en ambos extremos.

## Crimpe y pruebe el Ethernet

- PCW crimpa el cable Ethernet según el patrón de crimpado T568B, que es el más utilizado. Consulte la [sección sobre Ethernet del Book de NYC Mesh](https://wiki.nycmesh.net/books/3-hardware-firmware/page/ethernet-cable) para más información.
- Cuando termine de ordenar los hilos del cable, páselos por conectores RJ45 pasantes con el lado de la ventana hacia usted. Asegúrese de que el RJ45 quede lo más metido posible sobre la funda de goma del cable.
- Pruebe el Ethernet con el probador Klein Tools y asegúrese de que el cable pase la prueba.
    - Nota: la fila superior visible en la pantalla del probador muestra el extremo del Ethernet conectado al extremo principal del probador. La fila inferior muestra el extremo del Ethernet conectado al extremo remoto (la pieza que se separa).

## Pruebe los dispositivos

- Conecte los dispositivos al cable crimpado. Asegúrese de que estén recibiendo la cantidad correcta de energía por PoE.
- Pruebe para asegurarse de que el dispositivo esté recibiendo datos y de que el Wi-Fi funcione.
    - Las luces blancas y/o azules suelen ser buena señal.
    - Se pueden usar teléfonos para comprobar que un dispositivo esté emitiendo Wi-Fi.
    - Los dispositivos aparecerán en el controlador UniFi de PCW y deberían indicar “Adopted”.

## Monte los puntos de acceso y fije el cable

- Instale el soporte del punto de acceso, si usa un J-arm o una placa de montaje.
    - Nunca taladramos un techo para montar equipos. Si usa un soporte de techo no penetrante, este soporte debe armarse antes o mientras se tiende el cable Ethernet.
- Coloque los puntos de acceso en sus soportes.
    - Siempre procuramos dejar holgura adicional en el cable Ethernet. Esta holgura debe enrollarse con cuidado y sujetarse al soporte (o cerca de él) con bridas o cinta aislante.
    - En algunos casos, los cables deben colocarse de modo que formen un “bucle de goteo” justo antes de que el Ethernet entre en un dispositivo. [Obtenga más información sobre los bucles de goteo aquí](https://support.huawei.com/enterprise/en/doc/EDOC1100278610/f5d86b9c/guide-to-making-drip-loops).
- Asegure el cable Ethernet lo mejor posible para evitar daños (por el viento, etc.) con el tiempo. Estas son algunas buenas prácticas para fijar cables con grapas:
    - Fije los cables de la forma más discreta posible. En interiores, eso a menudo significa tender los cables junto a los zócalos, los marcos de las puertas o donde las paredes se unen con el techo.
    - Use grapas con tornillo en exteriores. Coloque una grapa cada 1-2 pies.
        - Para ladrillo, concreto y otros materiales más duros, pretaladre con brocas Tapcon y luego coloque Tapcons (tornillos azules) en las grapas de plástico negras, retirando los tornillos originales.
    - Para instalaciones en interiores, es preferible usar “grapas de plástico” (es decir, clavos con sujetacables de plástico), por su facilidad y porque hacen agujeros más pequeños. Use grapas negras con cable negro y grapas blancas con cable blanco.
