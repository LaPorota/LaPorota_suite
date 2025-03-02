# Info

- Es muy útil para desencriptar paquetes capturados de tráfico una vez que encontramos la clave de una red.
- Es muy útil para leer y analizar el tráfico capturado de una red.
- Nos permite limpiar los headers de una captura wireless desencriptada.
- Las capturas wireless tienen un montón de frames que no nos interesan.

Luego de conseguir la key, podemos pasarle el archivo con la captura de tráfico y airdecap lo va a desencriptar creando un nuevo archivo con la información en texto plano.

# remover cabeceras de una captura desencriptada

    sudo airdecap-ng -b <bssid>  <.cap>

    
# Desencriptar capturas WEP

    airdecap-ng -w <WEP-key> <capture-file>

# Desencriptar capturas WPA

    airdecap-ng -p <passphrase> <capture-file> -e <essid>
