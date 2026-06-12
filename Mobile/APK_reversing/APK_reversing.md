# ApkTool

#### descompilar

    apktool d <apk>

#### Rebuild después de modificar

     apktool b .

#### Crear un certificado para la app

    keytool -genkey -V -keystore key.keystore -alias APKtool -keyalg RSA -keysize 2048 -validity 10000

#### aplicar el cert

    jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore key.keystore [name].apk APKtool

#### Instalar apk

    adb install r <apk>


