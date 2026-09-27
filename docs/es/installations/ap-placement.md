---
title: Ubicación de los puntos de acceso
---

<!-- TODO: machine-drafted Spanish translation — needs review by a fluent speaker. -->
!!! note "Traducción preliminar"
    Esta página es una traducción preliminar y está pendiente de revisión. Si encuentra un error, la [versión en inglés](../../../installations/ap-placement/) es la referencia.

# Ubicación de los puntos de acceso

El lugar donde se coloca un punto de acceso importa tanto como el modelo de punto de acceso que se utiliza. Esta página explica cómo PCW
decide dónde colocar los AP: la diferencia entre un hub (sitio central) y un nodo, y qué tener en cuenta cuando un
nodo se conecta en malla de forma inalámbrica en lugar de por cable.

## Hubs y nodos

Los nodos de malla son instalaciones en las que no usamos una antena LiteBeam, sino que colocamos un punto de acceso
inalámbrico que se conecta en malla a un punto de acceso cercano, el cual está conectado por cable a un router y a una LiteBeam en un hub local.

Si un sitio puede ser un hub se decide durante la [evaluación del edificio](buildingassessment.md):
un hub necesita línea de visión directa con un sitio alto (torre) de PhillyWisper. Un nodo no la necesita, pero sí requiere un buen
enlace inalámbrico de regreso a un hub, que es el tema del resto de esta página.

## Consideraciones al instalar un nodo de malla

La guía de Ubiquiti [Considerations for Optimal Wireless Mesh Networks](https://help.ui.com/hc/en-us/articles/115002262328-Considerations-for-Optimal-Wireless-Mesh-Networks)
(consideraciones para redes de malla inalámbricas óptimas, en inglés) es nuestra referencia de trabajo. Los puntos que surgen con más frecuencia en las instalaciones de PCW son:

* **Las redes de malla deben ser complementarias**: aunque una red de malla puede funcionar de manera comparable a una red cableada, la calidad y la velocidad de la conexión pueden verse muy afectadas por el ruido de radiofrecuencia (RF) y por obstáculos entre los AP, como paredes, árboles u otras estructuras.
* **Se deben minimizar los "saltos" de la malla**: un AP en malla debe tener un solo "padre". Cada "salto" de la malla, es decir, cada conexión en malla entre AP, provoca una disminución significativa del rendimiento. Lo ideal es un máximo de dos "saltos"; por ejemplo, un AP de malla se conecta a otro AP de malla, que a su vez se conecta a un AP cableado.
* **Limite las conexiones simultáneas a un mismo "padre"**: del mismo modo, conectar demasiados AP en malla al mismo "padre" genera más ruido de RF y más exigencias de rendimiento sobre ese AP, lo que reduce el rendimiento y la estabilidad.
* **Asegure una señal fuerte entre los AP en malla**: lo ideal es que un AP en malla tenga línea de visión (LoS) despejada con su AP padre. Se recomienda una intensidad de señal de -60 dBm para un rendimiento óptimo. Procure que haya los menos obstáculos posibles entre el AP en malla y el padre, como paredes, árboles, muebles, etc.

## Ubicación en exteriores

Los AP de exterior deben montarse donde tengan visibilidad de radio con los AP de malla de las instalaciones domésticas que estén
dentro de su alcance, y a una altura suficiente para sobrepasar lo que haya a su alrededor. En los [nodos solares](solar.md), eso normalmente
significa que el AP va en la parte superior del mástil, con el panel y la caja montados debajo.

Para saber cómo configurar un AP una vez colocado, consulte la guía
[Configurar APs Unifi](../device-configuration/configure-ap-mesh.md).
