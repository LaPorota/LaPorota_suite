# Info

Permite capturar el tráfico que pasa por una interfaz de red.

Por defecto Airodump busca solamente redes en la banda 2.4 GHz 
# Iniciar airodump

    sudo airodump-ng <interface>

# Criterios de captura

Usualmente vamos a usar 3 criterios al momento de capturar tráfico:

| Option | Desc |
|------|-------|
| -w | Nos permite agregar un prefijo a los archivos generados de la captura |
|--bssid | Nos permite indicar que bssid capturar de manera específica |
| -c | Fuera a airodump a capturar un canal en específico |
| --band | busca bandas entre 2.4 y 5 GHZ.  **a**= 5 ghZ, **b** = 2.4 GHz, **g** = 2.4 GHz|
| --ivs | captura solamente los IVs (Initialization Vectors) **Permite a AIRCRACK crackear claves WEP** |

# La finalidad de su uso

El fin de esta utilidad es capturar un protocolo de enlace(handshake) WPA. Esto aparecerá en la primer línea superior.

    CH  2 ][ Elapsed: 12 s ][ 2011-11-06 13:31 ][ WPA handshake: C8:BC:C8:FE:D9:65

Luego de esto, podemos realizar una nueva captura sobre la bssid de la que encontramos el handshake.

# Descubrimiento de redes ocultas

Algunas redes se encuentran como ocultas de una manera simple para las interfaces comunes por GUI mediante un ESSID "vacío".

Con airmon apareceran pero, dentro del ESSID se encontrará un length.

### Buscar su nombre por fuerza bruta
Los modos de fuerza bruta son:


| modo | letra |
|---|---|
|Upper case | u |
|digits | n|
| all printed | a |
|lower and upper case | c |
| lower and uppercase plus numbers | m|

    sudo mdk3 <interfaz> p -b <modo> -c <channel> -t <BSSID>

### Buscar su nombre por ataque de diccionario

    sudo mdk3 <interfaz> p -f <dictio> -t <BSSID>
