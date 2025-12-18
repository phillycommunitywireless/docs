---

---
# Configurar ERX Router

Esta guía le guiará a través de la configuración de un Ubiquiti EdgeRouter X.

## Hardware requerido

* Router e cable de alimentación
* Tranque cable
* Computador
* Adaptador Ethernet USB (si la computadora no tiene puerto Ethernet)

![Hardware](../assets/images/erx/hardware.jpg)

## Pasos de instalación

### Establecer IP estática en el equipo

Ver [./static-ip](./static-ip.md)

### Conecte el ERX

1. Conecte el ERX a su cable de alimentación y conecte el cable de alimentación a una toma de corriente.
2. Conecte el puerto `eth0` del ERX al ordenador con un cable Ethernet, utilizando el adaptador Ethernet USB si no dispone de un puerto Ethernet.

![Ports](../assets/images/erx/wiring.jpeg)
![Ports](../assets/images/erx/eth0.jpeg)

### Configurar ERX

1. Descargue el [ERX config file](../assets/configs/erx-config.tar.gz)
2. Navegue al portal en [https://192.168.1.1](https://192.168.1.1) en su navegador.
3. Regístrese sesión en el portal con nombre de usuario `ubnt`, contraseña `ubnt`.
   ![Login](../assets/images/erx/login.jpeg)
4. En el `Use wizard?` , presione no.
   ![Login](../assets/images/erx/wizard.jpeg)
5. Presione la pestaña `System` en la parte inferior de la página.
6. En la sección `Restore Config` , presione `Upload a file` y seleccione el archivo de configuración de ERX que descargó.
   ![Login](../assets/images/erx/system.jpeg)
7. El ERX se reiniciará utilizando la nueva configuración.
8. ¡Eso es todo! Si necesita realizar más configuración, puede volver a iniciar sesión en el portal utilizando el nombre de usuario `pcwadmin`, y una contraseña que puede obtener de los mantenedores del proyecto.
