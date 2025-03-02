# Checkear las capacidades de nuestra interfaz de red

    iw list

# Buscar redes disponibles

    iwlist <interfaz> scan |  grep 'Cell\|Quality\|ESSID\|IEEE'

# Ver los canales disponibles en la interfaz

    iwlist wlan0 channel

# Cambiar el canal de la interfaz

    sudo ifconfig wlan0 down
    sudo iwconfig wlan0 channel 64
    sudo ifconfig wlan0 up

# Camiar la frecuencia de la interfaz

    sudo ifconfig wlan0 down
    sudo iwconfig wlan0 freq "5.52G"
    sudo ifconfig wlan0 up
# Setear la interfaz en un canal

    sudo iw dev wlan0mon set channel 1
