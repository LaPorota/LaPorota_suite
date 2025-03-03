
# Listar las redes accesibles

    sudo iwlist <interfaz> s | grep 'Cell\|Quality\|ESSID\|IEEE'
# Conectarse a una red WEP

#### 1) creamos un archivo de configuración con los datos de la conexión .conf

    network={
    	ssid="nombre_red"
        key_mgmt=NONE
        wep_key0=<key>
        wep_tx_keyidx=0
    }

#### 2) nos conectamos

    sudo wpa_supplicant -c wep.conf -i <interfaz>

#### 3) Pedimos una ip

    sudo dhclient <interfaz>

# Conectarse a una WPA

#### 1) Creamos un archivo de conexión .conf

    network={
    	ssid="HackMe"
        psk="password123"
    }

#### 2) Nos conectamos

    sudo wpa_supplicant -c wpa.conf -i <interfaz>

#### 3) Matamos cualquier ip de una conexión anterior

    sudo dhclient wlan0 -r

#### 4) pedimos una nueva ip

    sudo dhclient wlan0

# Conectarse a una red WPA ENTERPRISE

Lo mismo que lo anterior pero con otro archivo de configuración

#### 1) Creamos un archivo de configuración .conf

    network={
      ssid="HTB-Corp"
      key_mgmt=WPA-EAP
      identity="HTB\Administrator"
      password="Admin@123"
    }

# MAC spoof

Muchas veces las redes tienen una whitelist de MACs que pueden conectarse a la AP. Debido a esto, aunque tengamos los datos correspondientes para conectarnos, no podremos lograrlo. Para esto haremos un spoof de una MAC de un cliente que se encuentra conectado.


#### 1) Damos de baja la interfaz

    sudo ifconfig <interfaz> down

#### 2) Cambiamos nuestra mac por la MAC de algún cliente(station) conectado a la AP

    sudo macchanger <interfaz> -m <MAC>

#### 3) Levantamos la interfaz

    sudo ifconfig <interfaz> up

#### 4) Nos conectamos otra vez
