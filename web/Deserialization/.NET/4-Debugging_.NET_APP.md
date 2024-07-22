### INFO

Muchas apps en .NET como las webs no están configuradas para correr como stand alone. Para esto deberemos configurar un servidor. Aquí el módulo donde configurarlo.

https://github.com/LaPorota/LaPorota_suite/blob/main/web/servers/Config_UP_IIS.md

### Extra:
Si IIS no nos está permitiendo hacer de manera correcta el debug debido a la optimización, podemos correr el siguiente script de powershell:

    https://gist.githubusercontent.com/richardszalay/59664cd302e66511618f51eaaa77db26/raw/e6f28fd32b693f9f98c538c63880c3eb50e317f4/IISAssemblyDebugging.psm1


    Import-Module .\IISAssemblyDebugging.psm1
    Enable-IISAssemblyDebugging C:\inetpub\wwwroot\TeeTrove.Publish\


### dnSpy

##### Instalación
En su repositorio tenemos varios releases portables para descargar:


        https://github.com/dnSpyEx/dnSpy/releases


#### Debugging

1) Abrir dnSpy como administrador.
2) File > open y seleccinamos todas las dlls de la carpeta de la aplicación
3) Debug > Attach process y debería aparecernos el exe w3wp. Si no funciona, podemos enviar una request a la aplicación (desde el navegador) y refreshear el dnSpy
4) Podemos ahora poner breakpoints en el código y desde el browser hacer llamados para poder ver qué es lo que se está ejecutando en el momento.
