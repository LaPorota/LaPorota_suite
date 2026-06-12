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
    adb shell "/data/local/tmp/frida-server &"

