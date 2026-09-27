---
title: Nodos solares de malla
---

<!-- TODO: machine-drafted Spanish translation — needs review by a fluent speaker. -->
!!! note "Traducción preliminar"
    Esta página es una traducción preliminar y está pendiente de revisión. Si encuentra un error, la [versión en inglés](../../../installations/solar/) es la referencia.

# Descripción general de los nodos solares de malla

Philly Community Wireless apoya activamente espacios verdes sostenibles enfocados en la conservación ambiental y el uso eficiente de los recursos. Con nodos solares autónomos (sin conexión a la red eléctrica) diseñados por [Holobiont Lab](https://holobiontlab.org/), hemos instalado puntos de acceso WiFi alimentados por energía solar en huertos y otros espacios donde la electricidad es costosa o no está fácilmente disponible. Philly Community Wireless también está trabajando para alimentar sensores inteligentes, como el [monitor de calidad del aire PurpleAir](https://www.purpleair.com/products/classic-plus-air-quality-monitor), con nodos solares modificados para dar seguimiento a la salud ambiental.

## Especificaciones del hardware

* Caja para exteriores resistente a la intemperie
* Panel solar de 25-50W
* Cualquier combinación de baterías reutilizadas adecuadas, con voltaje nominal de 12V
* Un controlador de carga
* Un desconectador por baja temperatura (según el tipo de batería)
* Un convertidor elevador de 12V a 24V y 3A
* Un nodo de malla: para empezar, el punto de acceso de malla Ubiquiti de 24V

## Instalaciones

En 2021, PCW instaló un nodo solar de malla en Colobo Gardens, de Norris Square Neighborhood Projects. Por lo general, las baterías duran por lo menos un par de años antes de necesitar reemplazo. El punto de acceso está en la parte superior de un mástil de bambú, a una altura suficiente para sobrepasar las estructuras del huerto, con el panel solar y la caja montados debajo.

<figure style="display: flex; align-items: center; flex-direction: column;">
    <img src="/assets/images/installations/solar/full_solar_node.jpg"
         alt="El nodo solar de malla completo en Colobo Gardens: el punto de acceso en lo alto del mástil de bambú, con el panel solar montado en el techo debajo"
         style="width: 50%; height: 50%;">
    <figcaption>El nodo solar de malla completo en Colobo Gardens: el punto de acceso en lo alto del mástil de bambú, con el panel solar montado en el techo debajo</figcaption>
</figure>

<figure style="display: flex; align-items: center; flex-direction: column;">
    <img src="/assets/images/installations/solar/solar_panel_mount.jpg"
         alt="El panel solar en su soporte inclinado en el borde del techo, con el cableado que baja hasta la caja"
         style="width: 50%; height: 50%;">
    <figcaption>El panel solar en su soporte inclinado en el borde del techo, con el cableado que baja hasta la caja</figcaption>
</figure>

## La caja de la batería solar

La caja resistente a la intemperie contiene todo lo que no es el panel ni el punto de acceso: la batería, el controlador de carga y el inyector PoE, que lleva la alimentación hasta el AP a través de un solo cable Ethernet.

<figure style="display: flex; align-items: center; flex-direction: column;">
    <img src="/assets/images/installations/solar/solar_with_info.jpg"
         alt="La caja abierta, con la batería, el controlador de carga y el inyector PoE rotulados"
         style="width: 50%; height: 50%;">
    <figcaption>El interior de la caja en Colobo Gardens</figcaption>
</figure>

## Solución de problemas de los nodos solares de malla

Si necesita más ayuda para resolver problemas, consulte la sección 'Troubleshooting' (solución de problemas, pág. 12) de la [Meshbox Documentation](https://holobiontlab.org/docs/meshBoxDocumentation.pdf) (en inglés). La [documentación de meshbox](https://holobiontlab.org/r&d/meshbox) de Holobiont Lab explica con más detalle el diseño en el que se basan estos nodos.

Los problemas comunes incluyen:

* Descarga de la batería: la batería LiFePO4 debe marcar entre 12.5V y 14.6V.
  * Si marca menos de 12.5V, el sistema de gestión de la batería se apagará para ahorrar energía.
* Las conexiones entre la caja y el controlador de carga, así como las conexiones entre el controlador de carga y el AP.
  * Debe haber una luz **roja** en el controlador de carga y una luz **verde** en el inyector PoE.
* Temperaturas bajas o mal tiempo

## Más recursos

Consulte [Recursos de tecnología verde](green-technology.md) para conocer programas solares, organizaciones de agricultura urbana e iniciativas de monitoreo ambiental en Filadelfia.
