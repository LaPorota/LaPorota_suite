# Info

- Windows Remote Management es un protocolo standard para hacer managing de software y hardware de manera remota.
- Brinda un método seguro y eficiente de transferir datos entre computadores.
- Aprovecha los estandares web para garantizar compatibilidad.
- Por defecto usa los puertos **5985** para HTTP y **5986** para HTTPs.


# Qué usuarios pueden aprovecharlo?

- Usuarios administrativos
- Usuarios no administrativos con permisos específicos.
- Un usuario miembro de "Remote Management Users"

# Enumeración

### Nmap

    nmap -p5985,5986 10.129.229.244 -sCV

El HTTP suele saltar como **Microsoft HTTPAPI httpd 2.0**


### NetExec

    netexec winrm 10.129.229.244 -u frewdy -p Kiosko093

