# APK instalada en el dispositivo

#### listamos las apps instaladas

    adb shell pm list packages -f -3  

  Recibiremos una respuesta de este tipo:

    adb shell pm list packages -f -3          
    package:/data/app/host.exp.exponent-pbiVw4kHQrbMZDhpj587eA==/base.apk=host.exp.exponent
    package:/data/app/com.tunnelworkshop.postern-jRpmZyPzWzumRo8zZe-A5A==/base.apk=com.tunnelworkshop.postern

#### Extraemos la APK con adb

hacemos un pull con el path absoluto a la apk que queremos

    adb pull /data/...*....apk
