# Info

### ¿Qué es?
Frida es una herramienta que permite ver qué está pasando dentro de una app. Podríamos comparar su proceder con el de un debugger.

### Hooking

Dentro de frida, se llama **HOOKING** a la técnica de interceptar y alterar funcionalidades o métodos dentro de una aplicación o el SO.


# Instalación

    pip3 install frida-tools
    pip3 install objection

#### descargar la versión correspondiente a la versión instalada:

    https://github.com/frida/frida/releases

Si no sabemos qué versión de SO estamos atacando:

    adb shell getprop ro.product.cpu.abi

#### Extraer los archivos

    xz -d frida-server-*-android-arm64.xz
    mv frida-server-* frida server

#### Pasarlos al device

    adb push frida-server /data/local/tmp/
    adb shell "chmod 775 /data/local/tmp/frida-server"

### Correr frida

    adb shell "/data/local/tmp/frida-server &"

# Usos importantes

1. Permite capturar funciones de una app "on the fly".
2. Nos permite ver qué está pasando por detrás del programa mientras corre y cambiar cosas.
3. Nos permite debuggear programas en tiempo real


### Listar apps instaladas con el PID

    frida-ps -Uai

### Comenzar a trabajar con una app mediante el nombre

    frida -U -f package_name

### Conectarse mediante las APIs de frida a una app

    frida -U -p <PID>

### Listar funciones dentro las librerias de una app

    frida-trace -U -p <PID> -i "<nombre-fncion"

# LO siguiente no se hace, chingüegüenzas

### Redirigir el tráfico con frida

Creamos un archivo .js


    Java.perform(function() {
      var classRef = Java.use("<package_name>.<class>");
      classRef.<method_to_hook>.implementation = function(args) {
        // Custom logic to execute when the method is called
      }
    });



### Interceptamos con frida el browser y lo mandamos y le decimos que ejecte el archivo

    frida -U -p <PID> -l archivo.js

### Correr los codeshares

    frida --codeshare <codeshare> -U -p <PID>


# Frida Codeshare

Frida tiene su comunidad con códgos ya creados para que podamos aprovecharlos para realizar explotaciones.

    https://codeshare.frida.re
