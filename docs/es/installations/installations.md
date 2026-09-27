---
title: Descripción general de la instalación
---

<!-- TODO: machine-drafted Spanish translation — needs review by a fluent speaker. -->
!!! note "Traducción preliminar"
    Esta página es una traducción preliminar y está pendiente de revisión. Si encuentra un error, la [versión en inglés](../../../installations/installations/) es la referencia.

# Descripción general de la instalación

Philly Community Wireless se ha asociado con [**PhillyWisper**](https://phillywisper.net/) para instalar antenas para nuestra red wifi gratuita en azoteas de los vecindarios de Norris Square, Fairhill y Kensington. PhillyWisper es un proveedor de servicios de Internet inalámbrico (WISP), lo que significa que nuestro proyecto lleva Internet a nuestros clientes en la "última milla" mediante tecnología de radio.

Philly Community Wireless busca construir tecnologías de redes de malla inalámbricas que sean propiedad de la comunidad y operadas por ella. Esta página describe nuestro proceso de instalación y el tipo de red que intentamos construir en una amplia zona de la ciudad. En una red doméstica típica, todos los ["puntos de acceso" (APs)](https://en.wikipedia.org/wiki/Wireless_access_point) están conectados por cable Ethernet a su router para crear una red de área local inalámbrica. En una red de malla, los puntos de acceso no solo pueden estar conectados por cable, sino que también pueden conectarse entre sí de forma inalámbrica. Esto permite compartir una sola conexión a Internet con mucha menos infraestructura y mano de obra que si se conectara cada AP por cable.

## Proceso de instalación en la azotea

La mayoría de las instalaciones se realizan en el siguiente orden:

1. **Evaluación del edificio**: recibimos una nueva dirección. Verificamos si la dirección tiene [línea de visión (LoS)](https://en.wikipedia.org/wiki/Line-of-sight_propagation) con un sitio alto de PhillyWisper usando Google Earth y otras herramientas de mapas, y hacemos evaluaciones del edificio tanto a distancia como en persona para elaborar un plan de instalación. Para obtener más información, consulte la página [Evaluación del edificio](buildingassessment.md).
2. **Planificación de la instalación**: si hay LoS, nos comunicamos con el residente o la organización comunitaria para conocer sus necesidades de conectividad, así como las de sus vecinos y de la zona en general. Esto nos ayuda a decidir qué tipo de puntos de acceso y equipos de red llevar, y cuánto cable vamos a necesitar. Una vez definida la logística de la instalación inicial, ¡se fija la fecha de instalación!
3. **Establecer el enlace ascendente**: el día de la instalación, PCW comienza instalando la radio de enlace ascendente (uplink), por lo general una [LiteBeam](https://store.ui.com/us/en/products/litebeam-5ac), apuntada hacia un sitio alto de PhillyWisper. Esta radio proporciona la conexión a Internet.
4. **Instalar los puntos de acceso**: una vez establecido el enlace ascendente, podemos empezar a tender cable por el techo o por dentro del edificio e instalar puntos de acceso wifi según se necesiten, ya sea en interiores o en exteriores.

En las instalaciones residenciales, o bien transmitimos una red privada para el residente desde los mismos puntos de acceso que transmiten la red pública de PCW, o bien le proporcionamos un router adicional para que tenga su propia red privada, que obtiene su enlace ascendente de la red de PCW.

A continuación se muestra un diagrama del sistema resultante. Pegados a la silueta de la casa y dentro de ella aparecen los dispositivos de exterior y de interior que PCW instalará para usted. Las siguientes secciones describen con más detalle nuestros métodos de instalación.

<figure style="display: flex; justify-content: center; align-items: center; flex-direction: column;">
    <img src="../../../assets/images/installations/install/diagram.png"
         alt="Diagrama general de la instalación"
         style="width: 85%;">
    <figcaption>Diagrama general de la instalación</figcaption>
</figure>

## Duración de las instalaciones de antenas

Por lo general, las instalaciones tardan entre dos y cuatro horas, pero en algunos casos pueden tardar más. El proceso de instalación completo, desde la antena en la azotea hasta un kit de malla montado en la pared, puede requerir 2 o 3 visitas, cada una de una o dos horas de trabajo.

## Hardware para la instalación

<figure style="display: flex; justify-content: center; align-items: center; flex-direction: column;">
    <div style="display: flex; justify-content: center; align-items: center; flex-direction: column;">
        <img src="../../../assets/images/installations/install/image8.jpg" alt="LiteBeam montada en una chimenea con un soporte tipo J (J-arm)" width="80%">
    </div>
    <figcaption>LiteBeam (aprox. 14 x 11 x 11 pulgadas) montada en una chimenea con un soporte tipo J (J-arm)</figcaption>
</figure>

Por lo general, una instalación de Internet consiste en una antena en la azotea, un inyector PoE (alimentación a través de Ethernet), un router y un punto de acceso wifi (normalmente, todos son equipos de red Ubiquiti). Durante la instalación, PhillyWisper y Philly Community Wireless hacen todo lo posible por afectar los edificios lo menos posible. En cada lugar, adaptamos nuestro trabajo de instalación para que la colocación de los equipos de red sea lo menos invasiva y lo más segura posible, de acuerdo con los estándares de la industria.

En la mayoría de los lugares, primero instalamos una antena de radio Ubiquiti LiteBeam en el techo de la casa, que recibe la señal de un sitio alto cercano administrado por PhillyWisper. Para instalar la antena en la azotea, los técnicos de PhillyWisper suben a un punto alto y montan la pequeña antena de radio (vea más abajo las imágenes de distintas técnicas de montaje), que apuntan con precisión hacia la torre más cercana. Al montar la antena nunca perforamos el sistema de techado y, siempre que es posible, aprovechamos estructuras existentes (chimeneas, tubos de ventilación, etc.). Si no es posible usar estructuras existentes, utilizamos un soporte de techo no penetrante, que lleva el lastre adecuado y descansa sobre una alfombrilla de goma encima de su techo.

La radio de la azotea se alimenta con un cable Ethernet apto para exteriores que baja por la fachada del edificio y entra en la casa (nuestros equipos usan PoE, así que podemos alimentar los dispositivos de exterior por Ethernet desde un tomacorriente interior). Nos aseguramos de que el recorrido del cable sea lo más discreto posible y de que el cable quede bien tensado para que no se sacuda con el viento. Si hay perforaciones existentes por donde entraban al edificio los cables de proveedores de Internet (ISP) anteriores, se usarán si es posible y se sellarán con masilla al terminar.

## Ejemplos de instalación

### Soportes de techo no penetrantes

Utilizamos soportes de techo no penetrantes (NPRM). Debajo del NPRM se coloca una alfombrilla gruesa de goma para proteger el techo, y se usan 4 bloques de cemento como lastre para asegurarlo.

<figure style="display: flex; justify-content: center; align-items: center; flex-direction: column;">
    <img src="../../../assets/images/installations/install/image7.jpg"
         alt="Un soporte de techo no penetrante con una LiteBeam instalada"
         style="width: 80%;">
    <figcaption>Un soporte de techo no penetrante con una LiteBeam instalada</figcaption>
</figure>

### Montaje en estructuras existentes del techo

También solemos usar soportes tipo J (J-arm) o soportes que quedaron de instalaciones de telecomunicaciones anteriores (antiguas antenas parabólicas de satélite) para montar nuestros equipos.

<figure style="display: flex; justify-content: center; align-items: center; flex-direction: column;">
    <div style="display: flex; justify-content: center; align-items: center; flex-direction: column;">
        <img src="../../../assets/images/installations/install/image9.jpg" alt="Una LiteBeam montada en un mástil previamente instalado en una chimenea" width="80%">
    </div>
    <figcaption>Una LiteBeam montada en un mástil previamente instalado en una chimenea</figcaption>
</figure>

## Descripción general de los puntos de acceso wifi

### Puntos de acceso wifi para exteriores

Los anfitriones de antena también tendrán un router en su casa, cerca de la ventana del frente. En algunos casos, podemos instalar un punto de acceso montado en la pared exterior de la casa para propagar la señal de banda ancha por el vecindario.

### Descripción general del router y los puntos de acceso para interiores

El cable Ethernet que baja de la azotea pasa por un inyector PoE, que añade alimentación eléctrica a la señal que el cable ya transporta. Así es como la antena de la azotea funciona con un tomacorriente interior común.

<figure style="display: flex; justify-content: center; align-items: center; flex-direction: column;">
    <img src="../../../assets/images/installations/install/image4.jpg"
         alt="Diagrama de un inyector PoE: la alimentación de un tomacorriente de pared y los datos de un switch sin PoE se combinan en un solo cable Ethernet" style="">
</figure>

El cable Ethernet alimentado se conecta a un Ubiquiti EdgeRouter-X (o posiblemente a otro router en el futuro) configurado para admitir redes de malla. El router gestiona el tráfico de cada uno de los puntos de acceso (APs) con los que está conectado en malla.

<figure style="display: flex; justify-content: center; align-items: center; flex-direction: column;">
    <img src="../../../assets/images/installations/install/image5.jpg"
         alt="Ubiquiti EdgeRouterX"
         style="width: 50%;">
    <figcaption>Ubiquiti EdgeRouterX</figcaption>
</figure>

Por último, un AP de malla Ubiquiti (las "orejas de conejo"; ¡mírelo y verá por qué!) se conecta al router y permite que los dispositivos dentro del alcance de su señal de radio se conecten a la red. Las orejas de conejo deben instalarse en un lugar con visibilidad de radio hacia los APs de malla de las instalaciones domésticas que estén a su alcance.

<figure style="display: flex; justify-content: center; align-items: center; flex-direction: column;">
    <img src="../../../assets/images/device-configs/mesh/Materials.jpeg"
         alt="Un Unifi UAP-AC-Mesh, conocido como orejas de conejo"
         style="width: 50%;">
    <figcaption>Un Unifi UAP-AC-Mesh, conocido como "orejas de conejo"</figcaption>
</figure>
