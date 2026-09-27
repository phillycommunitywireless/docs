---
title: Evaluación del edificio
---

<!-- TODO: machine-drafted Spanish translation — needs review by a fluent speaker. -->
!!! note "Traducción preliminar"
    Esta página es una traducción preliminar y está pendiente de revisión. Si encuentra un error, la [versión en inglés](../../../installations/buildingassessment/) es la referencia.

PCW instala WiFi con regularidad en una gran variedad de edificios, como casas en hilera (rowhomes), edificios multifamiliares (MDUs), centros comunitarios y espacios públicos como parques y jardines.

Para evaluar si un edificio es adecuado para una instalación, debemos hacernos las siguientes preguntas:

* **¿Tiene el edificio línea de visión (LoS) hacia un sitio alto de PhillyWisper, o está muy cerca de un nodo de malla de PCW existente?**
    * Sin LoS directa hacia un sitio alto o un nodo existente, el rendimiento de la radio de enlace ascendente (uplink) se reducirá considerablemente (si es que logra conectarse).
    * Google Earth puede ser una herramienta útil para determinar si existe una posible LoS, pero en muchos casos puede ser necesaria una visita al lugar.
    * El follaje de los árboles puede causar interferencias importantes: ¡los lugares que funcionan en invierno pueden quedar bloqueados por el follaje en verano!
    * Además, las construcciones nuevas aparecen de repente. Es importante verificar en persona las condiciones del lugar, ya que Google Maps y herramientas similares pueden no tener actualizado el entorno.

* **¿El acceso a la azotea o al último piso del edificio es fácil, seguro y sencillo?**
    * ¿Se necesitan escaleras de mano? ¿Hay escaleras o una escotilla de acceso a la azotea?
    * Lo ideal es instalar las LiteBeam en la azotea, ya sea en una estructura existente del techo, con un soporte tipo J (j-arm) en la pared o con un soporte de techo no penetrante.
    * ¿Tenemos permiso para instalar equipos en el edificio o en las estructuras de la azotea?
    * PCW solo instala en techos planos, salvo raras excepciones.

* **¿Hay acceso a electricidad?**
    * Si la toma está en el exterior, ¿está protegida?
    * ¿Será necesario usar la toma de corriente para otra cosa? ¿Tienen acceso a ella otras personas que podrían desconectar nuestro equipo?
    * ¿Hay perforaciones existentes que podamos reutilizar para llevar la alimentación a través de Ethernet (PoE) desde el interior?
    * PCW NO perfora techos, ya que es muy difícil impermeabilizarlos.

* **¿Hay maneras fáciles de montar los puntos de acceso?**
    * Por ejemplo: postes existentes a los que podríamos simplemente sujetar los AP con amarres plásticos (zip ties), en lugar de traer un soporte de techo no penetrante o un soporte tipo J.
    * ¿Cuánto cable tendremos que tender?
    * ¿Qué tipo de puntos de acceso se necesitarán? Algunos no son resistentes a la intemperie y solo pueden usarse en interiores.
    * ¿Existe la posibilidad de que el montaje de los puntos de acceso dañe el techo o las paredes?
    * ¿Hay infraestructura de Internet existente (instalaciones anteriores de cable coaxial o de fibra óptica) que debamos tener en cuenta? Los cables que corren en paralelo pueden interferir entre sí y reducir el rendimiento de ambas conexiones.

* **Si se necesita mantenimiento, ¿podremos regresar en el futuro?**

Por ejemplo, este es un lugar ideal para una instalación:

<figure style="display: flex; align-items: center; flex-direction: column;">
    <img src="/assets/images/installations/install/nkcdc_roof.png"
         alt="Un lugar ideal para una instalación en azotea"
         style="width: 80%; ">
    <figcaption>Un lugar ideal para una instalación en azotea en Kensington</figcaption>
</figure>

* La azotea es plana y está libre de escombros, con mucho espacio para soportes de techo no penetrantes.
* El edificio es más alto que casi todos los demás edificios de la zona, lo que le da LoS despejada tanto hacia los sitios altos de PhillyWisper como hacia otros posibles sitios PtP/PtMP.
* Hay electricidad en la azotea; en este caso, tomacorrientes GFCI con tapa protectora.
