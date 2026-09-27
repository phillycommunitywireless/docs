---
title: Solución de problemas de dispositivos Unifi
---

<!-- TODO: machine-drafted Spanish translation — needs review by a fluent speaker. -->
!!! note "Traducción preliminar"
    Esta página es una traducción preliminar y está pendiente de revisión. Si encuentra un error, la [versión en inglés](../../../device-configuration/troubleshoot-devices/) es la referencia.

No todos los dispositivos funcionarán perfectamente. Además, los dispositivos instalados al aire libre estarán expuestos a los elementos, principalmente al calor y la humedad, y se desgastarán naturalmente con el tiempo. Dicho esto, los puntos de acceso para exteriores a menudo han durado 5 años o más. En Philadelphia, rara vez tenemos un clima tan severo que dañe nuestros radios.  

## Indicadores LED de estado de los AP Unifi
Cada AP Unifi tiene un LED que indica su estado actual. 

* **LED apagado** - El AP está fuera de línea. 
* **Blanco intermitente** - El AP está recibiendo alimentación y se está iniciando 
* **Blanco fijo** - El AP terminó su configuración y está listo para ser adoptado. 
    * Vea [Configurar AP de malla Unifi](configure-ap-mesh.md) para las instrucciones de adopción. 
* **Azul fijo** - El AP está adoptado y funciona con normalidad; en nuestro caso, transmitiendo la red de Philly Community Wireless. 
* **Blanco/azul intermitente** - Se está actualizando el firmware del AP. **No desconecte el AP**.
* **Azul intermitente** - El AP perdió la conectividad y está buscando un AP principal o un enlace ascendente (*uplink*). 
* **Azul/apagado intermitente rápido** - Se activó la función 'Locate' (localizar) desde el Unifi Controller.  

Consulte [esta página](https://help.ui.com/hc/en-us/articles/204910134-Understanding-Device-LED-Status-Indicators) (en inglés) para obtener más información sobre los indicadores LED de estado. 

## Solución de problemas de puntos de acceso
### El punto de acceso no enciende; el dispositivo se reinicia pero no permanece en línea 
**Observaciones**: No hay luces; el dispositivo está fuera de línea o no aparece en el controlador.

**Posibles causas y soluciones**:
* **Fuente de alimentación inadecuada** - Revise el inyector PoE conectado al dispositivo y asegúrese de que la luz esté encendida y de que el voltaje sea el correcto.
* **Conexión de alimentación o cable Ethernet defectuoso (si usa PoE)** - Pruebe si un cable Ethernet diferente suministra alimentación, para comprobar que el inyector PoE funciona correctamente. Vuelva a probar el cable defectuoso.

### No se puede conectar por SSH al AP para adoptarlo
* **Observaciones** - Las luces están encendidas y el dispositivo parece estar en línea, pero no se puede acceder a él por SSH.

**Posibles causas y soluciones**
* **Se le asignó una dirección IP distinta a la predeterminada** - La configuración de fábrica de la mayoría de los dispositivos Unifi establece su IP en `192.168.1.20` antes de la adopción; sin embargo, si esa dirección ya está en uso, es posible que se le asigne otra dirección IP al dispositivo. Pruebe usar `arp -a` para encontrar el AP.
* **Asegúrese de que su dirección IP estática esté asignada correctamente** - Revise las instrucciones en [Configurar una IP estática](configure-computer.md#configurar-una-direccion-ip-estatica) y asegúrese de estar usando la subred `192.168.1.x`.

### Se envió la solicitud de adopción, pero el dispositivo no aparece en el controlador
* **Observaciones** - El dispositivo parece estar en línea y se envió la solicitud de adopción mediante `sudo set-inform`, pero la solicitud no aparece en el controlador.

**Posibles causas y soluciones**
* **Asegúrese de que el dispositivo esté conectado a Internet** - Revise las instrucciones en [Compartir una conexión WiFi por Ethernet](configure-computer.md#compartir-una-conexion-wifi-por-ethernet) y asegúrese de que el AP tenga acceso a Internet
* **Actualice el controlador** - A veces puede haber una demora entre el envío de la solicitud y su aparición en el controlador.

### El dispositivo aparece como 'isolated' (aislado)
* **Observaciones** - El dispositivo está marcado como 'isolated' en el Unifi controller

**Posibles causas y soluciones**
* **El dispositivo pierde la conectividad hacia la red superior** - Un AP pasa a estar 'isolated' si ya no puede conectarse con el Unifi controller. Asegúrese de que no se hayan hecho cambios en la configuración de la red que impidan que el AP se comunique con el controlador. Primero, reinicie el AP desconectándolo y volviéndolo a conectar (desconéctelo del inyector PoE, o conéctese de forma remota por `ssh` y ejecute `reboot`). Si el AP está en malla, conectarlo por cable sin reiniciarlo también puede hacer que vuelva a la red. Si esto no funciona, elimine el AP y vuelva a adoptarlo. Si el problema persiste, reinicie el ERX o borre las concesiones (*leases*) de DHCP. 

## Solución de problemas de los ERX
### El ERX no enciende
**Observaciones**: No hay luces; el dispositivo está fuera de línea o no aparece en UISP.

**Posibles causas y soluciones**:
* **Conexión de alimentación o cable Ethernet defectuoso (si usa PoE)** - Pruebe el ERX con otra fuente de alimentación de 9 V y compruebe si el ERX se conecta. Pruebe cambiar a una fuente de alimentación de 9 V diferente. Si usa PoE, asegúrese de que el voltaje sea el correcto.

## Comandos de terminal útiles para redes 
* `ipconfig` (Windows)/`ifconfig` (Unix) - muestra las interfaces de red e información relacionada: dirección IP, máscara de subred y puerta de enlace predeterminada. 
* `arp -a` (Windows/Unix)- Muestra la tabla del protocolo de resolución de direcciones (ARP, por sus siglas en inglés): la correspondencia entre direcciones IP y direcciones MAC. 
    * `ip neigh show` - Comando equivalente.  
