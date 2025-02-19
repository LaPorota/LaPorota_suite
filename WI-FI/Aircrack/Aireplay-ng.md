# INfo
- Herramienta útil para generar tráfico inalámbrico.
- Podemos usarlo en conjunto con aircrack para descifrar claves WEP y WPA-PSK.
- Nos permite generar varios ataques.

### Ataques permitidos 

De la tabla siguiente las que son relevantes a WPA son la 0 y la 9. El resto son específicos de WEP

Los ataques se indican en la línea de comandos como flag utilizando su número: si quisieramos hacer un **fake authentication** deberíamos indicarlo dentro del comando como **"-1"**

|Attack #	| Attack Name|
|----|-----|
|0	|Deauthentication|
|1	|Fake Authentication|
|2	|Interactive Packet Replay|
|3	|ARP Request Replay Attack|
|4	|KoreK ChopChop Attack|
|5	|Fragmentation Attack|
|6	|Café-Latte Attack|
|7	|Client-Oriented Fragmentation Attack|
|8	|WPA Migration Mode Attack|
|9	|Injection Test|


# INjection Test

Previo a intentar cualquier ataque debemos estar seguros de que nuestra interfaz de red es capás de inyectar paquetes en la red target.

Si tenemos más de una placa de red esto también nos permite saber cual es más propicia a ser exitosa.

### Teoría

1) El injection test enumera los AP (access points) que responden a las sondas de transmisión.
2) Aireplay realiza una prueba de 30 frames para medir la calidad de la conexión.

Con esto podremos saber si nuestra tarjeta puede enviar y recibir correctamente una respuesta de los objetivos.

### El ataque

#### 1) Configuramos nuestra placa en modo monitor en el canal específico donde esté nuestro objetivo.

#### 2) Luego corremos aireplay con el tipo de ataque y la interfaz

    sudo aireplay-ng -9 <interfaz>

#### 3) con el resultado podemos inyectar en un SSID específico



#### Ejemplo:

Supongamos que encontramos los siguientes AP en el punto anterior

    kali@kali:~$ sudo aireplay-ng -9 wlan0mon
    12:02:10  Trying broadcast probe requests...
    12:02:10  Injection is working!
    12:02:11  Found 2 APs
    
    12:02:12  34:08:04:09:3D:38 - channel: 3 - 'wifu'
    12:02:13  Ping (min/avg/max): 1.455ms/4.163ms/12.006ms Power: -37.63
    12:02:13  30/30: 100%
    
    12:02:13  C8:BC:C8:FE:D9:65 - channel: 2 - 'secnet'
    12:02:13  Ping (min/avg/max): 1.637ms/4.516ms/18.474ms Power: -28.90
    12:02:13  30/30: 100%

Podríamos probar una prueba de inyección en el primer objetivo (wifu)

    sudo aireplay-ng -9 -e wifu -a 34:08:04:09:3D:38 wlan0mon

### Prueba de inyección de tarjeta-a-tarjeta

Vuelve más robustas las pruebas, normalizando el envío de frames entre las tarjetas que tenemos. Va a realizar también una comprobación de los ataques posibles sobre el objetivo.

    sudo aireplay-ng -9 -i <interfaz> <interfaz_adicional>
