# Requisitos

- Un usuario miembro del Administrators group

- Utiliza clases y namespases:

| clases | Desc |
|---|---|
|Win32_OperatingSystem | Trae detalles del OS|
|Win32_Process | Permite gestionar procesos |
|Win32_service | Permite gestionar servicios|
|Win32_ComputerSystem | Para traer informacipin general del sistema |

# Desde Windows

### WMIC
Linea de comandos que permite a los administradores gestionar aspectos del sistema.

##### Extraer información

    wmic /user:username /password:password /node:172.20.0.52 os get Caption,CSDVersion,OSArchitecture,Version

##### Ejecutar procesos

    wmic /user:username /password:password /node:172.20.0.52 process call create "notepad.exe"

### Powershell

##### Extraer información

    Get-WmiObject -Class Win32_OperatingSystem -ComputerName 172.20.0.52 | Select-Object Caption, CSDVersion, OSArchitecture, Version -Credential $credential

##### Iniciar un proceso

    Invoke-WmiMethod -Class Win32_Process -Name Create -ArgumentList "notepad.exe" -ComputerName 172.20.0.52 -Credential $credential

##### Ejecutar un comando

    Invoke-WmiMethod -Class Win32_Process -Name Create -ArgumentList "powershell..." -ComputerName 172.20.0.52 -Credential $credential

# Desde linux

### wmi-client

##### Instalación

    sudo apt-get install wmi-client

##### Extraer información

    wmic -U inlanefreight.local/helen%RedRiot88 //172.20.0.52 "SELECT Caption, CSDVersion, OSArchitecture, Version FROM Win32_OperatingSystem"

### wmiexec.py

- Pertenece a impacket.
- Usa el 445 para traer el output. si el 445 está bloqueado no funciona.
- Si queremos omitir el output  podemos usar -silentcommand o -nooutput

##### Correr comandos

    wmiexec.py inlanefreight/helen:RedRiot88@172.20.0.52 whoami

### NetExec

##### Extraer información

    netexec wmi 172.20.0.52 -u helen -p RedRiot88 --wmi "SELECT * FROM Win32_OperatingSystem"

##### Correr comandos

    netexec wmi 172.20.0.52 -u helen -p RedRiot88 -x whoami
