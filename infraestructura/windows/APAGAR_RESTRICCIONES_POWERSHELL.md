### Permitir correr scripts:

    set-executionpolicy remotesigned


o

    Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser

### Apagar antivirus

    Powershell -ep bypass

### Apagar protección en tiempo real

    Set-MpPreference -DisableRealTimeMonitoring $true

### Shellter

Podemos usar shellter para crear binarios maliciosos con shell reversas que evadan los antivirus

apt-cache search shellter

sudo apt install shellter

sudo apt install wine

dpkg --add-architecture i386 && apt-get update && apt-get install wine32

Luego corremos shellter como comando y creamos nuestro binario malicioso.
