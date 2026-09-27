---
title: Configurar EdgeRouter X
---

<!-- TODO: machine-drafted Spanish translation — needs review by a fluent speaker. -->
!!! note "Traducción preliminar"
    Esta página es una traducción preliminar y está pendiente de revisión. Si encuentra un error, la [versión en inglés](../../../device-configuration/configure-edgerouter-x/) es la referencia.

# Configurar EdgeRouter X
Esta guía le explica paso a paso cómo configurar un Ubiquiti EdgeRouter X.

## Configuración con LiteBeam
Este método configura el ERX para usarlo en un sitio de instalación de PCW, con conexión a Internet a través de una LiteBeam.

### Hardware requerido
- [Router ERX](https://store.ui.com/collections/operator-edgemax-routers/products/edgerouter-x) y su cable de alimentación
- Cable Ethernet
- Computadora
- Adaptador Ethernet USB (si la computadora no tiene puerto Ethernet)

<figure style="display: flex; align-items: center; flex-direction: column;">
    <img src="../../../assets/images/device-configs/erx/hardware.jpg"
         alt="Materiales para configurar el ERX: configuración 'normal'" 
         style="width: 50%;">
    <figcaption>Materiales para configurar el ERX: configuración 'normal'</figcaption>
</figure>

### 1) Conecte el ERX

El ERX tiene cinco puertos Ethernet. `eth0` recibe alimentación por PoE (alimentación a través de Ethernet) y es el puerto por el que se
configura el router; `eth4` es el puerto WAN y el que envía PoE hacia una LiteBeam.

<figure class="device-diagram">
    <img class="device-art" src="../../../assets/images/equipment/edgerouter-x.svg"
         alt="Panel frontal del EdgeRouter X, con los cinco puertos Ethernet rotulados de izquierda a derecha: eth0/PoE IN, eth 1, eth 2, eth 3 y eth4/PoE OUT.">
    <figcaption>Distribución de los puertos del ERX, de izquierda a derecha</figcaption>
</figure>

1. Conecte el ERX a su cable de alimentación y enchufe el cable de alimentación en un tomacorriente.
2. Conecte el puerto `eth0` del ERX a su computadora con un cable Ethernet; use el adaptador Ethernet USB si su computadora no tiene puerto Ethernet.

<figure style="display: flex; align-items: center; flex-direction: column;">
    <img src="../../../assets/images/device-configs/erx/wiring.jpeg"
         alt="Cableado del ERX: el cable de alimentación está conectado en la parte trasera y la interfaz 'eth0' está conectada a la computadora."
         style="width: 50%;">
    <figcaption></figcaption>
</figure>
<figure style="display: flex; align-items: center; flex-direction: column;">
    <img src="../../../assets/images/device-configs/erx/eth0.jpeg"
         alt="Cableado del ERX: primer plano de la interfaz 'eth0'."
         style="width: 50%;">
    <figcaption>Conecte 'eth0' al puerto Ethernet de su computadora o al adaptador Ethernet USB</figcaption>
</figure>

### 2) Configure los ajustes de red
Siga estas instrucciones: [Configurar una IP estática en su computadora](configure-computer.md#configurar-una-direccion-ip-estatica)

### 3a) Configure el ER-X con el asistente
1. En su navegador, vaya al portal en [https://192.168.1.1](https://192.168.1.1).
2. Inicie sesión en el portal con el nombre de usuario `ubnt` y la contraseña `ubnt`.
    <figure style="display: flex; align-items: center; flex-direction: column;">
        <img src="../../../assets/images/device-configs/erx/login.jpeg"
             alt="Pantalla de inicio de sesión del ERX"
             style="width: 50%;">
        <figcaption>Pantalla de inicio de sesión del ERX</figcaption>
    </figure>

3. Cuando aparezca el mensaje `Use wizard?` (¿Usar el asistente?), presione 'yes' (sí).
    <figure style="display: flex; align-items: center; flex-direction: column;">
        <img src="../../../assets/images/device-configs/erx/wizard.jpeg"
             alt="Pantalla de configuración del ERX"
             style="width: 50%;">
        <figcaption></figcaption>
    </figure>

4. Cambie el `Port` (puerto) de `eth0` a `eth4`. Así el puerto funcionará como WAN para la antena LiteBeam. 
5. En `User Setup` (configuración de usuario), cree un usuario nuevo y establezca el nombre de usuario y la contraseña de PCW.
6. Presione `Apply` (aplicar) y siga las instrucciones para reiniciar el dispositivo.
7. Vuelva al portal e inicie sesión con el nombre de usuario y la contraseña de PCW (comuníquese con los responsables del proyecto para obtener estos datos).
8. En el `Dashboard` (panel), haga clic en `Actions` (acciones) de `eth4` para activar PoE.
9. Por último, haga clic en la pestaña `System` (sistema), en la parte inferior izquierda de la consola.
10. Escriba el nombre de host (*host name*) del dispositivo.
11. Configure la dirección DNS como 1.1.1.1.

Para comprobar que un dispositivo está bien configurado, revise los ajustes de las pestañas `Dashboard` y `System`. Para verificar que la WAN está asignada a `eth4`, vaya a la sección `Firewall/Nat`. En la pestaña NAT, compruebe que `Masquerade` esté asignado a `eth4` para el enmascaramiento (*masquerade*) de la WAN.

### 3b) Configure el ER-X con un archivo de configuración
1. Descargue el [archivo de configuración del ERX](../../assets/configs/erx-config.tar.gz)
2. En su navegador, vaya al portal en [https://192.168.1.1](https://192.168.1.1).
3. Inicie sesión en el portal con el nombre de usuario `ubnt` y la contraseña `ubnt`, como se indicó arriba.
4. Cuando aparezca el mensaje `Use wizard?`, presione 'no'.
5. Presione la pestaña `System` en la parte inferior de la página.
6. En la sección `Restore Config` (restaurar configuración), presione `Upload a file` (subir un archivo) y seleccione el archivo de configuración del ERX que descargó.
<figure style="display: flex; align-items: center; flex-direction: column;">
    <img src="../../../assets/images/device-configs/erx/system.jpeg"
         alt="Pantalla de configuración del ERX"
         style="">
    <figcaption>En 'Restore Config', haga clic en 'Upload a file' y suba la configuración del ERX que descargó antes.</figcaption>
</figure>

7. El ERX se reiniciará con la nueva configuración.
8. Para hacer más ajustes, puede volver a iniciar sesión en el portal con el nombre de usuario y la contraseña de PCW.
9. Asegúrese de seguir las instrucciones (pasos 10 y 11 de la sección anterior) para actualizar el nombre de host y la dirección DNS en la pestaña `System`.

## Configuración en cascada (downstream)
Este método permite que el ERX se conecte a Internet a través del router de su casa. 

### 1) Conecte el ERX
1. Consulte [Conecte el ERX](#1-conecte-el-erx) en la sección anterior. 

### 2) Configure los ajustes de red
2. Siga estas instrucciones: [Configurar una IP estática en su computadora](configure-computer.md#configurar-una-direccion-ip-estatica).
3. **DESACTIVE** el wifi o su conexión a Internet. 
!!! info ""
      Así se asegura de que, en el siguiente paso, su solicitud llegue al ERX y no al router de su casa. 

### 3) Configure el ERX 
1. En su navegador, vaya al portal en [https://192.168.1.1](https://192.168.1.1).
2. Inicie sesión en el portal con el nombre de usuario `ubnt` y la contraseña `ubnt`.
    <figure style="display: flex; align-items: center; flex-direction: column;">
        <img src="../../../assets/images/device-configs/erx/login.jpeg"
             alt="Pantalla de inicio de sesión del ERX"
             style="width: 50%;">
        <figcaption>Pantalla de inicio de sesión del ERX</figcaption>
    </figure>

3. Cuando aparezca el mensaje `Use wizard?` (¿Usar el asistente?), presione 'yes' (sí).
    <figure style="display: flex; align-items: center; flex-direction: column;">
        <img src="../../../assets/images/device-configs/erx/wizard.jpeg"
             alt="Pantalla de configuración del ERX"
             style="width: 50%;">
        <figcaption></figcaption>
    </figure>

4. Cambie el `Port` (puerto) de `eth0` a `eth4`. 

5. Haga clic en 'LAN Ports' (puertos LAN) y asígnele al ERX una dirección IP **diferente** a la del router de su casa (que no sea `192.168.1.1`), en una subred diferente. Por ejemplo, configure el ERX en `192.168.5.1`.

6. En `User Setup` (configuración de usuario), cree un usuario nuevo y establezca el nombre de usuario y la contraseña de PCW.

7. Reinicie su router y reinicie el ERX. 

8. Vuelva al portal e inicie sesión con el nombre de usuario y la contraseña de PCW (comuníquese con los responsables del proyecto para obtener estos datos).

9. Por último, haga clic en la pestaña `System` (sistema), en la parte inferior izquierda de la consola.

10. Escriba el nombre de host (*host name*) del dispositivo.

11. Configure la dirección DNS como 1.1.1.1.

12. Restablezca la configuración de red de su computadora: elimine la IP estática que estableció en el [paso 2](#2-configure-los-ajustes-de-red_1) y vuelva a poner la conexión en modo dinámico (Dynamic). 

13. Vuelva a conectarse al ERX e inicie sesión con el nombre de usuario y la contraseña de PCW. 

14. Conecte el puerto `eth4` del ERX a un puerto LAN de su router. Ahora debería poder acceder a Internet a través del ERX. 

15. Adopte el ERX copiando la clave de UISP (*UISP key*). 

16. Si es necesario, actualice el firmware del ERX. 

## Notas de instalación
Cuando instale el ER-X en una casa con una LiteBeam en la azotea y un AP de malla, recuerde que la configuración típica es:

1. El puerto `eth0` sirve de paso (*passthrough*) para el PoE que llega desde un adaptador enchufado en un tomacorriente.
2. El puerto `eth1` se usa para el puerto LAN del adaptador que alimenta el primer AP de malla de PCW. Los puertos `eth2` y `eth3` pueden usarse para conexiones por cable a otros APs de malla; cada uno de ellos debe alimentarse con su propio adaptador PoE.
3. El puerto `eth4` sirve como puerto WAN, con PoE de paso para comunicarse con la LiteBeam de la azotea y alimentarla. 
