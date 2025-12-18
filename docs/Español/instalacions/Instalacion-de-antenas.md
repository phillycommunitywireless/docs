---

---
# Instalación de antenas

Philly Community Wireless se ha asociado con PhillyWisper para instalar antenas para la red wifi gratuita en los tejados del barrio de Norris Square Park. PhillyWisper es un proveedor de servicios de Internet inalámbrico (WISP), lo que significa que nuestro proyecto ofrece Internet a nuestros clientes a través de la tecnología de radio.

## Proceso de instalación en la azotea

La mayoría de las instalaciones se realizaron en el siguiente orden:

1. Examine el edificio y la azotea para evaluar la línea de visión (LOV) de la torre de origen de la ubicación alta para la señal de banda ancha.
2. Instale la antena en la azotea y conecte el cable al edificio.
3. Configure el router wifi y los kits de malla (para obtener más información, consulte nuestra [Configure AP-Mesh Guide](./configure-ap-mesh.md) y nuestra [Configure ERX Router Guide](./configure-erx.md)).
4. Es posible que instale una antena montada en la pared para propagar la señal por la calle.

## Duración de las instalaciones de antenas

Normalmente, las instalaciones tardan entre dos y cuatro horas en completarse, pero en algunos casos pueden tardar más. El proceso de instalación completo, desde una antena en el techo hasta un kit de malla montado en la pared, puede implicar 2-3 visitas, cada una de las cuales implica una o dos horas de trabajo.

# Hardware para la instalación

Las instalaciones en la azotea constan de una antena en la azotea, un inyector de alimentación a través de Ethernet, un router y un punto de acceso de malla. Philly Community Wireless y PhillyWisper utilizan principalmente radios y equipos de red Ubiquiti. Como cada techo es diferente, la instalación se personaliza para cada ubicación para garantizar la colocación más segura de acuerdo con los estándares del sector.

En general, instalamos una antena Ubiquiti LiteBeam en el techo de la casa, que recibe la señal de una torre PhillyWisper. La antena se conecta al hogar mediante un cable Ethernet. Actualmente, esta parte de la instalación debe ser completada por un técnico de PhillyWisper. Para fines de instalación, esto significa que los técnicos de PhillyWisper tendrán que montar una antena de radio pequeña (aproximadamente 14 x 11 x 11 pulgadas) a la altura del techo y apuntar con precisión a la torre más cercana.

PhillyWisper se esfuerza al máximo por impactar los edificios durante la instalación. Utilizan técnicas no invasivas al montar la radio (consulte las imágenes adjuntas de las distintas técnicas de montaje que aparecen a continuación). Nunca penetran en el sistema de techado mismo y ellos intentan y utilizan estructuras preexistentes (chimeneas, tubos de ventilación, etc) cuando es posible.

Si las estructuras preexistentes no son una opción, utilizarán un soporte de techo no penetrante, que se pesa correctamente y descansa sobre una alfombrilla de goma en la parte superior de su techo. A continuación, aseguran un cable de red estabilizado a los rayos UV para exteriores desde la radio del techo, hacia abajo a lo largo del exterior del edificio y el interior donde se ubicará el router WiFi.

Tanto Philly Community Wireless y PhillyWisper como la de la comunidad Philly garantizan que el recorrido del cable sea lo más discreto posible y garantizan que el cable tenga mucha tensión para que no se solapa con el viento. Si hay alguna penetración preexistente que entra en el edificio de ISP anteriores, utilizarán eso si es posible y calafatearás cuando termine.

## Ejemplos de instalación

### Soportes de techo no penetrantes

Utilizamos soportes de techo no penetrantes (NPRM). Una alfombra de goma gruesa se coloca debajo del NPRM para proteger el techo. Los bloques de cemento se utilizan como lastre para asegurar el NPRM:

![Non-penetrating roof mount 1](../assets/images/install/image1.jpg)
![Non-penetrating roof mount 2](../assets/images/install/image2.jpg)

### Antenas montadas en la pared

La siguiente imagen muestra dos mástiles montados en la pared con radios, junto con un interruptor exterior y una caja de conexiones.

El mástil de la izquierda tiene una radio Ubiquiti AF-24 que funciona a 24 GHz y proporciona una conexión de retorno de 1,4 Gbps al centro de datos.

![Wall mounted antenna 1](../assets/images/install/image6.jpg)
![Wall mounted antenna 2](../assets/images/install/image7.jpg)
![Wall mounted antenna 3](../assets/images/install/image8.jpg)
![Wall mounted antenna 4](../assets/images/install/image9.jpg)

El mástil de la derecha tiene radios PTMP con antenas de bocina simétricas. Las radios proporcionan servicio a clientes individuales.

El dispositivo blanco cuadrado entre y debajo de los mástiles es un Ubiquiti EP-S16, un conmutador de red para exteriores. Se suministra alimentación de 54 V CC al EP-S16, que a su vez suministra alimentación a las radios mediante POE (alimentación de Ethernet).

# Instalación de kit de malla para hosts de antena en la azotea

Los anfitriones de las instalaciones en la azotea también albergará un router en la casa cerca de la ventana al frente de la casa. En algunos casos podemos instalar una antena montada en la pared en el exterior de la casa para propagar la señal de banda ancha a través del vecindario.

Proporcionamos un kit con un inyector PoE y un AP de malla de orejas de conejo. Philly Community Wireless puede instalar el kit, o el residente puede instalar las orejas de conejo en cualquier lugar dentro de su casa, siempre y cuando otros puntos de acceso de malla estén dentro del alcance de radio (estamos planeando sugerir la entrada de la casa o el porche -- los puntos de acceso son impermeables).

## Descripción general del kit de malla

El cable Ethernet pasa a través de un inyector de alimentación a través de Ethernet (PoE), que añade alimentación a la señal que transporta el cable Ethernet y permite que los dispositivos de bajada se alimenten únicamente a través de Ethernet.

![PoE Injector](../assets/images/install/image4.jpg)

El cable Ethernet alimentado está conectado a un Ubiquiti EdgeRouter-X (o posiblemente a otro router en el futuro) configurado para admitir redes de malla. El router gestiona el tráfico de cada uno de los puntos de acceso (AP) con los que está conectado en malla.

![EdgeRouter-X](../assets/images/install/image5.jpg)

Por último, un Ubiquiti Mesh AP (“orejas de conejito” porque miren a ellos!) está conectado al router y permite que los dispositivos de su rango de señal de radio se conecten a la red. Las orejas de conejito deben instalarse en una ubicación que sea radiovisible para los puntos de acceso de malla en las instalaciones domésticas a su alcance.

![Ubiquiti Mesh AP](../assets/images/install/image3.jpg)

Para obtener más información sobre el kit de malla, consulte nuestra [Configure AP-Mesh Guide](./configure-ap-mesh.md)
