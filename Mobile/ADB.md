# Android Debug Bridge

## Instalación

#### Linux

    sudo apt update && sudo apt install android-tools-adb

#### Windows

    https://developer.android.com/tools/releases/platform-tools?hl=es-419

## Comandos básicos

#### Listar dispositivos

    adb devices

#### Conectarse a un dispositivo

    adb connect

#### Instalar un apk

    adb install

#### Iniciar una shell en el dispositivo

    adb shell

#### Uploadear archivos

    adb push

#### Descargar archivos

    adb pull

#### Ver el log de adb

    adb logcat

#### Entrar a un device como root

    adb root
#### Listar apps de terceros instaladas

    adb shell pm list packages -f -3
    
#### Proxy para burp

    adb shell settings put global http_proxy [burp_host_ip]:8080

## Manual

    https://developer.android.com/tools/adb?hl=es-419
