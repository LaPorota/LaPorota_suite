# Info

Permite capturar el tráfico que pasa por una interfaz de red.

# Iniciar airodump

    sudo airodump-ng <interface>

# Criterios de captura

Usualmente vamos a usar 3 criterios al momento de capturar tráfico:

| Option | Desc |
|------|-------|
| -w | Nos permite agregar un prefijo a los archivos generados de la captura |
|--bssid | Nos permite indicar que bssid capturar de manera específica |
| -c | Fuera a airodump a capturar un canal en específico |


# La finalidad de su uso

El fin de esta utilidad es capturar un protocolo de enlace(handshake) WPA. Esto aparecerá en la primer línea superior.

    CH  2 ][ Elapsed: 12 s ][ 2011-11-06 13:31 ][ WPA handshake: C8:BC:C8:FE:D9:65

Luego de esto, podemos realizar una nueva captura sobre la bssid de la que encontramos el handshake.
