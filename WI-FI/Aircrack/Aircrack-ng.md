# Info

- Puede crackear redes WEP y WPA/WPA2 que usan pre-shared keys o PMKID
- Aircrack trabaja de manera offline con paquetes capturados.


# Prueba de CPU con aircrack 

Nos permite hacer la prueba de cuántas pass-phrases puede crackear nuestro CPU por segundo.

    aircrack-ng -S


# Crackear claves WEP

Luego de capturar muchos paquetes de IVs con Airodump.

    aircrack-ng -K <captura.ivs>

# Crackear WPA

Luego de capturar el "four-way handshake" podemos realizar un ataque de diccionario sobre el pcap

    aircrack-ng <pcap> -w <dictio>
