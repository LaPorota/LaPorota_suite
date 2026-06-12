# instalación

    pip3 install frida-tools
    pip3 install objection

#### descargar la versión correspondiente a la versión instalada:

    https://github.com/frida/frida/releases

#### Extraer los archivos

    xz -d frida-server-*-android-arm64.xz
    mv frida-server-* frida server

#### Pasarlos al device

    adb push frida-server /data/local/tmp/
    adb shell "chmod 775 /data/local/tmp/frida-server"

### Correr frida

    adb shell "/data/local/tmp/frida-server &"

### Listar apps instaladas con el PID

    frida-ps -Uai

### Conectarse mediante las APIs de frida mediante una app

    frida -U -p <PID>

### Listar funciones dentro las librerias de una app

    frida-trace -U -p <PID> -i "<nombre-fncion"

# LO siguiente no se hace, chingüegüenzas

### Redirigir el tráfico con frida

Creamos un archivo .js


    Java.use("android.webkit.WebView")loadUrl.overload("java.lang.String").implementation = function(url) {
        console.log("WebView.loadUrl() called with URL: " + url);
        const newURL= "urlmaliciosa";
        this.loadUrl.overload("java.lang.String").call(this, newUrl);


### Interceptamos con frida el browser y lo mandamos y le decimos que ejecte el archivo

    frida -U -p <PID> -l archivo.js

### Correr los codeshares

    frida --codeshare <codeshare> -U -p <PID>


# Frida Codeshare

Frida tiene su comunidad con códgos ya creados para que podamos aprovecharlos para realizar explotaciones.

    https://codeshare.frida.re
