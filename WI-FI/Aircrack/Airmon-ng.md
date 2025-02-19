# Info

Permite habilitar y deshabilitar el moso monitor de la interfaz wireless

### Listar interfaces y su estado

    sudo airmon-ng

### Buscar servicios problemáticos

Hay servicios que pueden generar problemas con airmon-ng. Podemos buscarlos con la flag check

    sudo airmon-ng check

Luego podemos terminarlos agregando la flag kill


    sudo airmon-ng check kill

### Poner nuestra interface en modo monitor

    sudo airmon-ng start <interface>

Podemos también seleccionar un channel específico para que la interfaz monitoree

    sudo airmon-ng start <interface> <channel>

Para ver si la interface inició en modo monitor en el canal indicado

    sudo iw dev wlan0mon info

### Apagar el modo monitoreo

    sudo airmon-ng stop <interface>




