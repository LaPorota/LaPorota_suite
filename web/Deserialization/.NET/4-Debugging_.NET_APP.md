### INFO

Muchas apps en .NET como las webs no están configuradas para correr como stand alone. Para esto deberemos configurar un servidor. Aquí el módulo donde configurarlo.

https://github.com/LaPorota/LaPorota_suite/blob/main/web/servers/Config_UP_IIS.md

### Extra:
Si IIS no nos está permitiendo hacer de manera correcta el debug debido a la optimización, podemos correr el siguiente script de powershell:

    https://gist.githubusercontent.com/richardszalay/59664cd302e66511618f51eaaa77db26/raw/e6f28fd32b693f9f98c538c63880c3eb50e317f4/IISAssemblyDebugging.psm1


    Import-Module .\IISAssemblyDebugging.psm1
    C:\> Enable-IISAssemblyDebugging C:\inetpub\wwwroot\TeeTrove.Publish\
