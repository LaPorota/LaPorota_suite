# Construir el proxy dentro de LDPLAYER

## Habilitar la conexión puente

1. Abre LDPlayer y haz clic en el ícono de Configuración (engranaje) en el menú lateral.
2. Ve a la sección Red (Network).
3. Activa la opción Conexión en puente de red (Network Bridging) y guarda los cambios.

## Descargar Postern

 1. Abre el navegador del emulador o Google Play.
 2. Busca, descarga e instala la aplicación Postern.
 3. Agregar los datos del Proxy
 4. Abre la app Postern dentro del emulador.
 5. Dirígete a la sección Agregar Proxy.
 6. Rellena los datos de tu servidor proxy
 7. Configurar la regla de enrutamientoEn el menú principal de Postern, ve a la opción Reglas (Rules).
 8. Añade una nueva regla.En Coincidencia de objetivos (Match Method), selecciona Cualquiera (Any).
 9. En Objetivo (Target), selecciona el proxy que acabas de configurar y guarda la regla.

# Importar certificado

1. Crear el certificado en burp con formato DER
2. Transformarlo en certificado de android

#### transormar el cert en pem

    openssl x509 -inform DER -in cacert.der -out cacert.pem

#### sacar el hash

    openssl x509 -inform PEM -subject_hash_old -in cacert.pem |head -1

#### Crear el cert

    mv cacert.pem <hash>.0


#### Agrergarlo

    abd root
    abd remount
    adb push <cert>.0 /sdcard/
    adb shell
    mv /sdcard/<cert>.0 /system/etc/security/cacerts/
    chmod 644 /system/etc/security/cacarts/<cert>.o
    reboot

